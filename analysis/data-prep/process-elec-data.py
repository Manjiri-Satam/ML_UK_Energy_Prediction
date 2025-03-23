import pandas as pd
import os
import glob
import pyarrow.parquet as pq
import pyarrow as pa

raw_csv_path = "/Volumes/T7/ml-power-data/raw/elec/csv/elec.csv"
tmp_folder = "/Volumes/T7/ml-power-data/raw/elec/csv/tmp/"
final_path = "/Volumes/T7/ml-power-data/elec.parquet"

if not os.path.exists(tmp_folder):
    os.makedirs(tmp_folder)

chunk_size = 1000000

months_abbrev_to_numeric = {
    'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4,
    'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,
    'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12
}

# Process the CSV into chunked Parquet files
for ii, chunk in enumerate(pd.read_csv(raw_csv_path, chunksize=chunk_size)):
    chunk.columns = ['ID', 'date', 'hh', 'kwh']
    # only want the date portion (time is in `hh`)
    chunk['day'] = pd.to_numeric(chunk['date'].str[:2])
    chunk['month_abbr'] = chunk['date'].str[2:5]
    chunk['month'] = chunk['month_abbr'].map(months_abbrev_to_numeric)
    chunk['year'] = pd.to_numeric(('20' + chunk['date'].str[5:7]))
    chunk['date'] = pd.to_datetime(chunk[['year', 'month', 'day']])
    #chunk.drop(['day', 'month', 'year'], axis=1, inplace = True)
    chunk.to_parquet(tmp_folder + 'chunk' + str(ii) + '.parquet', engine='pyarrow')
    print(f'Chunk {ii} saved')


parquet_files = glob.glob(tmp_folder + "*.parquet")

# Check that every chunk is fine
for file in parquet_files:
    try:
        table = pq.read_table(file)
        # to test for successes, uncomment line below.
        # print(f"File {file} read successfully.")
    except Exception as e:
        print(f"Failed to read file {file}: {e}")

tables = [pq.read_table(file) for file in parquet_files]
combined_table = pa.concat_tables(tables)
combined_table.order_by()
# write the combined table to a new Parquet file with compression
pq.write_table(combined_table, final_path, compression='snappy')