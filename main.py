import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import svm
from sklearn import metrics
# access file
data_source_csv = "./dataset/sleepdata.csv"
data1 = pd.read_csv(data_source_csv, sep=';')
data_source_csv = "./dataset/sleepdata_2.csv"
data2 = pd.read_csv(data_source_csv, sep=';')
#數值處理--------------------------------------------------------
for i in range(len(data1['Start'])):
        struct_time = time.strptime(data1["Start"][i], "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(struct_time))
        data1.loc[i, 'Start'] = time_stamp
for i in range(len(data1['End'])):
        struct_time = time.strptime(data1["End"][i], "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(struct_time))
        data1.loc[i, 'End'] = time_stamp
for i in range(len(data1['Time in bed'])):
        data1.loc[i, 'Time in bed'] = data1.loc[i, 'End'] - data1.loc[i, 'Start']
# 將睡眠品質的值轉成數值
for i in range(len(data1['Sleep quality'])):
    characters = "%"
    x = 0
    try:
        for x in range(len(characters)):
            data1.loc[i, 'Sleep quality'] = float(data1.loc[i, 'Sleep quality'].replace(characters[x],""))    
    except:
        print("error", i)
        break
# 決定留下的數值--------------------------------------------------------------------
df1 = data1.drop(['Wake up', 'Heart rate', 'Sleep Notes'], axis = 1)
#將資料做數值轉換，並建立一個新column儲存它們---------------------------------------------------------
for j in range(len(data1['Sleep Notes'])):
    list_Sleep_notes = ["Stressful day", 'Drank coffee', 'Drank tea', 'Ate late', 'Worked out'] #所有活動
    Sleep_notes = data1['Sleep Notes'][j]
    float_types = data1['Sleep Notes'][0] 
    note_status = [0,0,0,0,0]
    try:
        if (type(Sleep_notes) != type(float_types)):
            length = len(Sleep_notes.split(':'))
            if length >=2:
                for i in range(length):
                    if Sleep_notes.split(':')[i] == list_Sleep_notes[0]:
                        df1.loc[j, 'Stressful day'] = 1
                        note_status[0] = 1
                    elif Sleep_notes.split(':')[i] == list_Sleep_notes[1]:
                        df1.loc[j, 'Drank coffee'] = 1
                        note_status[1] = 1
                    elif Sleep_notes.split(':')[i] == list_Sleep_notes[2]:
                        df1.loc[j, 'Drank tea'] = 1
                        note_status[2] = 1
                    elif Sleep_notes.split(':')[i] == list_Sleep_notes[3]:
                        df1.loc[j, 'Ate late'] = 1
                        note_status[3] = 1
                    elif Sleep_notes.split(':')[i] == list_Sleep_notes[4]:
                        df1.loc[j, 'Worked out'] = 1
                        note_status[4] = 1
                for i in range(5):
                    if note_status[i] == 0:
                        df1.loc[j, list_Sleep_notes[i]] = 0
            else:
                i = 0
                for i in range(length):
                    if Sleep_notes.split(':')[i] == list_Sleep_notes[0]:
                        df1.loc[j, 'Stressful day'] = 1
                        df1.loc[j, 'Drank coffee'] = 0
                        df1.loc[j, 'Drank tea'] = 0
                        df1.loc[j, 'Ate late'] = 0
                        df1.loc[j, 'Worked out'] = 0
                    elif Sleep_notes.split(':')[i] == list_Sleep_notes[1]:
                        df1.loc[j, 'Stressful day'] = 0
                        df1.loc[j, 'Drank coffee'] = 1
                        df1.loc[j, 'Drank tea'] = 0
                        df1.loc[j, 'Ate late'] = 0
                        df1.loc[j, 'Worked out'] = 0
                    elif Sleep_notes.split(':')[i] == list_Sleep_notes[2]:
                        df1.loc[j, 'Stressful day'] = 0
                        df1.loc[j, 'Drank coffee'] = 0
                        df1.loc[j, 'Drank tea'] = 1
                        df1.loc[j, 'Ate late'] = 0
                        df1.loc[j, 'Worked out'] = 0
                    elif Sleep_notes.split(':')[i] == list_Sleep_notes[3]:
                        df1.loc[j, 'Stressful day'] = 0
                        df1.loc[j, 'Drank coffee'] = 0
                        df1.loc[j, 'Drank tea'] = 0
                        df1.loc[j, 'Ate late'] = 1
                        df1.loc[j, 'Worked out'] = 0
                    elif Sleep_notes.split(':')[i] == list_Sleep_notes[4]:
                        df1.loc[j, 'Stressful day'] = 0
                        df1.loc[j, 'Drank coffee'] = 0
                        df1.loc[j, 'Drank tea'] = 0
                        df1.loc[j, 'Ate late'] = 0
                        df1.loc[j, 'Worked out'] = 1
        else:
            df1.loc[j, 'Stressful day'] = 0
            df1.loc[j, 'Drank coffee'] = 0
            df1.loc[j, 'Drank tea'] = 0
            df1.loc[j, 'Ate late'] = 0
            df1.loc[j, 'Worked out'] = 0
    except:
        print("error", j)
#開始對資料做分配-----------------------------------------------------------------------------
df1_target = df1['Sleep quality']
df1_last = df1.drop('Sleep quality', axis=1)
data1_train,data1_test,target1_train,target1_test = train_test_split(df1_last,df1_target, test_size=0.4,random_state=47)
# 特徵縮放---------------------------------------------------------------------------------------
#scaler_time_bed = preprocessing.StandardScaler().fit(df1['Time in bed'].values[:].reshape(-1,1))
#scaler_time_bed.transform(df1['Drank coffee'].values[:].reshape(-1,1))
scaler = preprocessing.StandardScaler().fit(data1_train.values[:])
std_data1_train = scaler.transform(data1_train.values[:])
std_data1_test = scaler.transform(data1_test.values[:])

scaler_target = preprocessing.StandardScaler().fit(target1_train.values[:].reshape(-1,1))
std_target1_train = scaler_target.transform(target1_train.values[:].reshape(-1,1))
std_target1_test = scaler_target.transform(target1_test.values[:].reshape(-1,1))

# 訓練模型----------------------------------------------------------------------------------------
linearModel = svm.SVR(C=100, kernel = 'rbf', gamma = 'auto')
linearModel.fit(std_data1_train, target1_train.values[:])
predicted = linearModel.predict(std_data1_test)
print('R2 score: ', linearModel.score(std_data1_train, target1_train.values[:]))
print('MSE: ', metrics.mean_squared_error(target1_test.values[:], predicted))
linearModel.fit(std_data1_train, std_target1_train.ravel())
predicted = linearModel.predict(std_data1_test)
print('this is standafter...')
print('R2 score: ', linearModel.score(std_data1_train, std_target1_train))
print('MSE: ', metrics.mean_squared_error(std_target1_test, predicted))