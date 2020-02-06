import pandas as pd
import csv
import glob

GenderDict = {'Abd Elrahman Hussein': 0, 'Abeer':1, 'Ahmed Nasr':0, 'Ahmed Hesham':0, 'Asmaa':1, 'Dina':1,
              'Farida':1, 'Arwa':1, 'Fayez':0, 'Islam Hisham':0, 'Karim':0, 'MennaAllah Rostom':1, 'Ola':1,
              'Osama':0, 'sharshar':0, 'Toqa':1, 'youssef':0, 'Hesham Madkour':0, 'Hossam':0, 'MennaAllah abdelrahman':1,
              'Rania':1}

shoulder = pd.read_csv('init.csv')
elbow = pd.read_csv('init.csv')
RightWatch = pd.read_csv('init.csv')


data_path = 'E:/GenderClassification/PycharmProjects/GenderClassification/home/abeer/Dropbox/Dataset_HAR project/Brushing Teeth/*'

addrs = glob.glob(data_path)
for i in addrs:
    key = i.replace('E:/GenderClassification/PycharmProjects/GenderClassification/home/abeer/Dropbox/Dataset_HAR project/Brushing Teeth', '')
    if GenderDict[key[1:]] == 0:
        label = 0
    else:
        label =1
    print("The label of ", key[1:], " is ", label)
    folders = glob.glob(i + '/*')
    for j in folders:
        csv_files = glob.glob(j + '/*')
        for k in csv_files:
            print(k)
            if '(1)' in k or '(2)' in k or '(3)' in k or '(4)' in k or '(5)' in k:
                continue

            elif  'Shoulder.csv' in k :
                file = None
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                shoulder = shoulder.append(file)
                shoulder = shoulder.reset_index(drop=True)
            elif 'Elbow.csv' in k:
                file = None
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                elbow = elbow.append(file)
                elbow = elbow.reset_index(drop=True)
            elif 'Watch.csv' in k:
                file = None
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                RightWatch = RightWatch.append(file)
                RightWatch = RightWatch.reset_index(drop=True)



RightWatch = RightWatch.iloc[:, 4:]

folder = 'BrushingTeeth/'
ef = shoulder.to_csv(folder + 'BT_DataSet_Shoulder_Labeled.csv', index=None)
ef = elbow.to_csv(folder + 'BT_DataSet_Elbow_Labeled.csv', index=None)
ef = RightWatch.to_csv(folder + 'BT_DataSet_Watch_Labeled.csv', index=None)

