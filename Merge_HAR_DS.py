import pandas as pd
def merge():
    folder = 'LeftLegSensor/'
    file1 = pd.read_csv(folder + "ola.csv")
    file2 = pd.read_csv(folder + "Arwa.csv")
    file3 = pd.read_csv(folder + "yousef.csv")
    file4 = pd.read_csv(folder + "Islam.csv")
    file5 = pd.read_csv(folder + "karim.csv")
    file6 = pd.read_csv(folder + "Abdo.csv")
    file7 = pd.read_csv(folder + "Abeer.csv")
    file8 = pd.read_csv(folder + "toqa.csv")
    file9 = pd.read_csv(folder + "menna.csv")
    file10 = pd.read_csv(folder + "AhmedNasr.csv")

    file11 = pd.read_csv(folder + "AhmedHesham.csv")
    file12 = pd.read_csv(folder + "Sharshar.csv")
    file13 = pd.read_csv(folder + "fayez.csv")
    file14 = pd.read_csv(folder + "hossam.csv")
    file15 = pd.read_csv(folder + "Osama.csv")
    file16 = pd.read_csv(folder + "Rania.csv")
    file17 = pd.read_csv(folder + "mennaAbdo.csv")
    file18 = pd.read_csv(folder + "Farida.csv")
    file19 = pd.read_csv(folder + "Dina.csv")
    file20 = pd.read_csv(folder + "Asmaa.csv")

    file1['label'] = None
    file2['label'] = None
    file3['label'] = None
    file4['label'] = None
    file5['label'] = None
    file6['label'] = None
    file7['label'] = None
    file8['label'] = None
    file9['label'] = None
    file10['label'] = None

    file11['label'] = None
    file12['label'] = None
    file13['label'] = None
    file14['label'] = None
    file15['label'] = None
    file16['label'] = None
    file17['label'] = None
    file18['label'] = None
    file19['label'] = None
    file20['label'] = None



    file1['label'].fillna(1, inplace=True)
    file2['label'].fillna(1, inplace=True)
    file7['label'].fillna(1, inplace=True)
    file8['label'].fillna(1, inplace=True)
    file9['label'].fillna(1, inplace=True)
    file3['label'].fillna(0, inplace=True)
    file4['label'].fillna(0, inplace=True)
    file5['label'].fillna(0, inplace=True)
    file6['label'].fillna(0, inplace=True)
    file10['label'].fillna(0, inplace=True)

    file11['label'].fillna(0, inplace=True)
    file12['label'].fillna(0, inplace=True)
    file13['label'].fillna(0, inplace=True)
    file14['label'].fillna(0, inplace=True)
    file15['label'].fillna(0, inplace=True)
    file16['label'].fillna(1, inplace=True)
    file17['label'].fillna(1, inplace=True)
    file18['label'].fillna(1, inplace=True)
    file19['label'].fillna(1, inplace=True)
    file20['label'].fillna(1, inplace=True)

    df = file2
    df = df.append(file1)
    df = df.append(file3)
    df = df.append(file4)
    df = df.append(file5)
    df = df.append(file6)
    df = df.append(file7)
    df = df.append(file8)
    df = df.append(file9)
    df = df.append(file10)
    df = df.append(file11)
    df = df.append(file12)
    df = df.append(file13)
    df = df.append(file14)
    df = df.append(file15)
    df = df.append(file16)
    df = df.append(file17)
    df = df.append(file18)
    df = df.append(file19)
    df = df.append(file20)

    df = df.reset_index(drop=True)
    df = df.iloc[:, 2:]
    df.info()
    print(df['label'].value_counts())
    ef = df.to_csv('/home/abeer/PycharmProjects/GenderClassification/HAR_DataSet_Labeled.csv', index=None)
def merge_without_testFiles():
    folder = 'LeftLegSensor/'

    file2 = pd.read_csv(folder + "Arwa.csv")
    file3 = pd.read_csv(folder + "yousef.csv")
    file4 = pd.read_csv(folder + "Islam.csv")
    file5 = pd.read_csv(folder + "karim.csv")
    file6 = pd.read_csv(folder + "Abdo.csv")
    file7 = pd.read_csv(folder + "Abeer.csv")
    file8 = pd.read_csv(folder + "toqa.csv")
    file9 = pd.read_csv(folder + "menna.csv")
    file10 = pd.read_csv(folder + "AhmedNasr.csv")

    file11 = pd.read_csv(folder + "AhmedHesham.csv")
    file12 = pd.read_csv(folder + "Sharshar.csv")
    file13 = pd.read_csv(folder + "fayez.csv")
    file14 = pd.read_csv(folder + "hossam.csv")

    file16 = pd.read_csv(folder + "Rania.csv")
    file17 = pd.read_csv(folder + "mennaAbdo.csv")
    file18 = pd.read_csv(folder + "Farida.csv")
    file19 = pd.read_csv(folder + "Dina.csv")
    file20 = pd.read_csv(folder + "Asmaa.csv")


    file2['label'] = None
    file3['label'] = None
    file4['label'] = None
    file5['label'] = None
    file6['label'] = None
    file7['label'] = None
    file8['label'] = None
    file9['label'] = None
    file10['label'] = None

    file11['label'] = None
    file12['label'] = None
    file13['label'] = None
    file14['label'] = None

    file16['label'] = None
    file17['label'] = None
    file18['label'] = None
    file19['label'] = None
    file20['label'] = None




    file2['label'].fillna(1, inplace=True)
    file7['label'].fillna(1, inplace=True)
    file8['label'].fillna(1, inplace=True)
    file9['label'].fillna(1, inplace=True)
    file3['label'].fillna(0, inplace=True)
    file4['label'].fillna(0, inplace=True)
    file5['label'].fillna(0, inplace=True)
    file6['label'].fillna(0, inplace=True)
    file10['label'].fillna(0, inplace=True)

    file11['label'].fillna(0, inplace=True)
    file12['label'].fillna(0, inplace=True)
    file13['label'].fillna(0, inplace=True)
    file14['label'].fillna(0, inplace=True)

    file16['label'].fillna(1, inplace=True)
    file17['label'].fillna(1, inplace=True)
    file18['label'].fillna(1, inplace=True)
    file19['label'].fillna(1, inplace=True)
    file20['label'].fillna(1, inplace=True)

    df = file2

    df = df.append(file3)
    df = df.append(file4)
    df = df.append(file5)
    df = df.append(file6)
    df = df.append(file7)
    df = df.append(file8)
    df = df.append(file9)
    df = df.append(file10)
    df = df.append(file11)
    df = df.append(file12)
    df = df.append(file13)
    df = df.append(file14)

    df = df.append(file16)
    df = df.append(file17)
    df = df.append(file18)
    df = df.append(file19)
    df = df.append(file20)

    df = df.reset_index(drop=True)
    df = df.iloc[:, 2:]
    df.info()
    print(df['label'].value_counts())
    ef = df.to_csv('/home/abeer/PycharmProjects/GenderClassification/HAR_DataSet_without_TestFiles.csv', index=None)


def prepare_test():

    folder = 'LeftLegSensor/'
    file1 = pd.read_csv(folder + "ola.csv")
    file2 = pd.read_csv(folder + "Osama.csv")
    file1['label'] = None
    file2['label'] = None
    file1['label'].fillna(1, inplace=True)
    file2['label'].fillna(0, inplace=True)

    df = file2
    df = df.append(file1)

    df = df.reset_index(drop=True)
    df = df.iloc[:, 2:]
    df.info()
    print(df['label'].value_counts())
    ef = df.to_csv('/home/abeer/PycharmProjects/GenderClassification/HAR_TestFile.csv', index=None)


merge()
merge_without_testFiles()
prepare_test()
