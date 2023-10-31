# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:43:19 2023

@author: John Wang
"""
#'glob' is a module used for searching and manipulating files and directories based on wildcard patterns.
import glob as g
import pandas as pd

#Define the pattern to search for .txt files
pattern = 'S:/sd.nanofluidics.com/rddata/OnsoData/202310??_?????????-?CC_OSQ?_??/AF_IMAGES/?????????-?CC_af_log.csv'

#Use glob to find the files matching the pattern
file_list = g.glob(pattern)
CompiledAFLogs = None
dataframes = []

#Use enumerate() to keep track of the index
for index, file in enumerate(file_list):
    file_num = f"AFLog{index + 1}"
    df = pd.read_csv(file)  # Read the csv file and store it in df
    df['AFLog'] = file_num  # Add the AFLog coloumn
    dataframes.append(df) # Append the DataFrame to the list
#Concatenate all DataFrames in the list into a single Dataframe  
CompiledAFLogs = pd.concat(dataframes, ignore_index=True) 
#Turns all values in a specific coloumn into an absolute value and reassigns them to a new coloumn.
CompiledAFLogs['AbsMoveMm'] = CompiledAFLogs[' MoveMm'].abs()
#Writes CompiledAFLogs data frames' to a csv file in the designated path. 
CompiledAFLogs.to_csv('#Desired filepath') 