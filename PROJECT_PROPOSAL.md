# FIT3179 Data Visualisation 2 - Project Proposal

## Student Information
**Student Name:** Trisha Bhagat
**Student ID:**  33925216 

---

## Project Overview

### Domain: Australian Labour Market Analysis
**Why:** This visualisation addresses the critical need to understand regional employment patterns and job market dynamics across Australia. It targets policymakers, job seekers, employers, and regional development officers who need insights into where employment opportunities exist versus where people are actually employed.

**Who:** Designed for the average Australian interested in employment trends, job market conditions, and regional economic patterns. The visualisation will be accessible to general audiences without requiring statistical expertise.

**What:** The visualisation combines official Australian Bureau of Statistics employment and job vacancy data to reveal spatial patterns in labour market supply and demand across Australian states and territories.

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

### Secondary Dataset: Job Vacancies
**Source:** Australian Bureau of Statistics (ABS)  
**Publication:** Job Vacancies, Australia - Table 1  
**URL:** https://www.abs.gov.au/statistics/labour/jobs/job-vacancies-australia/aug-2025/6354001.xlsx  
**Catalogue:** 6354.0  
**Release Date:** 21 September 2025  

**Attributes:**
- **State/Territory:** Categorical (8 regions)
- **Job Vacancies:** Quantitative (number of positions)
- **Industry:** Categorical (industry divisions)
- **Quarter:** Ordinal (time period)
- **Sector:** Categorical (public/private)

### Geographic Data
**Source:** Natural Earth Data / D3 Gallery  
**Format:** GeoJSON for Australian state boundaries  
**Purpose:** Provides spatial geometry for choropleth mapping

---

## Data Transformation

### Normalisation
- **Employment rates** already normalised as percentages of working-age population
- **Job vacancy rates** calculated per 1,000 labour force participants for comparability
- **Regional comparisons** standardised using population-weighted metrics

### Spatial Processing
- State/Territory codes standardised between datasets (NSW, VIC, QLD, etc.)
- Geographic boundaries simplified for web performance (<1MB total)
- Coordinate system: WGS84 (EPSG:4326) for web compatibility

### Temporal Aggregation
- Quarterly data averaged for trend analysis
- Latest quarter (Q3 2025) highlighted for current snapshot
- Year-over-year comparisons calculated where available

---

## Visualisation Design

### Map Idiom Justification: Choropleth + Proportional Symbols

**Choropleth Map (Employment Rates):**
- **Why Choropleth:** Employment rate is an intensive property (ratio/percentage) that represents the characteristic of each region rather than a raw count. Choropleth mapping is ideal for showing how this rate varies across geographic areas.
- **Why Not Proportional Symbols:** Employment rate as a percentage doesn't have magnitude that would be well-represented by symbol size.

**Proportional Symbol Map (Job Vacancies):**
- **Why Proportional Symbols:** Job vacancy counts are extensive properties (absolute numbers) that represent quantities that can be meaningfully compared by size. Larger circles indicate more job opportunities.
- **Why Not Choropleth:** Raw vacancy counts would create misleading patterns if shown as area fills, as larger states would appear to have higher rates simply due to size.

### Visual Encoding Strategy
- **Color (Hue/Saturation):** Sequential blue scheme for employment rates (ColorBrewer)
- **Size:** Circle area proportional to job vacancies 
- **Position:** Geographic coordinates (longitude/latitude)
- **Interactive Elements:** Hover tooltips, filtering by industry/time

### Map Projection
- **Projection:** Albers Equal-Area Conic (optimised for Australia using Projection Wizard)
- **Justification:** Preserves area relationships crucial for choropleth interpretation while minimising distortion across Australia's extent

---

## Innovation & Features

### Novel Approach
- **Dual-layer spatial analysis** pioneering the comparison of labour supply (employment) with labour demand (vacancies) in a single integrated view
- **Multi-temporal storytelling** revealing quarterly employment dynamics through animated transitions and time-series coordination
- **Sectoral decomposition** enabling industry-specific geographic analysis to identify skills-geography mismatches
- **Supply-demand tension mapping** highlighting regions with high employment but low vacancies (tight markets) vs low employment with high vacancies (opportunity zones)

### Advanced Interactions & Custom Elements
- **Coordinated multi-view design** with synchronized highlighting between map regions, temporal charts, and industry breakdowns
- **Custom tooltip narratives** providing contextual explanations of regional employment dynamics and policy implications  
- **Interactive projection switching** allowing users to compare different map projections optimized for Australian geography
- **Dynamic data filtering** with smooth transitions between time periods and industry sectors
- **Responsive legend positioning** adapting to screen size and data complexity

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
1. **Spatial Employment Efficiency:** Which Australian regions demonstrate optimal employment-to-vacancy ratios indicating efficient labour market matching?
2. **Geographic Labour Market Tensions:** Where do high employment rates coexist with low job vacancies (tight markets) versus high vacancies with low employment (skills gaps)?
3. **Regional Economic Resilience:** How do state-level employment patterns correlate with job creation capacity across different industries?
4. **Policy Intervention Opportunities:** Which geographic areas show the greatest potential for targeted workforce development or job creation initiatives?

### Anticipated Research Contributions
- **Methodological Innovation:** Pioneer dual-layer employment mapping approach combining supply-side (employment) with demand-side (vacancy) perspectives
- **Policy Implications:** Identify geographic priority areas for Australian Government workforce development programs  
- **Economic Geography Insights:** Reveal spatial patterns in post-pandemic labour market recovery across Australian states
- **Data Visualization Advancement:** Demonstrate effective techniques for encoding intensive vs extensive spatial properties

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