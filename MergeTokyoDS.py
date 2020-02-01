import csv
import glob
import pandas as pd

dict = {}
with open('IDGenderAgelist.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dict[row[0]] = row[1]



data_path = 'AutomaticExtractionData_IMUZCenter/*.csv'
addrs = glob.glob(data_path)


df = pd.read_csv('AutomaticExtractionData_IMUZCenter/T0_ID004948_Center_seq0.csv', skiprows=2, names=['Gx','Gy','Gz', 'Ax','Ay','Az'])
df['label'] = None
df['label'].fillna(1, inplace=True)
df = df.iloc[0:500, :]
df.info()
print(df['label'].value_counts())

for key in dict.keys():
    l = len(str(key))
    keyStr = str(key).zfill(6-l)
    for addr in addrs:
        if keyStr in addr:
            file = pd.read_csv(addr, skiprows=2, names=['Gx','Gy','Gz', 'Ax','Ay','Az'])
            file['label'] = None
            file['label'].fillna(int(dict[key]), inplace=True)
            file = file.iloc[0:500, :]
            df = df.append(file)
            df = df.reset_index(drop=True)

df.info()
print(df['label'].value_counts())
ef = df.to_csv ('Tokyo_DataSet_FixedLength_Labeled.csv', index = None)