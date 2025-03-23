import pandas as pd

raw_path = "/Volumes/T7/ml-power-data/raw/elec/csv/edrp_elec.csv"
filtered_path = "/Volumes/T7/ml-power-data/raw/elec/csv/6pm.csv"

months_abbrev_to_numeric = {
    'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4,
    'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8,
    'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12
}

chunk_size = 100000

chunks = []

for ii, chunk in enumerate(pd.read_csv(raw_path, chunksize = chunk_size)):
    chunk.columns = ['ID', 'date', 'hh', 'kwh']
    chunk = chunk[chunk['hh'] == 36]
    # only want the date portion (time is in `hh`)
    chunk['day'] = pd.to_numeric(chunk['date'].str[:2])
    chunk['month_abbr'] = chunk['date'].str[2:5]
    chunk['month'] = chunk['month_abbr'].map(months_abbrev_to_numeric)
    chunk['year'] = pd.to_numeric(('20' + chunk['date'].str[5:7]))
    chunk['date'] = pd.to_datetime(chunk[['year', 'month', 'day']])
    chunks.append(chunk)
    print(f'Chunk {ii} saved')

df = pd.concat(chunks)

df.to_csv(filtered_path, index = False)