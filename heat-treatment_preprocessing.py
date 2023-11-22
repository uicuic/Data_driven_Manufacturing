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

# data information
df.info()
des = df.describe()

# Check missing values
 # 1. Using IQR and change Lower, Upper limit
from ft_col import outlier_test

df.plot(kind = 'box')
outlire_result_box = df.apply(outlier_test)
outlire_result_box.sum(axis=1)
(outlire_result_box.sum(axis = 1)<2).sum() #1.5
#bc_drop_id[outlier_result.sum(axis = 1)<2]

outlire_result_box.sum().sum()

df['Drying_Temp_1'].plot(kind = 'box')


# corr(feature selection)EDA(Exploratory Data Analysis) 
corr = df.corr()
corr['CP_control_OP']
corr[abs(corr) > 0.5]
df.corr()['Quenching_Temp_3']['Quenching_CP_Monitor']
df_diff = df[['Quenching_Temp_3','Quenching_CP_Monitor']]
df_diff.describe()
corr[['Quenching_Temp_3','Quenching_CP_Monitor']]


df.head()

df_s = df_sample.head(10000)
df_r_s = df.head(10000)


import matplotlib.pyplot as plt

plt.plot(df_r_s.index, df_r_s['Quenching_OP_1'])

# relation of cp_op and q_cp
import seaborn as sns
plot = df[['CP_control_OP','Quenching_CP']]
# Scatter plot - pairplot()
sns.pairplot()

    # remove Salt_Sludge_Removal
corr['Salt_Sludge_Removal']

# make cp to dependent variable
df[df['Quenching_CP'] < 0.2]




# unsupervised learning and check relation with 'Quenching_CP'

df_cluster = df.drop(columns = ['Salt_Sludge_Removal'])

from sklearn.cluster import KMeans
k_means=KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300, n_clusters=2, n_init=10, random_state=None, tol=0.0001, verbose=0)
k_means.fit(df_cluster)
predict_cluster=k_means.predict(df_cluster)
cluster_label = pd.Series(predict_cluster)
df_cluster['label'] = cluster_label

df_cluster.columns
df_cluster.label.value_counts()

# groupby with label
group_cluseter = df_cluster.groupby('label')
group_mean = group_cluseter.mean()
df_cluster.head(100000)



# IsolationForest for search outlire

from sklearn.ensemble import IsolationForest
clf = IsolationForest(max_features = 25, contamination=0.01)  # contamination 파라미터는 이상치의 비율을 설정합니다.
clf.fit(df_cluster)
outliers = clf.predict(df_cluster) 
outliers_series = pd.Series(predict_cluster)
outliers_series.value_counts()

