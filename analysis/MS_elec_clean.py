# this code is used to make elec_clean_2 table in the database
# split it as date, month and time
#error- year and day columns interchanged which is fixed later

import sqlite3
import pandas as pd

# Establish the database connection
conn = sqlite3.connect("C:/Manjiri Satam_created/Hertie_study/Spring 2024/Machine Learning/Project/ml-power-data- from Jackson/data/ml-power.db")

# Create a cursor object using the cursor() method
cursor = conn.cursor()

clean_code = """
CREATE TABLE elec_clean_2 AS 
SELECT
    -- ANON_ID as id,
    ANON_ID as id,
    substr(ADVANCEDATETIME, 1, 2) as year, 
    substr(ADVANCEDATETIME, 3, 3) as month,
    substr(ADVANCEDATETIME, 6, 2) as day,
    HH as time,
    ELECKWH as kwh
FROM elec;
"""

# Copy 'elec' to 'elec_clean'
#conn.execute("CREATE TABLE elec_clean AS SELECT * FROM elec;")
cursor.execute(clean_code)
conn.commit()

# SQL command to delete the row where 'ANON_ID' column has the value 'ANON_ID'
# from 'elec_clean'
conn.execute("DELETE FROM elec_clean_2 WHERE id = 'ANON_ID';")
conn.commit()

#column names of rows and columns have been interchanged
cursor.execute("ALTER TABLE elec_clean_2 RENAME COLUMN year TO date;")
cursor.execute("ALTER TABLE elec_clean_2 RENAME COLUMN day TO year;")

# Close the database connection
conn.close()
