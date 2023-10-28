# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:01:49 2023

@author: whackett
"""

# Compile Z-Stage Moves

import pandas as pd
 
AFLog1 = pd.read_csv('//sd/rddata/OnsoData/20231020_FC1004390-BCC_OS20016_7/AF_IMAGES/FC1004390-BCC_af_log.csv')
AFLog2 = pd.read_csv("//sd/rddata/OnsoData/20231021_FC1005701-BCC_OSQ010_16/AF_IMAGES/FC1005701-BCC_af_log.csv")
AFLog3 = pd.read_csv("//sd/rddata/OnsoData/20231020_FX0038186-ACC_OSQ009_22/AF_IMAGES/FX0038186-ACC_af_log.csv")

AFLog1 = pd.DataFrame(AFLog1)
AFLog2 = pd.DataFrame(AFLog2)
AFLog3 = pd.DataFrame(AFLog3)

AFLog1['AFLog'] = 'AFLog1'
AFLog2['AFLog'] = 'AFLog2'
AFLog3['AFLog'] = 'AFLog3'

CompiledAFLogs = pd.concat([AFLog1, AFLog2, AFLog3])

CompiledAFLogs['AbsMoveMm'] = CompiledAFLogs[' MoveMm'].abs()

print(CompiledAFLogs)

CompiledAFLogs.to_csv('C:\Users\jowang\OneDrive - Pacific Biosciences of California\Desktop\Python\RunComplier\AFLogs.csv')
