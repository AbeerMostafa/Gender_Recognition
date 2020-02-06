import pandas as pd
import glob



data_path = 'E:/GenderClassification/PycharmProjects/GenderClassification/home/abeer/Dropbox/Dataset_HAR project/Brushing Teeth/*'

addrs = glob.glob(data_path)
for i in addrs:
    folders = glob.glob(i + '/*')
    for j in folders:
        csv_files = glob.glob(j + '/*')
        shoulder = pd.read_csv('initAcc.csv')
        elbow = pd.read_csv('initAcc.csv')
        watch = pd.read_csv('initAcc.csv')


        for k in csv_files:
            if '(1)' in k or '(2)' in k or '(3)' in k or '(4)' in k or '(5)' in k:
                continue
            elif 'Accelerometer' in k and 'Shoulder' in k:
                file = pd.read_csv(k)
                shoulder = shoulder.append(file.iloc[:, 3:])
                shoulder = shoulder.reset_index(drop=True)
                print(shoulder.columns)
            elif 'Accelerometer' in k and "Elbow" in k:
                file = pd.read_csv(k)
                elbow = elbow.append(file.iloc[:, 3:])
                elbow = elbow.reset_index(drop=True)
            elif 'D5' not in k and "F5" not in k:
                file = pd.read_csv(k)
                watch = watch.append(file.iloc[:, 3:])
                watch = watch.reset_index(drop=True)


        for k in csv_files:
            if '(1)' in k or '(2)' in k or '(3)' in k or '(4)' in k or '(5)' in k:
                continue
            elif 'Gyroscope' in k and 'Shoulder' in k:
                file = pd.read_csv(k)
                file = file.iloc[:, 3:]
                shoulder = pd.concat([shoulder, file], axis=1)
                print(shoulder.columns)
                print(shoulder.info())
            elif 'Gyroscope' in k and "Elbow" in k:
                file = pd.read_csv(k)
                file = file.iloc[:, 3:]
                elbow = pd.concat([elbow, file], axis=1)


        ef = shoulder.to_csv(j +'/Shoulder.csv', index=None)
        ef = elbow.to_csv(j +'/Elbow.csv', index=None)
        ef = watch.to_csv(j +'/Watch.csv', index=None)

