# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:29:51 2023

@author: Kevin
"""

import pandas as pd

excel = {"Test":("Color", "Spot Count", "Gain", "LED Power", "FAT"),
         "Results":("Red", 20, 50, "High", "Pass")}
data = pd.DataFrame(excel)
data.columns = ['Test Name', 'Final Results']
print(data)

new_excel = {"Color": data.iloc[0,1], "Spot Count": data.iloc[1,1],"Gain": data.iloc[2,1],"LED Power": data.iloc[3,1],"FAT": data.iloc[4,1]}
columns = ["Color", "Spot Count", "Gain", "LED Power", "FAT"] 
new_data = pd.DataFrame([new_excel], columns = columns)
print(new_data)