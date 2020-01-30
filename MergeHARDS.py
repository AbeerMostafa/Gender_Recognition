import pandas as pd
import csv
import glob

GenderDict = {'Abd Elrahman Hussein': 0, 'Abeer':1, 'Ahmed Nasr':0, 'Ahmed Hesham':0, 'Asmaa Assaf':1, 'Dina':1,
              'Farida':1, 'Arwa':1, 'Fayez':0, 'Islam Hisham':0, 'Karim':0, 'MennaAllah Rostom':1, 'Ola':1,
              'Osama':0, 'Ahmed Sharshar':0, 'Toqa':1, 'Yousef':0, 'Hesham Madkour':0, 'Hossam':0, 'MennaAllah abdelrahman':1,
              'Rania':1}

LUA = pd.read_csv('init.csv')
RC = pd.read_csv('init.csv')
LC = pd.read_csv('init.csv')
back = pd.read_csv('init.csv')
waist = pd.read_csv('init.csv')
RUA = pd.read_csv('init.csv')
LeftWatch = pd.read_csv('init.csv')
RightWatch = pd.read_csv('init.csv')

data_path = 'E:/GenderClassification/PycharmProjects/GenderClassification/home/abeer/Dropbox/Dataset_HAR project/*'

addrs = glob.glob(data_path)
for i in addrs:
    key = i.replace('E:/GenderClassification/PycharmProjects/GenderClassification/home/abeer/Dropbox/Dataset_HAR project', '')
    if GenderDict[key[1:]] == 0:
        label = 0
    else:
        label =1
    folders = glob.glob(i + '/Walk/Esphalt/Alone/*')
    for j in folders:
        csv_files = glob.glob(j + '/*')
        for k in csv_files:
            print(k)
            if  'C5-LUA.csv' in k:
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                LUA = LUA.append(file)
                LUA = LUA.reset_index(drop=True)
            elif  'C6-back.csv' in k:
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                back = back.append(file)
                back = back.reset_index(drop=True)

            elif  'D2-RUA.csv' in k:
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                RUA = RUA.append(file)
                RUA = RUA.reset_index(drop=True)

            elif  'D5-LC.csv' in k :
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                LC = LC.append(file)
                LC = LC.reset_index(drop=True)
            elif 'DE-Waist.csv' in k:
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                waist = waist.append(file)
                waist = waist.reset_index(drop=True)
            elif 'F5-RC.csv' in k:
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                RC = RC.append(file)
                RC = RC.reset_index(drop=True)
            elif 'right hand' in k or 'righthand' in k:
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                RightWatch = RightWatch.append(file)
                RightWatch = RightWatch.reset_index(drop=True)

            elif 'left hand' in k or 'lefthand' in k:
                file = pd.read_csv(k)
                file['label'] = None
                file['label'].fillna(label, inplace=True)
                LeftWatch = LeftWatch.append(file)
                LeftWatch = LeftWatch.reset_index(drop=True)


LUA = LUA.iloc[:, 2:]
RUA = RUA.iloc[:, 2:]
LC = LC.iloc[:, 2:]
back = back.iloc[:, 2:]
waist = waist.iloc[:, 2:]
RC = RC.iloc[:, 2:]
RightWatch = RightWatch.iloc[:, 2:]
LeftWatch = LeftWatch.iloc[:, 2:]


ef = LUA.to_csv('HAR_DataSet_LUA_Labeled.csv', index=None)
ef = RUA.to_csv('HAR_DataSet_RUA_Labeled.csv', index=None)
ef = waist.to_csv('HAR_DataSet_waist_Labeled.csv', index=None)
ef = back.to_csv('HAR_DataSet_back_Labeled.csv', index=None)
ef = LC.to_csv('HAR_DataSet_LC_Labeled.csv', index=None)
ef = RC.to_csv('HAR_DataSet_RC_Labeled.csv', index=None)
ef = RightWatch.to_csv('HAR_DataSet_RightWatch_Labeled.csv', index=None)
ef = LeftWatch.to_csv('HAR_DataSet_LeftWatch_Labeled.csv', index=None)

# def merge():
#     folder = 'LeftLegSensor/'
#     file1 = pd.read_csv(folder + "ola.csv")
#     file2 = pd.read_csv(folder + "Arwa.csv")
#     file3 = pd.read_csv(folder + "yousef.csv")
#     file4 = pd.read_csv(folder + "Islam.csv")
#     file5 = pd.read_csv(folder + "karim.csv")
#     file6 = pd.read_csv(folder + "Abdo.csv")
#     file7 = pd.read_csv(folder + "Abeer.csv")
#     file8 = pd.read_csv(folder + "toqa.csv")
#     file9 = pd.read_csv(folder + "menna.csv")
#     file10 = pd.read_csv(folder + "AhmedNasr.csv")
#
#     file11 = pd.read_csv(folder + "AhmedHesham.csv")
#     file12 = pd.read_csv(folder + "Sharshar.csv")
#     file13 = pd.read_csv(folder + "fayez.csv")
#     file14 = pd.read_csv(folder + "hossam.csv")
#     file15 = pd.read_csv(folder + "Osama.csv")
#     file16 = pd.read_csv(folder + "Rania.csv")
#     file17 = pd.read_csv(folder + "mennaAbdo.csv")
#     file18 = pd.read_csv(folder + "Farida.csv")
#     file19 = pd.read_csv(folder + "Dina.csv")
#     file20 = pd.read_csv(folder + "Asmaa.csv")
#
#     file1['label'] = None
#     file2['label'] = None
#     file3['label'] = None
#     file4['label'] = None
#     file5['label'] = None
#     file6['label'] = None
#     file7['label'] = None
#     file8['label'] = None
#     file9['label'] = None
#     file10['label'] = None
#
#     file11['label'] = None
#     file12['label'] = None
#     file13['label'] = None
#     file14['label'] = None
#     file15['label'] = None
#     file16['label'] = None
#     file17['label'] = None
#     file18['label'] = None
#     file19['label'] = None
#     file20['label'] = None
#
#
#
#     file1['label'].fillna(1, inplace=True)
#     file2['label'].fillna(1, inplace=True)
#     file7['label'].fillna(1, inplace=True)
#     file8['label'].fillna(1, inplace=True)
#     file9['label'].fillna(1, inplace=True)
#     file3['label'].fillna(0, inplace=True)
#     file4['label'].fillna(0, inplace=True)
#     file5['label'].fillna(0, inplace=True)
#     file6['label'].fillna(0, inplace=True)
#     file10['label'].fillna(0, inplace=True)
#
#     file11['label'].fillna(0, inplace=True)
#     file12['label'].fillna(0, inplace=True)
#     file13['label'].fillna(0, inplace=True)
#     file14['label'].fillna(0, inplace=True)
#     file15['label'].fillna(0, inplace=True)
#     file16['label'].fillna(1, inplace=True)
#     file17['label'].fillna(1, inplace=True)
#     file18['label'].fillna(1, inplace=True)
#     file19['label'].fillna(1, inplace=True)
#     file20['label'].fillna(1, inplace=True)
#
#     df = file2
#     df = df.append(file1)
#     df = df.append(file3)
#     df = df.append(file4)
#     df = df.append(file5)
#     df = df.append(file6)
#     df = df.append(file7)
#     df = df.append(file8)
#     df = df.append(file9)
#     df = df.append(file10)
#     df = df.append(file11)
#     df = df.append(file12)
#     df = df.append(file13)
#     df = df.append(file14)
#     df = df.append(file15)
#     df = df.append(file16)
#     df = df.append(file17)
#     df = df.append(file18)
#     df = df.append(file19)
#     df = df.append(file20)
#
#     df = df.reset_index(drop=True)
#     df = df.iloc[:, 2:]
#     df.info()
#     print(df['label'].value_counts())
#     ef = df.to_csv('/home/abeer/PycharmProjects/GenderClassification/HAR_DataSet_Labeled.csv', index=None)
# def merge_without_testFiles():
#     folder = 'LeftLegSensor/'
#
#     file2 = pd.read_csv(folder + "Arwa.csv")
#     file3 = pd.read_csv(folder + "yousef.csv")
#     file4 = pd.read_csv(folder + "Islam.csv")
#     file5 = pd.read_csv(folder + "karim.csv")
#     file6 = pd.read_csv(folder + "Abdo.csv")
#     file7 = pd.read_csv(folder + "Abeer.csv")
#     file8 = pd.read_csv(folder + "toqa.csv")
#     file9 = pd.read_csv(folder + "menna.csv")
#     file10 = pd.read_csv(folder + "AhmedNasr.csv")
#
#     file11 = pd.read_csv(folder + "AhmedHesham.csv")
#     file12 = pd.read_csv(folder + "Sharshar.csv")
#     file13 = pd.read_csv(folder + "fayez.csv")
#     file14 = pd.read_csv(folder + "hossam.csv")
#
#     file16 = pd.read_csv(folder + "Rania.csv")
#     file17 = pd.read_csv(folder + "mennaAbdo.csv")
#     file18 = pd.read_csv(folder + "Farida.csv")
#     file19 = pd.read_csv(folder + "Dina.csv")
#     file20 = pd.read_csv(folder + "Asmaa.csv")
#
#
#     file2['label'] = None
#     file3['label'] = None
#     file4['label'] = None
#     file5['label'] = None
#     file6['label'] = None
#     file7['label'] = None
#     file8['label'] = None
#     file9['label'] = None
#     file10['label'] = None
#
#     file11['label'] = None
#     file12['label'] = None
#     file13['label'] = None
#     file14['label'] = None
#
#     file16['label'] = None
#     file17['label'] = None
#     file18['label'] = None
#     file19['label'] = None
#     file20['label'] = None
#
#
#
#
#     file2['label'].fillna(1, inplace=True)
#     file7['label'].fillna(1, inplace=True)
#     file8['label'].fillna(1, inplace=True)
#     file9['label'].fillna(1, inplace=True)
#     file3['label'].fillna(0, inplace=True)
#     file4['label'].fillna(0, inplace=True)
#     file5['label'].fillna(0, inplace=True)
#     file6['label'].fillna(0, inplace=True)
#     file10['label'].fillna(0, inplace=True)
#
#     file11['label'].fillna(0, inplace=True)
#     file12['label'].fillna(0, inplace=True)
#     file13['label'].fillna(0, inplace=True)
#     file14['label'].fillna(0, inplace=True)
#
#     file16['label'].fillna(1, inplace=True)
#     file17['label'].fillna(1, inplace=True)
#     file18['label'].fillna(1, inplace=True)
#     file19['label'].fillna(1, inplace=True)
#     file20['label'].fillna(1, inplace=True)
#
#     df = file2
#
#     df = df.append(file3)
#     df = df.append(file4)
#     df = df.append(file5)
#     df = df.append(file6)
#     df = df.append(file7)
#     df = df.append(file8)
#     df = df.append(file9)
#     df = df.append(file10)
#     df = df.append(file11)
#     df = df.append(file12)
#     df = df.append(file13)
#     df = df.append(file14)
#
#     df = df.append(file16)
#     df = df.append(file17)
#     df = df.append(file18)
#     df = df.append(file19)
#     df = df.append(file20)
#
#     df = df.reset_index(drop=True)
#     df = df.iloc[:, 2:]
#     df.info()
#     print(df['label'].value_counts())
#     ef = df.to_csv('/home/abeer/PycharmProjects/GenderClassification/HAR_DataSet_without_TestFiles.csv', index=None)


# def prepare_test():
#
#     folder = 'LeftLegSensor/'
#     file1 = pd.read_csv(folder + "ola.csv")
#     file2 = pd.read_csv(folder + "Osama.csv")
#     file1['label'] = None
#     file2['label'] = None
#     file1['label'].fillna(1, inplace=True)
#     file2['label'].fillna(0, inplace=True)
#
#     df = file2
#     df = df.append(file1)
#
#     df = df.reset_index(drop=True)
#     df = df.iloc[:, 2:]
#     df.info()
#     print(df['label'].value_counts())
#     ef = df.to_csv('/home/abeer/PycharmProjects/GenderClassification/HAR_TestFile.csv', index=None)


# merge()
# merge_without_testFiles()
# prepare_test()