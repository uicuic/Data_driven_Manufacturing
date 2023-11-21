#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 21:43:54 2023

@author: uichan
"""
import pandas as pd

#read data
df = pd.read_csv('heat-treatment_dataset (raw data).csv', encoding="cp949")
df_sample = pd.read_csv('heat-treatment_dataset (sample data).csv', encoding="cp949")
df.columns
df_sample.columns
df['Unnamed: 0'].value_counts()

#remove 'Unnamed: 0'
import seaborn as sns
sns.lineplot(data=df['Unnamed: 0'])
df = df.drop('Unnamed: 0', axis=1)
df.head()


#rename columns
df.columns
# 'CP(제어) OP', '건조 1존 OP', '건조 2존 OP', '건조로 온도 1 Zone', '건조로 온도 2 Zone',
#        '세정기', '소입1존 OP', '소입2존 OP', '소입3존 OP', '소입4존 OP', '소입로 CP 값',
#        '소입로 CP 모니터 값', '소입로 온도 1 Zone', '소입로 온도 2 Zone', '소입로 온도 3 Zone',
#        '소입로 온도 4 Zone', '솔트 1존 OP', '솔트 2존 OP', '솔트 CONV 1존', '솔트 CONV 2존',
#        '솔트 슬러지 제거', '솔트 컨베이어 온도 1 Zone', '솔트 컨베이어 온도 2 Zone', '솔트조 온도 1 Zone',
#        '솔트조 온도 2 Zone'
df.columns = ['CP_control_OP', 'Drying_OP_1', 'Drying_OP_2', 'Drying_Temp_1','Drying_Temp_2', 'Washing_Machine', 'Quenching_OP_1', 'Quenching_OP_2', 'Quenching_OP_3', 'Quenching_OP_4',
'Quenching_CP', 'Quenching_CP_Monitor', 'Quenching_Temp_1', 'Quenching_Temp_2',
'Quenching_Temp_3', 'Quenching_Temp_4', 'Salt_OP_1', 'Salt_OP_2','Salt_CONV_1', 'Salt_CONV_2', 'Salt_Sludge_Removal',
'Salt_Conveyor_Temp_1', 'Salt_Conveyor_Temp_2', 'Salt_Bath_Temp_1',
'Salt_Bath_Temp_2']
df.columns

#

