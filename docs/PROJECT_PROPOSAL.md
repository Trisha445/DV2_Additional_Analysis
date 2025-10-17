# FIT3179 Data Visualisation 2 - Project Proposal

## Student Information
**Student Name:** Trisha Bhagat
**Student ID:**  33925216 

---

## Project Overview

### Domain: Australian Labour Market and Wage Analysis
**Why:** This visualisation addresses the critical need to understand regional employment patterns and wage dynamics across Australia. By combining employment rates with wage price index data, it reveals the economic reality behind job markets - not just whether people are employed, but how well they are compensated. This targets policymakers, job seekers, employers, and regional development officers who need insights into both employment opportunities and wage competitiveness across states.

**Who:** Designed for the average Australian interested in employment trends, wage growth patterns, and regional economic conditions. The visualisation will be accessible to general audiences without requiring statistical expertise, while providing sufficient depth for policy analysis.

**What:** The visualisation combines official Australian Bureau of Statistics employment data with wage price index data to reveal spatial patterns in both labour market participation and wage growth across Australian states and territories, creating a comprehensive picture of regional economic health.

---

## Data Sources

### Primary Dataset: Labour Force Statistics
**Source:** Australian Bureau of Statistics (ABS)  
**Publication:** Labour Force, Australia, Detailed - Table 02  
**URL:** https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia-detailed/aug-2025/6291002.xlsx  
**Catalogue:** 6291.0.55.001  
**Release Date:** 25 September 2025  

**Attributes:**
- **State/Territory:** Categorical (8 regions)
- **Employment Rate:** Quantitative (percentage)
- **Unemployment Rate:** Quantitative (percentage) 
- **Participation Rate:** Quantitative (percentage)
- **Labour Force:** Quantitative (persons)
- **Population:** Quantitative (persons)
- **Time Period:** Ordinal (quarterly data)

### Secondary Dataset: Wage Price Index
**Source:** Australian Bureau of Statistics (ABS)  
**Publication:** Wage Price Index, Australia - Table 9  
**URL:** https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/wage-price-index-australia/sep-2025/6345009.xlsx  
**Catalogue:** 6345.0  
**Release Date:** 25 October 2025  

**Attributes:**
- **State/Territory:** Categorical (8 regions)
- **Wage Price Index:** Quantitative (index points, base 2017=100)
- **Annual Wage Growth Rate:** Quantitative (percentage change)
- **Quarter:** Ordinal (quarterly data, Q3 2025)
- **Industry Sector:** Categorical (all sectors combined)
- **Reference Base:** 2017 = 100.0

### Geographic Data
**Source:** Natural Earth Data / D3 Gallery  
**Format:** GeoJSON for Australian state boundaries  
**Purpose:** Provides spatial geometry for choropleth mapping

---

## Data Transformation

### Normalisation
- **Employment rates** already normalised as percentages of working-age population
- **Wage indices** standardised to base year 2017=100 for temporal comparability
- **Wage growth rates** calculated as annual percentage change for cross-state comparison
- **Regional comparisons** standardised using population-weighted metrics

### Spatial Processing
- State/Territory codes standardised between datasets (NSW, VIC, QLD, etc.)
- Geographic boundaries simplified for web performance (<1MB total)
- Coordinate system: WGS84 (EPSG:4326) for web compatibility
- Wage data spatially joined to employment data by state identifier

### Temporal Aggregation
- Quarterly data focused on latest quarter (Q3 2025) for current snapshot
- Wage growth calculated year-over-year for Q3 2024 to Q3 2025
- Employment data synchronized to same temporal reference point

---

## Visualisation Design

### Map Idiom Justification: Choropleth + Proportional Symbols

**Choropleth Map (Employment Rates):**
- **Why Choropleth:** Employment rate is an intensive property (ratio/percentage) that represents the characteristic of each region rather than a raw count. Choropleth mapping is ideal for showing how this rate varies across geographic areas.
- **Why Not Proportional Symbols:** Employment rate as a percentage doesn't have magnitude that would be well-represented by symbol size.

**Proportional Symbol Map (Wage Growth):**
- **Why Proportional Symbols:** Wage price indices are comparative measures that benefit from size encoding to show relative wage competitiveness. Circle size can effectively represent the magnitude of wage growth differences between states.
- **Why Not Choropleth:** Wage indices represent point values rather than area characteristics, making proportional symbols more appropriate for showing relative economic performance.

### Visual Encoding Strategy
- **Color (Hue/Saturation):** Sequential blue scheme for employment rates (ColorBrewer)
- **Size:** Circle area proportional to wage price index values
- **Position:** Geographic coordinates (longitude/latitude)
- **Interactive Elements:** Hover tooltips showing both employment and wage data, filtering by time period

### Map Projection
- **Projection:** Albers Equal-Area Conic (optimised for Australia using Projection Wizard)
- **Justification:** Preserves area relationships crucial for choropleth interpretation while minimising distortion across Australia's extent

---

## Innovation & Features

### Novel Approach
- **Employment-Wage Integration** pioneering the spatial analysis of labour market participation alongside wage competitiveness in a unified visualization
- **Economic Health Mapping** revealing the relationship between employment success and wage growth across Australian regions
- **Multi-dimensional Labour Analysis** combining supply-side employment data with compensation trends to show complete labour market picture
- **Regional Economic Performance** highlighting states with strong employment AND competitive wage growth versus those facing challenges in either dimension

### Advanced Interactions & Custom Elements
- **Coordinated multi-view design** with synchronized highlighting between employment choropleth and wage symbols
- **Dual-metric tooltips** providing comprehensive regional labour market summaries including employment rates, wage indices, and growth rates
- **Interactive projection switching** allowing users to compare different map projections optimized for Australian geography
- **Dynamic temporal controls** for exploring wage growth trends over time
- **Responsive design** adapting to different screen sizes while maintaining data clarity

### Design Excellence & Theoretical Foundation
- **Advanced figure-ground relationships** using carefully calibrated color palettes from ColorBrewer 2.0 for optimal perception
- **Sophisticated visual hierarchy** implementing Gestalt principles to guide attention flow from overview to detail
- **Typography system** using modular scale and optimal line heights for enhanced readability across devices
- **Cognitive load optimization** balancing information density with comprehension through progressive disclosure

---

## Theoretical Framework & Methodology

### Conceptual Foundation
**Labour Market Geography Theory:** Builds on Peck (1996) and Storper & Walker (1989) concepts of uneven geographical development in labour markets, examining spatial variations in employment supply and demand relationships.

**Spatial Mismatch Hypothesis:** Tests Kain's (1968) theory adapted to Australian context - examining geographic disconnects between where jobs are available versus where unemployed populations reside.

### Analytical Framework
**Munzner's What-Why-How:** 
- **What:** Spatial + temporal employment data (networks, fields, geometry)
- **Why:** Analyze distribution patterns, identify anomalies, compare trends
- **How:** Choropleth encoding for intensive properties, symbol mapping for extensive data, coordinated multiple views

### Five Design-Sheet Methodology Integration
- **Sheet 1:** Explored scatter plots, bar charts, basic maps
- **Sheet 2:** Refined to dual-layer geographic approach with interactivity sketches  
- **Sheet 3:** Detailed encoding decisions and projection testing
- **Sheet 4:** Layout considerations and responsive design planning
- **Sheet 5:** Final integrated design with annotation strategy

## Expected Insights & Research Questions

### Primary Research Questions
1. **Regional Economic Health:** Which Australian states demonstrate optimal employment rates coupled with competitive wage growth, indicating healthy labour markets?
2. **Employment-Wage Relationships:** How do employment participation rates correlate with wage price index values across different states and territories?
3. **Regional Competitiveness:** Which regions offer the best combination of job availability and wage growth for Australian workers?
4. **Policy Insights:** Where do employment and wage patterns suggest the need for targeted economic development or labour market interventions?

### Anticipated Research Contributions
- **Methodological Innovation:** Pioneer integrated employment-wage mapping approach combining labour market participation with compensation analysis
- **Policy Applications:** Identify geographic priority areas for Australian Government economic development and workforce strategies
- **Economic Geography Insights:** Reveal spatial patterns in post-pandemic labour market recovery and wage competitiveness across Australian states
- **Data Visualization Advancement:** Demonstrate effective techniques for encoding multiple economic indicators in spatial visualizations

---

## Technical Specifications

### Performance Requirements
- **Total data size:** <1MB (compliant with assignment requirements)
- **Load time:** <3 seconds on standard broadband
- **Compatibility:** Modern web browsers, responsive design

### Accessibility
- **Color schemes:** ColorBrewer palettes suitable for colorblind users
- **Text alternatives:** Comprehensive tooltips and annotations
- **Keyboard navigation:** Full interactivity without mouse dependency

---

## License & Attribution
**Data License:** Creative Commons Attribution 4.0 International  
**Attribution:** Australian Bureau of Statistics, 2025  
**Usage Rights:** Suitable for academic and educational purposes  

---

**Proposal Date:** 28 September 2025  
**Expected Completion:** Week 11, 2025