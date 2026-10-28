# Global Fuel Prices and Taxation Trends
## Tableau analytics project (synthetic demonstration)

**Status:** Starter project package prepared. The included dataset is synthetic and is not evidence of actual prices, tax rates, subsidies, or policy outcomes.

### Project purpose
Build a Tableau dashboard to explore how fuel prices, estimated tax shares, subsidy shares, regions, income groups, and years can be analyzed together. The package supports dashboard development and demonstration; it does not validate the real-world claims in the supplied project brief.

### What is included
- `data/synthetic_global_fuel_prices.csv` — generated demonstration dataset
- `data/data_dictionary.csv` — field definitions and caveats
- `data/dataset_profile.json` — basic structural checks
- `docs/tableau_build_guide.md` — step-by-step Tableau instructions
- `docs/analysis_plan.md` — questions, proposed KPIs, and interpretation caveats
- `docs/data_validation_checklist.md` — checklist for replacing synthetic data with sourced observations
- `tableau/workbook_status.md` — workbook status and instructions
- `requirements.txt` — Python requirements for optional regeneration/inspection
- `LICENSE` — MIT license for project text/code (not a license for any later third-party data)

### Dataset facts (verified from the generated file)
- 420 rows
- 20 illustrative country names
- Years 2020–2026 inclusive
- 3 fuel categories: Petrol, Diesel, LPG
- 6 broad regions
- Every row has `Data_Status = SYNTHETIC_DEMO`
- Expected row count = 20 countries × 7 years × 3 fuels = 420

These are structural facts about the generated sample only. They are not real-world findings. The user's brief mentioned 84 countries and 27,468 records; those figures have **not** been verified because no source dataset was provided.

### Quick start
1. Open Tableau Desktop or Tableau Public.
2. Connect to `data/synthetic_global_fuel_prices.csv`.
3. Confirm `Year` is numeric/date-compatible and the share fields are numeric decimals.
4. Follow `docs/tableau_build_guide.md`.
5. Publish only after adding a clear dashboard banner: **SYNTHETIC DEMO DATA — NOT FOR POLICY OR OPERATIONAL DECISIONS**.
6. For a review-ready public demo, publish your workbook to Tableau Public and add its URL to SkillWallet after publication.

### Suggested repository structure
```text
global-fuel-prices-taxation-trends/
├── data/
│   ├── synthetic_global_fuel_prices.csv
│   ├── data_dictionary.csv
│   └── dataset_profile.json
├── docs/
│   ├── analysis_plan.md
│   ├── data_validation_checklist.md
│   └── tableau_build_guide.md
├── tableau/
│   └── workbook_status.md
├── README.md
├── LICENSE
└── requirements.txt
```

### Important limitations
- No `.twb` or `.twbx` workbook is included: Tableau workbook files should be created and saved in Tableau Desktop/Public, then added to the repository.
- Prices and shares are randomly generated for practice, not sourced country statistics.
- Do not use the demo values for policy recommendations, economic claims, forecasting, or decisions.
