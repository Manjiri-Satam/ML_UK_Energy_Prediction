import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

elec_path = "~/git/ml-power/data/elec.parquet"

elec = pq.ParquetFile(elec_path)

# Initialize an empty dictionary to store min and max dates for each ID
dates = {}

# Process each row group
for i in range(elec.num_row_groups):
    try:
        table = elec.read_row_group(i, columns=['date', 'ID'])
    except Exception as e:
        print(f'Error reading group {i}:', e)

    df = table.to_pandas()

    grouped = df.groupby('ID')['date'].agg(['min', 'max'])

    # overwrite previous min/max for that ID if this one is lesser/greater
    for IDx, row in grouped.iterrows():
        if IDx in dates:
            dates[IDx]['min'] = min(dates[IDx]['min'], row['min'])
            dates[IDx]['max'] = max(dates[IDx]['max'], row['max'])
        else:
            dates[IDx] = {'min': row['min'], 'max': row['max']}


# turn back into a Pandas DF to save as CSV
IDs = list(dates.keys())
min_dates = [dates[ID]['min'] for ID in IDs]
max_dates = [dates[ID]['max'] for ID in IDs]

result_table = pd.DataFrame({
    'ID': IDs,
    'first_date': min_dates,
    'last_date': max_dates
})

result_table.to_csv("~/git/ml-power/data/first-and-last-date-by-id.csv")