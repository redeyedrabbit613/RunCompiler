# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:53:53 2024

@author: Kevin
"""

import glob as gl
import pandas as pd
run_id = []
file = 'Cluster Density Mast List.xlsx'
df = pd.read_excel(file)
run_id = df['SQ Run ID']

#use glob to find the files matching the pattern
file_list = gl.glob(pattern)
compiledruns = None 
dataframes = []

for file in file_list:
    run_id = 
    df = pd.read_excel(file)  # Read the Excel file and store it in df
    df['Run_ID'] = run_id #Create a new column labeled as Run_ID
    dataframes.append(df[['Flow_cell_ID'], ['Cluster Generator'], ['Lane'], ['Read'], ['Swath'], ['Tile'], ['Raw_SpotCount_PerMm2_AllSpots'], ['Run_ID']]) # Append dataframes with the columns of data from the df.
Compiledruns = pd.concat(dataframes, ignore_index=True)     

Compiledruns.to_excel('C:/Python/RunCompiler/CompiledRuns.xlsx')    

print('Runs successfully compiled.') 