import pandas as pd
from dateutil.relativedelta import relativedelta

# system-specific (change locally but do not push!)
raw_path = '/Volumes/T7/ml-power-data/raw/elec/csv/6pm.csv'
geography_path = '~/git/ml-power/data/raw/geography.csv'
output_path = '~/git/ml-power/data/df.csv'

raw = pd.read_csv(raw_path)

print('6pm file read in')

monthly_average = raw.groupby(['ID', 'year', 'month'])['kwh'].mean().reset_index()

print('Monthly averages calculated')

daily = raw.pivot_table(
    index=['ID', 'year', 'month', 'month_abbr'],  # what identifies unique rows
    columns='day',
    values='kwh',
    aggfunc='sum' # no aggregation performed (sum of scalar X is X)
).reset_index()


# find previous month and year
daily['date_for_merging'] = pd.to_datetime((daily['year'].astype(str) + '-' + daily['month'].astype(str) + '-1'))
daily['date_for_merging'] = daily['date_for_merging'].apply(lambda x: x - relativedelta(months=1))
daily['year'] = daily['date_for_merging'].dt.year
daily['month'] = daily['date_for_merging'].dt.month
del daily['date_for_merging']

# reverse columns (make 1->31, 2->30 etc) so that the number is days since beginning of current month
daily.columns = ['ID', 'year', 'month', 'month_abbr'] + ['kwh' + str(day) for day in daily.columns[4:][::-1].to_list()]

# drop 31, 30, and 29 (because Feb only has 28 days) -> will have previous 4 weeks
daily.drop(columns = ['kwh31', 'kwh30', 'kwh29'], inplace = True)

# make the closest days first
fixed_columns = daily.iloc[:, :-28]
days = daily.iloc[:, -28:]
days = days.iloc[:, ::-1]
daily = pd.concat([fixed_columns, days], axis=1)
del fixed_columns
del days

print('Previous 28 days of use calculated')

df = pd.merge(monthly_average, daily, 'left', on = ['ID', 'year', 'month'])

del monthly_average
del daily

# only want months where we have 28 days of previous use
# for example, exclude the month after the data starts (unless it starts in the first few days)
df.dropna(inplace = True)

df['ID'] = df['ID'].astype(str)


geography = pd.read_csv(geography_path)
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
geography['ID'] = geography['id'].astype(str)
del geography['id']


df = pd.merge(df, geography, 'left', on = 'ID')

print('Saving file')

df.to_csv(output_path)