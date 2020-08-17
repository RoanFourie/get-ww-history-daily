'''
Python v3.8 or later
Windows 
For Sibanye Stillwater.
DESCRIPTION: Get daily maximum values around 5 AM between two dates.
OWNER: Roan Fourie
REVISION: 0
REVISION DATE: 2020-08-17 (Week 34)
REVISION AUTHOR: Roan Fourie
REVISION DESCRIPTION: 
        edit the list of tags and edit the dates and times where data must be parsed from.
        Return files with the day's maximum value.
USAGE:   
NOTES:
'''

import pyodbc 
import pandas as pd
import numpy as np

tags = ['KDCE_GP2_00INS01_00IQWT320.FA_PV0',
    'KDCE_GP2_00INS02_00IQWT320.FA_PV0',
    'KDCE_GP2_00INS03_00IQWT320.FA_PV0'
]

# Make a SQL connection
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=SGLX00SCHIS00GL;"
                      "Database=Runtime;"
                      "Trusted_Connection=yes;")


with cnxn:  # using the with statement will automatically close the connections
    cursor = cnxn.cursor()  

    for tag in tags:
        # Query results from SQL into a Pandas Data Frame
        df = pd.read_sql_query(f"SET QUOTED_IDENTIFIER OFF \
        SELECT * FROM OPENQUERY(INSQL, \"SELECT DateTime = convert(nvarchar, DateTime, 21),Time = convert(char(5), DateTime, 108), [{tag}] \
        FROM WideHistory \
        WHERE wwRetrievalMode = 'Cyclic' \
        AND wwResolution = 600000 \
        AND wwQualityRule = 'Extended' \
        AND wwVersion = 'Latest' \
        AND DateTime >= '20200501 05:00:00.000' \
        AND DateTime <= '20200814 05:00:00.000'\") \
        where Time >= '01:00' \
        AND Time <= '05:30'", cnxn)

        # Convert DateTime string to date time object type
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        # Get only the date without the time
        df['DT'] = df['DateTime'].dt.date   
        # Group the dates together A-Z then select the one with the largest value in the group
        # This will give the maximum for the day in a new data frame
        df1 = df.groupby(['DT'], sort=False)[tag].max()

        print(df1)

        df1.to_csv(f'c:\\scada\\{tag}-results.csv', sep=",", encoding='utf-8')

