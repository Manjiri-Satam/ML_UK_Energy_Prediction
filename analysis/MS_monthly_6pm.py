# usimg elec_clean_2 table where I have already split the datetime column - MS_elec_clean.py
# in this file I am taking time as 6pm
# kwh avg per HH per month per year
# merge the geo file
# export this to csv

import sqlite3
import pandas as pd

# Establish the database connection
conn = sqlite3.connect("C:/Manjiri Satam_created/Hertie_study/Spring 2024/Machine Learning/Project/ml-power-data- from Jackson/data/ml-power.db")

# Create a cursor object using the cursor() method
cursor = conn.cursor()

monthly_6pm_usage = """
CREATE TABLE monthly_6pm AS 
SELECT 
    id,
    month,
    year,
    time,
    AVG(kwh) as mean_kwh
FROM elec_clean_2
WHERE time = 36
GROUP BY id, month, year;
"""

cursor.execute(monthly_6pm_usage)
conn.commit()

#merge the HH dataset with this
merged_monthly_6pm_geography = """
    CREATE TABLE merged_monthly_6pm_geo AS
    SELECT monthly_6pm.*, households.*
    FROM monthly_6pm
    JOIN households ON monthly_6pm.id = households.id
"""

cursor.execute(merged_monthly_6pm_geography)
conn.commit()

# Fetch data from avg_6pm_per_hh table
query_avg_6pm_per_hh = "SELECT * FROM monthly_6pm"
df_avg_monthly_6pm_per_hh = pd.read_sql_query(query_avg_6pm_per_hh, conn)

# Save avg_6pm_per_hh DataFrame as CSV
df_avg_monthly_6pm_per_hh.to_csv("C:/Manjiri Satam_created/Hertie_study/Spring 2024/Machine Learning/Project/ml-power-data- from Jackson/ml-power/src/monthly_6pm.csv", index=False)

# Fetch data from merged_6pm_geo table
query_merged_6pm_geo = "SELECT * FROM merged_monthly_6pm_geo"
df_merged_monthly_6pm_geo = pd.read_sql_query(query_merged_6pm_geo, conn)

# Save merged_6pm_geo DataFrame as CSV
df_merged_monthly_6pm_geo.to_csv("C:/Manjiri Satam_created/Hertie_study/Spring 2024/Machine Learning/Project/ml-power-data- from Jackson/ml-power/src/merged_monthly_6pm_geo.csv", index=False)