# Data Validation Checklist for Real-World Data

Use this before replacing the synthetic dataset.

- [ ] Record the original source and direct URL for every input table.
- [ ] Confirm permission/license and attribution requirements.
- [ ] Confirm the coverage period and exact countries included.
- [ ] Verify whether the fuel price is retail, wholesale, pre-tax, or another measure.
- [ ] Normalize units (e.g., USD per litre) and document exchange-rate source/date.
- [ ] Document whether prices are annual averages, monthly observations, or snapshots.
- [ ] Define tax share precisely and distinguish excise, VAT/sales tax, and other levies.
- [ ] Define subsidy precisely; distinguish explicit subsidies from price controls or transfers.
- [ ] Confirm income-group definitions and the classification year.
- [ ] Check duplicates at the intended country × date × fuel grain.
- [ ] Inspect missing values, outliers, and abrupt series breaks.
- [ ] Validate representative records against original source tables.
- [ ] Document interpolation, conversions, exclusions, and assumptions.
- [ ] Recompute row counts and distinct country/year/fuel counts.
- [ ] Remove or rename the `SYNTHETIC_DEMO` marker only when the source data has actually replaced the sample.
- [ ] Update the dashboard title, source notes, and limitations.
- [ ] Do not claim 84 countries or 27,468 records until independently verified against the actual source dataset.
