# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:28:13 2024

@author: William Hackett
"""

import glob as gl
import pandas as pd

# path to list of top-level run folders in CSV file, where the top line should be Run_Path
run_list = pd.read_csv("# path to list of top-level run folders in CSV file, where the top line should be Run_Path.csv")

# create column for the sensor log file path from the run folder
run_list['sensor_log_path'] = run_list['Run_Path'] + '/Logs/Analysis/Metrics/*by_cycle_and_tile.csv'

# create a column with Run_ID (ex. OSQ008_21)
run_list['Run_ID'] = run_list['Run_Path'].str.extract(r'.*CC_([^CC]+)$')


compiled_run_list = []

for index, row in run_list.iterrows():
    # use glob to get the list of files that match the pattern
    matching_files = gl.glob(row['sensor_log_path'])

#    if matching_files:
    for log_file_path in matching_files:
        # read read af_log file
        run_data = pd.read_csv(log_file_path)
        # add a specific Run_ID to each row
        run_data['Run_ID'] = row['Run_ID']
        compiled_run_list.append(run_data)

compiled_run_list = pd.concat(compiled_run_list, ignore_index=False)

print(compiled_run_list)

#output csv folder
compiled_run_list.to_csv(‘OutputFileLocationHere.csv’)
