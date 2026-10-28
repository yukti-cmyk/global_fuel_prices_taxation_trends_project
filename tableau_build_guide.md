# Tableau Build Guide

## Goal
Create a dashboard named **Global Fuel Prices & Taxation Trends — Synthetic Demo**. Keep the synthetic-data disclosure visible on every dashboard/story point.

## 1. Connect the data
1. Launch Tableau Desktop or Tableau Public.
2. Choose **Connect → To a File → Text file**.
3. Select `data/synthetic_global_fuel_prices.csv`.
4. Check field types:
   - `Year`: Number (whole) or Date after creating a date field.
   - `Fuel_Price_USD_per_Litre`: Number (decimal).
   - `Estimated_Tax_Share`, `Estimated_Subsidy_Share`: Number (decimal).
   - Country, Region, Income_Group, Fuel_Type: Dimensions.
5. Retain `Data_Status` and `Source_Note` in the data source.

## 2. Create calculated fields
Create these fields (names and formulas are Tableau syntax):

**Tax Share %**
```text
[Estimated_Tax_Share] * 100
```

**Subsidy Share %**
```text
[Estimated_Subsidy_Share] * 100
```

**Year Date** (optional)
```text
MAKEDATE(INT([Year]), 1, 1)
```

**Fuel Price (3 decimal)**
Use `Fuel_Price_USD_per_Litre` directly and format to 3 decimals. It is illustrative USD/litre only.

## 3. Build worksheets
### A. KPI — Average Demo Fuel Price
- Text mark.
- Place `AVG(Fuel_Price_USD_per_Litre)` on Text.
- Title it **Average synthetic demo price (USD/L)**.
- Add a subtitle stating this is not observed data.

### B. Fuel price trend
- Columns: `Year`
- Rows: `AVG(Fuel_Price_USD_per_Litre)`
- Color: `Fuel_Type`
- Marks: Line
- Add filters for `Region`, `Country`, and `Income_Group`.
- Note: generated values are not a valid real-world trend.

### C. Country comparison
- Rows: `Country`
- Columns: `AVG(Fuel_Price_USD_per_Litre)`
- Color: `Fuel_Type`
- Sort descending.
- Use as a demonstration comparison only.

### D. Tax and subsidy scatterplot
- Columns: `AVG(Estimated_Tax_Share)`
- Rows: `AVG(Fuel_Price_USD_per_Litre)`
- Detail: `Country`
- Color: `Income_Group`
- Size: `AVG(Estimated_Subsidy_Share)`
- Add a tooltip with Country, Region, Year, Fuel_Type, price, tax share, subsidy share, and Data_Status.
- Caution: synthetic values cannot establish correlation or causation.

### E. Regional comparison
- Rows: `Region`
- Columns: `AVG(Fuel_Price_USD_per_Litre)`
- Color: `Fuel_Type`
- Use bars; label axes and indicate synthetic data.

### F. Country map (optional)
- Assign Tableau's geographic role to `Country` if recognized.
- Put Country on Detail and AVG(Fuel_Price_USD_per_Litre) on Color.
- If any country is not geocoded, use the country comparison bar chart instead. A map is optional and should not be required for the dashboard to work.

## 4. Assemble dashboard
Recommended size: 1200 × 800 (or Automatic for Tableau Public).
Layout:
1. Header and disclosure banner.
2. KPI tiles: average demo price, country count, year range, fuel types.
3. Trend chart (top-left), regional comparison (top-right).
4. Country comparison (bottom-left), tax/subsidy scatterplot (bottom-right).
5. Filters: Year, Region, Country, Fuel_Type, Income_Group.
6. Add filter actions so selecting a region/country filters the other sheets.
7. Add a footer: “Synthetic sample data generated for dashboard practice. Not suitable for policy, commercial, or academic conclusions.”

## 5. Suggested story points
1. What does the synthetic dataset contain?
2. How do the generated fuel categories compare?
3. How can price, tax-share, and subsidy-share fields be explored?
4. What data quality and source checks are needed before a real analysis?

## 6. Quality assurance
- Verify filters update all intended worksheets.
- Verify all charts show the synthetic-data warning.
- Confirm percent fields are displayed consistently.
- Confirm no worksheet title describes synthetic values as actual country prices.
- Check tooltip values and empty selections.
- Ensure no claims about affordability, tax burden, or policy performance are made from synthetic data.

## 7. Save and publish
1. Save the workbook as `tableau/global_fuel_prices_taxation_trends.twbx` in Tableau.
2. If saving a `.twb`, keep the CSV in the expected relative folder and test after moving the repository.
3. Publish to Tableau Public only if you are comfortable making the workbook and data public.
4. Add the published URL to SkillWallet's Demo Link field.
5. Add the GitHub repository URL to SkillWallet's GitHub Link field.

The `.twb/.twbx` workbook is a planned manual deliverable; this package does not claim it has been created or published.
