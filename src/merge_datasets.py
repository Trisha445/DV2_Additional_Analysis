#!/usr/bin/env python3
"""
Dataset Merger for Australian Labour Market Analysis
===================================================

This script merges the Labour Force dataset and Wage Index dataset on the 'State' column
and creates new derived metrics for comprehensive analysis.

Week 10 Requirements:
- Merge datasets on 'State' column
- Create 'Employment_to_Wage_Ratio' = EmploymentRate / WageIndex
- Save as 'merged_labour_data.csv' for Vega-Lite visualization
- Add job vacancy estimates for scatter plot size encoding

Author: Trisha Bhagat (33925216)
Date: October 10, 2025
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def load_datasets():
    """
    Load the cleaned labour force and wage datasets.
    """
    print("📥 Loading cleaned datasets...")
    
    try:
        # Load labour force data
        labour_df = pd.read_csv('data/labour_force_cleaned.csv')
        print(f"✅ Labour Force data loaded: {labour_df.shape[0]} rows, {labour_df.shape[1]} columns")
        
        # Load wage data
        wage_df = pd.read_csv('data/wage_data_cleaned.csv')
        print(f"✅ Wage Index data loaded: {wage_df.shape[0]} rows, {wage_df.shape[1]} columns")
        
        return labour_df, wage_df
    
    except FileNotFoundError as e:
        print(f"❌ Error loading datasets: {e}")
        print("💡 Make sure to run clean_wage_data.py first to generate the wage dataset")
        return None, None

def validate_merge_compatibility(labour_df, wage_df):
    """
    Validate that the datasets can be properly merged on the State column.
    """
    print("\n🔍 Validating merge compatibility...")
    
    # Check state columns
    labour_states = set(labour_df['State'].unique())
    wage_states = set(wage_df['State'].unique())
    
    print(f"📊 Labour Force states ({len(labour_states)}): {sorted(labour_states)}")
    print(f"💰 Wage Index states ({len(wage_states)}): {sorted(wage_states)}")
    
    # Find common states
    common_states = labour_states.intersection(wage_states)
    missing_in_wage = labour_states - wage_states
    missing_in_labour = wage_states - labour_states
    
    print(f"\n✅ Common states ({len(common_states)}): {sorted(common_states)}")
    
    if missing_in_wage:
        print(f"⚠️  States in Labour Force but not in Wage data: {missing_in_wage}")
    
    if missing_in_labour:
        print(f"⚠️  States in Wage data but not in Labour Force: {missing_in_labour}")
    
    # Check temporal alignment
    labour_quarters = labour_df['Year_Quarter'].unique()
    wage_quarters = wage_df['Year_Quarter'].unique()
    
    print(f"\n📅 Labour Force quarters: {labour_quarters}")
    print(f"📅 Wage Index quarters: {wage_quarters}")
    
    return len(common_states) >= 6  # Need at least 6 states for meaningful analysis

def create_job_vacancy_estimates(df):
    """
    Create realistic job vacancy estimates based on state characteristics.
    This simulates the data that would come from ABS Job Vacancies statistics.
    """
    print("🏢 Creating job vacancy estimates...")
    
    # Base vacancy rates per 1000 labour force (realistic Australian patterns)
    vacancy_rates = {
        'New South Wales': 28.5,          # High urban demand
        'Victoria': 26.8,                 # Strong services sector
        'Queensland': 24.2,               # Tourism and resources
        'Western Australia': 32.1,        # Mining boom effect
        'South Australia': 21.4,          # Manufacturing transition
        'Tasmania': 19.8,                 # Lower economic activity
        'Australian Capital Territory': 31.7,  # Government sector demand
        'Northern Territory': 29.3        # Skills shortages
    }
    
    # Calculate job vacancies
    df['Job_Vacancy_Rate'] = df['State'].map(vacancy_rates)
    df['Job_Vacancies'] = (df['Labour_Force'] * df['Job_Vacancy_Rate'] / 1000).round(0).astype(int)
    
    return df

def merge_datasets(labour_df, wage_df):
    """
    Merge the datasets and create derived metrics.
    """
    print("\n🔗 Merging datasets...")
    
    # Perform inner join on State column
    merged_df = pd.merge(
        labour_df, 
        wage_df, 
        on='State', 
        how='inner',
        suffixes=('_labour', '_wage')
    )
    
    print(f"✅ Merged dataset shape: {merged_df.shape[0]} rows, {merged_df.shape[1]} columns")
    
    # Create derived metrics
    print("🧮 Creating derived metrics...")
    
    # Employment to Wage Ratio (efficiency metric)
    merged_df['Employment_to_Wage_Ratio'] = (
        merged_df['Employment_Rate'] / merged_df['WageIndex'] * 100
    ).round(3)
    
    # Wage Growth Category
    merged_df['Wage_Growth_Category'] = pd.cut(
        merged_df['WageGrowthRate'],
        bins=[0, 2.0, 2.3, 3.0],
        labels=['Low Growth', 'Moderate Growth', 'High Growth'],
        include_lowest=True
    )
    
    # Employment Category
    merged_df['Employment_Category'] = pd.cut(
        merged_df['Employment_Rate'],
        bins=[0, 60, 65, 100],
        labels=['Below Average', 'Average', 'Above Average'],
        include_lowest=True
    )
    
    # Economic Performance Score (composite metric)
    # Normalize both metrics to 0-100 scale and take weighted average
    emp_norm = (merged_df['Employment_Rate'] - merged_df['Employment_Rate'].min()) / \
               (merged_df['Employment_Rate'].max() - merged_df['Employment_Rate'].min()) * 100
    
    wage_norm = (merged_df['WageGrowthRate'] - merged_df['WageGrowthRate'].min()) / \
                (merged_df['WageGrowthRate'].max() - merged_df['WageGrowthRate'].min()) * 100
    
    merged_df['Economic_Performance_Score'] = (
        0.6 * emp_norm + 0.4 * wage_norm
    ).round(1)
    
    # Add job vacancy estimates
    merged_df = create_job_vacancy_estimates(merged_df)
    
    return merged_df

def clean_merged_dataset(merged_df):
    """
    Clean and organize the merged dataset for visualization.
    """
    print("\n🧹 Cleaning merged dataset...")
    
    # Select and order columns for output
    output_columns = [
        'State',
        'State_Code_labour',  # Use labour dataset state codes as primary
        'Employment_Rate',
        'Unemployment_Rate', 
        'Participation_Rate',
        'Labour_Force',
        'Population',
        'WageIndex',
        'WageGrowthRate',
        'Employment_to_Wage_Ratio',
        'Job_Vacancies',
        'Job_Vacancy_Rate',
        'Economic_Performance_Score',
        'Employment_Category',
        'Wage_Growth_Category',
        'Year_Quarter'
    ]
    
    # Use the labour quarter as primary reference
    merged_df['Year_Quarter'] = merged_df['Year_Quarter_labour']
    
    final_df = merged_df[output_columns].copy()
    
    # Rename State_Code column to remove suffix
    final_df = final_df.rename(columns={'State_Code_labour': 'State_Code'})
    
    # Sort by Economic Performance Score descending
    final_df = final_df.sort_values('Economic_Performance_Score', ascending=False).reset_index(drop=True)
    
    print(f"✅ Final dataset shape: {final_df.shape[0]} rows, {final_df.shape[1]} columns")
    
    return final_df

def display_analysis_summary(df):
    """
    Display comprehensive analysis of the merged dataset.
    """
    print("\n" + "="*70)
    print("📊 MERGED DATASET ANALYSIS SUMMARY")
    print("="*70)
    
    print(f"\n📋 Dataset Overview:")
    print(f"   • Total states/territories: {len(df)}")
    print(f"   • Reference period: {df['Year_Quarter'].iloc[0]}")
    print(f"   • Data completeness: {(df.notna().sum().sum() / (len(df) * len(df.columns)) * 100):.1f}%")
    
    print(f"\n💼 Employment Statistics:")
    print(f"   • Mean employment rate: {df['Employment_Rate'].mean():.1f}%")
    print(f"   • Highest employment: {df['Employment_Rate'].max():.1f}% ({df[df['Employment_Rate'] == df['Employment_Rate'].max()]['State'].iloc[0]})")
    print(f"   • Lowest employment: {df['Employment_Rate'].min():.1f}% ({df[df['Employment_Rate'] == df['Employment_Rate'].min()]['State'].iloc[0]})")
    
    print(f"\n💰 Wage Index Statistics:")
    print(f"   • Mean wage index: {df['WageIndex'].mean():.1f}")
    print(f"   • Highest wages: {df['WageIndex'].max():.1f} ({df[df['WageIndex'] == df['WageIndex'].max()]['State'].iloc[0]})")
    print(f"   • Lowest wages: {df['WageIndex'].min():.1f} ({df[df['WageIndex'] == df['WageIndex'].min()]['State'].iloc[0]})")
    print(f"   • Mean wage growth: {df['WageGrowthRate'].mean():.2f}%")
    
    print(f"\n🏢 Job Market Dynamics:")
    print(f"   • Total job vacancies: {df['Job_Vacancies'].sum():,}")
    print(f"   • Average vacancy rate: {df['Job_Vacancy_Rate'].mean():.1f} per 1,000 workers")
    print(f"   • Highest vacancies: {df['Job_Vacancies'].max():,} ({df[df['Job_Vacancies'] == df['Job_Vacancies'].max()]['State'].iloc[0]})")
    
    print(f"\n⚖️ Economic Efficiency:")
    print(f"   • Mean Employment-to-Wage Ratio: {df['Employment_to_Wage_Ratio'].mean():.3f}")
    print(f"   • Most efficient: {df['Employment_to_Wage_Ratio'].max():.3f} ({df[df['Employment_to_Wage_Ratio'] == df['Employment_to_Wage_Ratio'].max()]['State'].iloc[0]})")
    print(f"   • Least efficient: {df['Employment_to_Wage_Ratio'].min():.3f} ({df[df['Employment_to_Wage_Ratio'] == df['Employment_to_Wage_Ratio'].min()]['State'].iloc[0]})")
    
    print(f"\n🎯 Top Performing States (by Economic Performance Score):")
    top_3 = df.head(3)
    for i, (_, row) in enumerate(top_3.iterrows(), 1):
        print(f"   {i}. {row['State']}: {row['Economic_Performance_Score']:.1f} points")
        print(f"      Employment: {row['Employment_Rate']:.1f}%, Wage Growth: {row['WageGrowthRate']:.2f}%")
    
    print(f"\n📈 Category Distribution:")
    emp_counts = df['Employment_Category'].value_counts()
    wage_counts = df['Wage_Growth_Category'].value_counts()
    
    print(f"   Employment Categories:")
    for cat, count in emp_counts.items():
        print(f"      • {cat}: {count} states")
    
    print(f"   Wage Growth Categories:")
    for cat, count in wage_counts.items():
        print(f"      • {cat}: {count} states")

def save_merged_dataset(df, output_path):
    """
    Save the merged dataset for Vega-Lite visualization.
    """
    print(f"\n💾 Saving merged dataset to: {output_path}")
    
    try:
        df.to_csv(output_path, index=False)
        print("✅ Successfully saved merged_labour_data.csv")
        
        # Verify the saved file
        verify_df = pd.read_csv(output_path)
        print(f"✓ Verification: File contains {len(verify_df)} rows and {len(verify_df.columns)} columns")
        
        return True
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

def main():
    """
    Main execution function for dataset merging.
    """
    print("🇦🇺 AUSTRALIAN LABOUR MARKET DATASET MERGER")
    print("=" * 55)
    print("Preparing integrated data for Week 10 scatter plot analysis\n")
    
    try:
        # Step 1: Load datasets
        labour_df, wage_df = load_datasets()
        if labour_df is None or wage_df is None:
            return None
        
        # Step 2: Validate merge compatibility
        if not validate_merge_compatibility(labour_df, wage_df):
            print("❌ Datasets are not compatible for merging")
            return None
        
        # Step 3: Merge datasets
        merged_df = merge_datasets(labour_df, wage_df)
        
        # Step 4: Clean and organize
        final_df = clean_merged_dataset(merged_df)
        
        # Step 5: Display analysis
        display_analysis_summary(final_df)
        
        # Step 6: Save merged dataset
        output_path = 'data/merged_labour_data.csv'
        success = save_merged_dataset(final_df, output_path)
        
        if success:
            print("\n🎉 SUCCESS! Merged dataset ready for Week 10 visualization")
            print("\n📋 Next steps for Week 10:")
            print("   1. Use merged_labour_data.csv for scatter plot")
            print("   2. x-axis: Employment_Rate")
            print("   3. y-axis: WageIndex") 
            print("   4. size: Job_Vacancies")
            print("   5. color: State or Economic_Performance_Score")
            print("   6. Add interactive tooltips and filters")
        
        return final_df
        
    except Exception as e:
        print(f"❌ Error in main execution: {e}")
        return None

if __name__ == "__main__":
    # Execute the merger pipeline
    merged_data = main()
    
    # Display final preview
    if merged_data is not None:
        print("\n" + "="*70)
        print("📋 FINAL MERGED DATASET PREVIEW")
        print("="*70)
        print(merged_data.to_string(index=False))
        print(f"\n✅ Merge complete! Dataset ready for Week 10 scatter plot visualization.")