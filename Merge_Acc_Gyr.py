import pandas as pd
import glob



data_path = 'E:/GenderClassification/PycharmProjects/GenderClassification/home/abeer/Dropbox/Dataset_HAR project/*'

addrs = glob.glob(data_path)
for i in addrs:
    folders = glob.glob(i + '/Walk/Esphalt/Alone/*')
    for j in folders:
        csv_files = glob.glob(j + '/*')
        LUA = pd.read_csv('initAcc.csv')
        RC = pd.read_csv('initAcc.csv')
        LC = pd.read_csv('initAcc.csv')
        back = pd.read_csv('initAcc.csv')
        waist = pd.read_csv('initAcc.csv')
        RUA = pd.read_csv('initAcc.csv')
        LeftWatch = pd.read_csv('initAcc.csv')
        RightWatch = pd.read_csv('initAcc.csv')

        for k in csv_files:
            if '(1)' in k or '(2)' in k or '(3)' in k or '(4)' in k or '(5)' in k:
                continue
            elif 'Accelerometer' in k and 'F5-RC' in k:
                file = pd.read_csv(k)
                RC = RC.append(file.iloc[:, 3:])
                RC = RC.reset_index(drop=True)
                print(RC.columns)
            elif 'Accelerometer' in k and "DE-Waist" in k:
                file = pd.read_csv(k)
                waist = waist.append(file.iloc[:, 3:])
                waist = waist.reset_index(drop=True)
            elif 'Accelerometer' in k and "D5-LC" in k:
                file = pd.read_csv(k)
                LC = LC.append(file.iloc[:, 3:])
                LC = LC.reset_index(drop=True)
            elif 'Accelerometer' in k and "D2-RUA" in k:
                file = pd.read_csv(k)
                RUA = RUA.append(file.iloc[:, 3:])
                RUA = RUA.reset_index(drop=True)
            elif 'Accelerometer' in k and "C6-back" in k:
                file = pd.read_csv(k)
                back = back.append(file.iloc[:, 3:])
                back = back.reset_index(drop=True)
            elif 'Accelerometer' in k and "C5-LUA" in k:
                file = pd.read_csv(k)
                LUA = LUA.append(file.iloc[:, 3:])
                LUA = LUA.reset_index(drop=True)


        for k in csv_files:
            if '(1)' in k or '(2)' in k or '(3)' in k or '(4)' in k or '(5)' in k:
                continue
            elif 'Gyroscope' in k and 'F5-RC' in k:
                file = pd.read_csv(k)
                file = file.iloc[:, 3:]
                RC = pd.concat([RC, file], axis=1)
                print(RC.columns)
                print(RC.info())
            elif 'Gyroscope' in k and "DE-Waist" in k:
                file = pd.read_csv(k)
                file = file.iloc[:, 3:]
                waist = pd.concat([waist, file], axis=1)
            elif 'Gyroscope' in k and "D5-LC" in k:
                file = pd.read_csv(k)
                file = file.iloc[:, 3:]
                LC = pd.concat([LC, file], axis=1)
            elif 'Gyroscope' in k and "D2-RUA" in k:
                file = pd.read_csv(k)
                file = file.iloc[:, 3:]
                RUA = pd.concat([RUA, file], axis=1)
            elif 'Gyroscope' in k and "C6-back" in k:
                file = pd.read_csv(k)
                file = file.iloc[:, 3:]
                back = pd.concat([back, file], axis=1)
            elif 'Gyroscope' in k and "C5-LUA" in k:
                file = pd.read_csv(k)
                file = file.iloc[:, 3:]
                LUA = pd.concat([LUA, file], axis=1)

        ef = LUA.to_csv(j +'/C5-LUA.csv', index=None)
        ef = RUA.to_csv(j +'/D2-RUA.csv', index=None)
        ef = waist.to_csv(j +'/DE-Waist.csv', index=None)
        ef = back.to_csv(j +'/C6-back.csv', index=None)
        ef = LC.to_csv(j +'/D5-LC.csv', index=None)
        ef = RC.to_csv(j +'/F5-RC.csv', index=None)
