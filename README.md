# 🇦🇺 Australian Labour Market Analysis Dashboard

**FIT3179 Data Visualisation 2 - Advanced Analytics Project**

[![Live Dashboard](https://img.shields.io/badge/Live%20Dashboard-GitHub%20Pages-brightgreen?style=for-the-badge&logo=github)](https://trisha445.github.io/DV2_Additional_Analysis/)
[![Data Source](https://img.shields.io/badge/Data%20Source-Australian%20Bureau%20of%20Statistics-blue?style=flat-square)](https://www.abs.gov.au/)
[![Vega-Lite](https://img.shields.io/badge/Built%20with-Vega--Lite%205.20.0-orange?style=flat-square)](https://vega.github.io/vega-lite/)

---

## 🎯 Project Overview

A comprehensive, interactive dashboard analyzing Australia's labour market dynamics through advanced data visualization techniques. This project demonstrates the relationship between employment rates, wage indices, and job market opportunities across Australian states and territories.

### **🌐 [View Live Dashboard](https://trisha445.github.io/DV2_Additional_Analysis/)**

---

## 📊 Key Visualizations

### 1. **Geographic Employment Distribution**
- **Type**: Interactive Choropleth Map
- **Data**: Employment rates by state/territory
- **Features**: Graticule overlay, optimized projection, interactive tooltips
- **Insights**: ACT leads (67.2%), SA lowest (59.8%)

### 2. **Employment vs Wage Correlation**
- **Type**: Annotated Scatter Plot with Interactive Filters
- **Data**: Employment rates vs wage indices
- **Features**: Complete annotation system, responsive design, no horizontal scroll
- **Insights**: Strong positive correlation, resource states excel in wages

### 3. **Economic Performance Bubbles**
- **Type**: Modular Bubble Chart (External JSON)
- **Data**: Multi-dimensional economic metrics
- **Features**: Professional grid system, circular legends, GitHub Pages deployment
- **Insights**: Queensland achieves highest economic performance (62.6)

### 4. **Job Market Opportunities**
- **Type**: Interactive Bar Chart
- **Data**: Job vacancies by state with filtering
- **Features**: Dynamic wage growth filtering, responsive design
- **Insights**: NSW dominates with 1.14M vacancies, eastern states control 78%

---

## 🛠️ Technical Implementation

### **Frontend Architecture**
- **Framework**: Pure HTML5/CSS3/JavaScript
- **Visualization Library**: Vega-Lite 5.20.0 with VegaEmbed
- **Design System**: Custom CSS with professional gradients and responsive layouts
- **Typography**: Inter + Georgia font stack for optimal readability

### **Data Pipeline**
- **Source**: Australian Bureau of Statistics (ABS)
- **Processing**: Python scripts for data cleaning and merging
- **Format**: CSV + GeoJSON for optimal performance
- **Validation**: Comprehensive error checking and data integrity

### **Advanced Features**
- ✅ **Modular Architecture**: External JSON specifications for maintainability
- ✅ **Responsive Design**: Mobile-first approach with breakpoint optimization
- ✅ **Interactive Filtering**: Real-time data exploration capabilities
- ✅ **Professional Annotations**: Complete highest/lowest highlighting system
- ✅ **Zero Horizontal Scroll**: Optimized layout for all screen sizes
- ✅ **GitHub Pages Deployment**: Automated CI/CD pipeline

---

## 📁 Project Structure

```
DV2_Additional_Analysis/
├── 📊 index.html                          # Main dashboard
├── 📈 assets/
│   ├── australia-states.geojson           # Geographic boundaries
│   ├── state_performance_bubblemap.json   # External bubble chart spec
│   └── *.html                             # Standalone chart files
├── 📂 data/
│   ├── merged_labour_data.csv             # Processed dataset
│   └── wage_data_cleaned.csv              # Wage indices
├── 🐍 src/
│   ├── merge_datasets.py                  # Data processing pipeline
│   └── clean_wage_data.py                 # Data cleaning utilities
├── 📋 docs/
│   ├── PROJECT_PROPOSAL.md                # Project specification
│   └── WEEK9_REPORT.md                    # Technical documentation
└── 🎨 assets/css/
    └── dashboard.css                       # Styling framework
```

---

## 🚀 Quick Start

### **Option 1: View Online**
Simply visit the [**Live Dashboard**](https://trisha445.github.io/DV2_Additional_Analysis/) - no setup required!

### **Option 2: Run Locally**
```bash
# Clone the repository
git clone https://github.com/Trisha445/DV2_Additional_Analysis.git
cd DV2_Additional_Analysis

# Start local server
python -m http.server 8000

# Open in browser
# Navigate to http://localhost:8000
```

---

## 📈 Data Sources & Methodology

### **Primary Dataset**
- **Source**: Australian Bureau of Statistics (ABS)
- **Tables**: Labour Force Survey (6291002), Wage Price Index
- **Coverage**: All 8 Australian states and territories
- **Temporal**: Latest available data (2024-2025)

### **Processing Pipeline**
1. **Data Extraction**: Direct ABS API integration
2. **Cleaning**: Missing value handling, outlier detection
3. **Normalization**: Rate calculations, standardization
4. **Validation**: Cross-reference checks, integrity verification
5. **Export**: Optimized CSV/JSON formats

### **Quality Assurance**
- ✅ **100% Coverage**: No missing states/territories
- ✅ **Data Integrity**: Comprehensive validation checks
- ✅ **Source Attribution**: Full ABS compliance and citations
- ✅ **Update Frequency**: Quarterly refresh capability

---

## 🎨 Design Philosophy

### **Visual Hierarchy**
- **Primary**: Interactive scatter plot for correlation analysis
- **Secondary**: Geographic context through choropleth mapping
- **Tertiary**: Supporting metrics via bubble and bar charts

### **User Experience**
- **Progressive Disclosure**: Layer information complexity appropriately
- **Interactive Exploration**: Enable user-driven data discovery
- **Responsive Design**: Seamless experience across all devices
- **Accessibility**: High contrast, screen reader compatibility

### **Professional Standards**
- **Color Theory**: Scientifically-backed palettes for data perception
- **Typography**: Optimized for reading comprehension
- **Layout**: Grid-based system for visual consistency
- **Performance**: Sub-2 second load times, optimized assets

---

## 🏆 Key Insights & Findings

### **Employment Landscape**
- **🥇 Top Performer**: ACT (67.2% employment rate)
- **📊 National Average**: 63.1% employment rate
- **📉 Improvement Opportunity**: SA (59.8% employment rate)

### **Economic Dynamics**
- **💰 Wage Leaders**: WA dominates with mining sector strength
- **📈 Growth Champions**: QLD achieves highest economic performance
- **🔄 Correlation Pattern**: Strong positive employment-wage relationship

### **Market Opportunities**
- **🎯 Volume Leaders**: NSW (1.14M vacancies), VIC, QLD
- **📍 Per Capita**: WA offers highest opportunity density
- **🏢 Sector Concentration**: Professional services drive eastern growth

---

## 🤝 Contributing

This project welcomes contributions! Areas for enhancement:

- **Data Sources**: Additional ABS tables, historical time series
- **Visualizations**: New chart types, advanced interactions
- **Performance**: Optimization, caching strategies
- **Accessibility**: Enhanced screen reader support, WCAG compliance

---

## 📄 License & Attribution

### **Code License**
MIT License - See [LICENSE](LICENSE) for details

### **Data Attribution**
- **Australian Bureau of Statistics**: Labour force and wage data
- **CC BY 4.0**: Geographic boundary data
- **Vega-Lite**: Visualization framework (BSD-3-Clause)

---

## 👤 Author

**Trisha Bhagat**  
*FIT3179 Data Visualisation 2*  
*Monash University*

[![GitHub](https://img.shields.io/badge/GitHub-Trisha445-black?style=flat-square&logo=github)](https://github.com/Trisha445)
[![Dashboard](https://img.shields.io/badge/Live%20Dashboard-View%20Now-brightgreen?style=flat-square)](https://trisha445.github.io/DV2_Additional_Analysis/)

---

## 📊 Project Stats

![Repo Size](https://img.shields.io/github/repo-size/Trisha445/DV2_Additional_Analysis)
![Last Commit](https://img.shields.io/github/last-commit/Trisha445/DV2_Additional_Analysis)
![Languages](https://img.shields.io/github/languages/count/Trisha445/DV2_Additional_Analysis)
![Top Language](https://img.shields.io/github/languages/top/Trisha445/DV2_Additional_Analysis)

---

*📈 Built with passion for data storytelling and evidence-based insights*