"""Regenerate the synthetic demonstration dataset. Not real-world data."""
import random
import pandas as pd

random.seed(42)
countries = [
    ("India","Asia","Lower-middle income","INR",1.0,.18,.08),
    ("Japan","Asia","High income","JPY",1.0,.32,.02),
    ("Indonesia","Asia","Upper-middle income","IDR",.9,.12,.15),
    ("Thailand","Asia","Upper-middle income","THB",1.0,.25,.04),
    ("Germany","Europe","High income","EUR",1.3,.48,0.0),
    ("France","Europe","High income","EUR",1.3,.45,0.0),
    ("Spain","Europe","High income","EUR",1.2,.42,0.0),
    ("Poland","Europe","High income","PLN",1.1,.35,.02),
    ("United States","North America","High income","USD",1.0,.16,0.0),
    ("Canada","North America","High income","CAD",1.1,.22,0.0),
    ("Mexico","North America","Upper-middle income","MXN",.9,.20,.03),
    ("Brazil","South America","Upper-middle income","BRL",1.0,.28,.04),
    ("Chile","South America","High income","CLP",1.1,.24,0.0),
    ("Argentina","South America","Upper-middle income","ARS",.8,.15,.10),
    ("South Africa","Africa","Upper-middle income","ZAR",.9,.22,.04),
    ("Kenya","Africa","Lower-middle income","KES",.9,.20,.06),
    ("Nigeria","Africa","Lower-middle income","NGN",.7,.10,.20),
    ("Egypt","Africa","Lower-middle income","EGP",.8,.12,.12),
    ("Australia","Oceania","High income","AUD",1.1,.25,0.0),
    ("New Zealand","Oceania","High income","NZD",1.2,.30,0.0),
]
shocks = {2020:-.18,2021:-.05,2022:.24,2023:.14,2024:.12,2025:.10,2026:.11}
regions = {"Asia":.02,"Europe":.22,"North America":-.12,"South America":.04,"Africa":-.02,"Oceania":.08}
rows=[]
for country,region,income,currency,basep,tax_base,subsidy_base in countries:
    for year in range(2020,2027):
        for fuel,mult in [("Petrol",1.0),("Diesel",.92),("LPG",.52)]:
            price=round(max(.15,basep*mult*(1+shocks[year]+regions[region]+random.uniform(-.06,.06))),3)
            tax=round(min(.65,max(.05,tax_base+.01*(year-2020)+random.uniform(-.025,.025))),3)
            subsidy=round(min(.35,max(0,subsidy_base+random.uniform(-.025,.025))),3)
            rows.append({"Country":country,"Region":region,"Income_Group":income,"Year":year,
                         "Fuel_Type":fuel,"Fuel_Price_USD_per_Litre":price,"Estimated_Tax_Share":tax,
                         "Estimated_Subsidy_Share":subsidy,"Currency_Reference":currency,
                         "Data_Status":"SYNTHETIC_DEMO",
                         "Source_Note":"Illustrative generated value; not observed or verified country data"})
pd.DataFrame(rows).to_csv("data/synthetic_global_fuel_prices.csv",index=False)
print(f"Wrote {len(rows)} synthetic rows.")
