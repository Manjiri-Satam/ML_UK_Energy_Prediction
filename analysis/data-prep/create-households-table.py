import pandas as pd
import numpy as np
geography = pd.read_csv("../data/raw/geography.csv")
geography = (geography.loc[:, ['anonID', 'eProfileClass', 'fuelTypes', 'ACORN_Category',
                               'ACORN_Group', 'ACORN_Type', 'ACORN_Description', 'NUTS1', 'gspGroup', 'Elec_Tout']].
             rename(columns = {'anonID': 'id',
                               'eProfileClass': 'electricity_profile_class',
                               'fuelTypes': 'fuel_types',
                               'ACORN_Category': 'acorn_category',
                               'ACORN_Group': 'acorn_group',
                               'ACORN_Type': 'acorn_type',
                               'ACORN_Description': 'acorn_description',
                               'NUTS1': 'uk_administrative_geography',
                               'gspGroup': 'grid_supply_point',
                               'Elec_Tout': 'has_electricity_meter'}))
geography['id'] = geography['id'].astype(str)

print("Geography data read in and prepared")

households.to_sql(con = conn,
                  name = 'households',
                  if_exists = "replace",
                  index = False)

print("`households` table written into database")

households.to_csv("../data/households.csv")

print("`households` saved as CSV")

conn.close()