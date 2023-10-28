import glob
import pandas as pd

#define the pattern to search for .txt files
pattern = 'C:/Python/test_env/20231027_TS???????-BCC_AST?_??/AF_IMAGES/TS???????-BCC_af_log.xlsx'

#use glob to find the files matching the pattern
file_list = glob.glob(pattern)
CompiledAFLogs = None
dataframes = []

# Use enumerate() to keep track of the index
for index, file in enumerate(file_list):
    var_name = f"AFLog{index + 1}"
    df = pd.read_excel(file)  # Read the Excel file and store it in df
    df['AFLog'] = var_name  # Add the AFLog column
    dataframes.append(df) # Append the DataFrame to the list
#Concatenate all DataFrames in the list into a single Dataframe  
CompiledAFLogs = pd.concat(dataframes, ignore_index=True) 

CompiledAFLogs['AbsMoveMm'] = CompiledAFLogs[' MoveMm'].abs()
 
print(CompiledAFLogs)
    
CompiledAFLogs.to_excel('C:/Python/RunCompiler/AFLogs.xlsx')    
    
    
"""
Spyder Editor

This is a temporary script file.
"""

