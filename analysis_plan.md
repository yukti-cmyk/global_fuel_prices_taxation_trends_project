# Analysis Plan

## Objective
Demonstrate a Tableau workflow for comparing fuel categories, time periods, regions, illustrative income groups, and synthetic tax/subsidy fields.

## Questions the dashboard can demonstrate
- How do generated prices vary by fuel category?
- How do generated values compare across the sample's regions and country labels?
- What patterns appear when generated tax and subsidy shares are plotted against generated prices?
- Which fields, source notes, and validation checks would be required for a real-world study?

## Proposed dashboard metrics
- Average synthetic price by fuel type, country, region, and year
- Number of countries represented in the sample
- Count of years and fuel categories
- Average illustrative tax share and subsidy share

## Interpretation limits
The records are synthetic and designed for learning dashboard mechanics. Any visible patterns are artifacts of the generation process. They cannot support claims about real fuel prices, taxation, subsidies, economic development, affordability, volatility, forecasting, or causality. Do not label a synthetic pattern as a finding about a country.

## Replacing with real data
Before making real-world claims, obtain licensed, source-documented country-year-fuel observations. Record original source URL, publication/access date, unit, currency, tax definition, subsidy definition, conversion method, and missing-data handling. See `data_validation_checklist.md`.
