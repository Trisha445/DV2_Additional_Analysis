# FIT3179 Data Visualisation - Week 9 Homework Report

## Student Information
**Name:** Trisha Bhagat  
**Student ID:** 33925216  
## GitHub Page URL

*(Publish this repository as GitHub Pages from the main branch or gh-pages branch; update the URL if you use a different path.)*

## Map Overview

### Domain of Visualisation
- Australian labour market geography — spatial analysis of employment rates across Australian states and territories (Q3 2025).

### Visualised Dataset  
- Source: Australian Bureau of Statistics (ABS) Labour Force Survey (Table 6291002, Aug 2025).  
- Attributes: State, State_Code, Employment_Rate (%), Unemployment_Rate (%), Participation_Rate (%), Labour_Force (persons), Population (persons), Year_Quarter.  
- Author: Australian Bureau of Statistics.

### Data Transformation
- No data manipulation of original ABS values. Employment rates are used as provided (percentages). All transformations are display-only (coordinate helper fields derived for point placement) and are documented in the report.

### Map Idiom Justification
- Choropleth (with complementary proportional symbols) chosen because Employment_Rate is an intensive property (percentage). Color encodes rate; symbol size encodes labour force magnitude for additional context.

---

## Technical Implementation

### Map Features Implemented
- Appropriate projection: Conic equal-area / Albers (Australia-optimised).
- Graticule included and ocean background applied.
- Australia state boundaries (GeoJSON) used for accurate choropleth background.
- Proportional symbols (circles) sized by Labour_Force; color scale for Employment_Rate.
- Clear legends for colour and size, human-readable labels, and formatted tooltips.
- Accessible, colorblind-friendly palettes (viridis/plasma alternatives) used.

### Design Principles Applied
- Figure-ground separation, muted base colours and vibrant data encoding.
- Sequential colour scale for rates (no diverging scale).
- Minimal empty space: projection and translate/scale tuned for Australia extent.
- Labels and legends positioned to avoid overlap and improve readability.

### Data Quality Assurance
- No missing jurisdictions; all 8 states/territories included.
- Original ABS values preserved; no derived metrics used for scoring.
- File sizes kept small to ensure fast load times.

## Expected Insights
- The visualization highlights regional differences in employment rates and the relative scale of labour forces by state, supporting regional labour market analysis and planning.

## Notes for Submission
- Ensure `index.html` embeds `js/week9_homework_map.json` (Vega-Lite) and the `data/labour_force_cleaned.csv` file is present.  
- After pushing, enable GitHub Pages in the repository settings (use main or gh-pages) and verify the published URL above.
# FIT3179 Data Visualisation - Week 9 Homework Report

## Student Information
**Name:** Trisha Bhagat  
**Student ID:** 33925216  
## GitHub Page URL

*(Publish this repository as GitHub Pages from the main branch or gh-pages branch; update the URL if you use a different path.)*

## Map Overview

### Domain of Visualisation
- Australian labour market geography — spatial analysis of employment rates across Australian states and territories (Q3 2025).

### Visualised Dataset  
- Source: Australian Bureau of Statistics (ABS) Labour Force Survey (Table 6291002, Aug 2025).  
- Attributes: State, State_Code, Employment_Rate (%), Unemployment_Rate (%), Participation_Rate (%), Labour_Force (persons), Population (persons), Year_Quarter.  
- Author: Australian Bureau of Statistics.

### Data Transformation
- No data manipulation of original ABS values. Employment rates are used as provided (percentages). All transformations are display-only (coordinate helper fields derived for point placement) and are documented in the report.

### Map Idiom Justification
- Choropleth (with complementary proportional symbols) chosen because Employment_Rate is an intensive property (percentage). Color encodes rate; symbol size encodes labour force magnitude for additional context.

---

## Technical Implementation

### Map Features Implemented
- Appropriate projection: Conic equal-area / Albers (Australia-optimised).
- Graticule included and ocean background applied.
- Australia state boundaries (GeoJSON) used for accurate choropleth background.
- Proportional symbols (circles) sized by Labour_Force; color scale for Employment_Rate.
- Clear legends for colour and size, human-readable labels, and formatted tooltips.
- Accessible, colorblind-friendly palettes (viridis/plasma alternatives) used.

### Design Principles Applied
- Figure-ground separation, muted base colours and vibrant data encoding.
- Sequential colour scale for rates (no diverging scale).
- Minimal empty space: projection and translate/scale tuned for Australia extent.
- Labels and legends positioned to avoid overlap and improve readability.

### Data Quality Assurance
- No missing jurisdictions; all 8 states/territories included.
- Original ABS values preserved; no derived metrics used for scoring.
- File sizes kept small to ensure fast load times.

## Expected Insights
- The visualization highlights regional differences in employment rates and the relative scale of labour forces by state, supporting regional labour market analysis and planning.

## Notes for Submission
- Ensure `index.html` embeds `js/week9_homework_map.json` (Vega-Lite) and the `data/labour_force_cleaned.csv` file is present.  
- After pushing, enable GitHub Pages in the repository settings (use main or gh-pages) and verify the published URL above.