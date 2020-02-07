# Import Libraries

import tensorflow.keras as keras
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import History
import math as m
import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import accuracy_score, confusion_matrix


from sklearn.ensemble import RandomForestClassifier


import pywt


def RF_classifier(x_train, y_train, x_test, y_test):
    classifier = RandomForestClassifier()
    res = []
    for i in range(10):
        classifier.fit(x_train.reshape((x_train.shape[0], x_train.shape[1]*x_train.shape[2]*x_train.shape[3])), y_train)
        y_pred_RF = classifier.predict(x_test.reshape((x_test.shape[0], x_test.shape[1]*x_test.shape[2]*x_test.shape[3])))
        accuracy = accuracy_score(y_test, y_pred_RF)
        res.append(accuracy)

        print('prediction accuracy on test set: {:.4f}%'.format(accuracy* 100))

    print('Avg prediction accuracy on test set: {:.4f}%'.format((sum(res)/len(res) )* 100))

def svm_classifier(x_train, y_train, x_test, y_test):
    SVM_clf = SVC(kernel='rbf', random_state=0)

    SVM_clf.fit(x_train.reshape((x_train.shape[0], 145161)), y_train)

    y_pred_SVM = SVM_clf.predict(x_test.reshape((x_test.shape[0], 145161)))
    accuracy = accuracy_score(y_test, y_pred_SVM)

    print('prediction accuracy on test set: {:.4f}%'.format(accuracy * 100))

def CNN(x_train, y_train, x_test, y_test):
    history = History()

    input_shape = x_train[0].shape
    print("one sample input shape to the neural network =  ", input_shape, "num of samples =  ", x_train.shape[0] )
    batch_size = 10
    num_classes = 2
    epochs = 14

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    model = Sequential()
    model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(64, (5, 5), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))

    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss=keras.losses.binary_crossentropy, optimizer=keras.optimizers.Adam(), metrics=['accuracy'])

    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test), callbacks=[history])

    train_score = model.evaluate(x_train, y_train, verbose=0)
    print('Train loss: {}, Train accuracy: {}'.format(train_score[0], train_score[1]))
    test_score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss: {}, Test accuracy: {}'.format(test_score[0], test_score[1]))

def splitting_into_samples(df, sampling_rate):

    split_period = 5  # seconds
    split_size = sampling_rate * split_period

    splitted_dataset = np.zeros((m.floor(df.shape[0]/split_size), split_size, len(df.columns)))
    splitted_dataset[0, :, :] = df.iloc[0:0 + split_size, :].values

    for i, batch in enumerate(range(split_size, df.shape[0]-(df.shape[0]%split_size), split_size)):
        splitted_dataset[i+1, :, :] = df.iloc[batch:batch + split_size, :].values

    # rand_indices = np.random.choice([x for x in range(len(splitted_dataset))], size=len(splitted_dataset),
    #                                 replace=False)
    # splitted_dataset = [splitted_dataset[x] for x in rand_indices]
    return splitted_dataset

def separate_labels(splitted_dataset):
    labels = []
    for i in range(splitted_dataset.shape[0]):
        label = int(splitted_dataset[i,0,-1])
        labels.append(label)

    print(labels)
    features = splitted_dataset[:, :, 0:-1]

    return features, labels

def Autocorrelation(splitted_dataset, labels):
    pd.DataFrame(data=splitted_dataset[1:, 1:], index = splitted_dataset[1:, 0],  columns = splitted_dataset[0, 1:])  # 1st row as the column names
    lags = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    features = np.zeros(shape=[len(splitted_dataset), splitted_dataset[0].shape[1] * len(lags)])
    for i, sample in enumerate(splitted_dataset):
        for j, lag in enumerate(lags):
            for k, label in enumerate(sample.columns):
                features[i, j * 9 + k] = sample[label].autocorr(lag=lag)
    labels = np.asarray(labels)
    return features, labels

def remove_na(features, labels):
    bad_rows = []
    for i, r in enumerate(features):
        for e in r:
            if np.isnan(e):
                bad_rows.append(i)
                break
    for i in bad_rows:
        features = np.delete(features, i, axis=0)
        labels = np.delete(labels, i)
    print(features.shape, labels.shape)
    return features, labels

def wavelet_transform(train_signals_ucihar, test_signals_ucihar, train_labels_ucihar, test_labels_ucihar):
    scales = range(1, 64)
    waveletname = 'morl'

    train_size = len(train_signals_ucihar)
    test_size = len(test_signals_ucihar)

    train_data_cwt = np.ndarray(shape=(train_size, 63, 63, 6))

    for ii in range(0, train_size):
        if ii % 1000 == 0:
            print(ii)
        for jj in range(0, 6):
            signal = train_signals_ucihar[ii, :, jj]
            coeff, freq = pywt.cwt(signal, scales, waveletname, 1)
            coeff_ = coeff[:, :63]
            train_data_cwt[ii, :, :, jj] = coeff_

    test_data_cwt = np.ndarray(shape=(test_size, 63, 63, 6))
    for ii in range(0, test_size):
        if ii % 100 == 0:
            print(ii)
        for jj in range(0, 6):
            signal = test_signals_ucihar[ii, :, jj]
            coeff, freq = pywt.cwt(signal, scales, waveletname, 1)
            coeff_ = coeff[:, :63]
            test_data_cwt[ii, :, :, jj] = coeff_

    train_labels_ucihar = list(map(lambda x: int(x) - 1, train_labels_ucihar))
    test_labels_ucihar = list(map(lambda x: int(x) - 1, test_labels_ucihar))

    x_train = train_data_cwt
    y_train = list(train_labels_ucihar[:train_size])
    x_test = test_data_cwt
    y_test = list(test_labels_ucihar[:test_size])

    return x_train, y_train, x_test, y_test

def load_Osaka_dataset():

    df = pd.read_csv('Tokyo_DataSet_Labeled.csv')

    important_features = ['Gx', 'Gy', 'Gz', 'Ax', 'Ay', 'Az', 'label']
    sampling_rate = 100 #Hz
    return df, important_features, sampling_rate

def load_HAR_dataset(file):
    sampling_rate = 50 #Hz
    df = pd.read_csv(file)
    # Watches
    # important_features = ['user_acc_x(G)',
    #                       'user_acc_y(G)',
    #                       'user_acc_z(G)',
    #                       'rotation_rate_x(radians/s)',
    #                       'rotation_rate_y(radians/s)',
    #                       'rotation_rate_z(radians/s)',
    #                       'label']

    # Sensors
    important_features = ['x-axis (g)',
                          'y-axis (g)',
                          'z-axis (g)',
                          'x-axis (deg/s)',
                          'y-axis (deg/s)',
                          'z-axis (deg/s)',
                          'x-axis (g)_2',
                          'y-axis (g)_2',
                          'z-axis (g)_2',
                          'x-axis (deg/s)_2',
                          'y-axis (deg/s)_2',
                          'z-axis (deg/s)_2',
                          'label']

    df = df[important_features]
    df.fillna(0, inplace=True)
    return df, sampling_rate

def test_on_different_people():
    df_train, important_features, sampling_rate = load_HAR_dataset('HAR_DataSet_without_TestFiles.csv')
    df_test, important_features, sampling_rate = load_HAR_dataset('HAR_TestFile.csv')
    df_train.info()
    print(df_train['label'].value_counts())

    splitted_dataset_train = splitting_into_samples(df_train, sampling_rate)

    print("Number of samples and their shape :  ", splitted_dataset_train.shape)

    features_train, labels_train = separate_labels(splitted_dataset_train, important_features)

    df_test.info()
    print(df_test['label'].value_counts())

    splitted_dataset_test = splitting_into_samples(df_test, sampling_rate)

    print("Number of samples and their shape :  ", splitted_dataset_test.shape)

    features_test, labels_test = separate_labels(splitted_dataset_test, important_features)

    test_labels_ucihar = np.array(labels_test)
    test_signals_ucihar = features_test
    train_labels_ucihar = np.array(labels_train)
    train_signals_ucihar = features_train
    return train_signals_ucihar, test_signals_ucihar, train_labels_ucihar, test_labels_ucihar

def concat_with_same_features(file1_HAR, file2):
    f1 = pd.read_csv(file1_HAR)
    f2 = pd.read_csv(file2)

    important_features = ['x-axis (g)',
                          'y-axis (g)',
                          'z-axis (g)',
                          'x-axis (deg/s)',
                          'y-axis (deg/s)',
                          'z-axis (deg/s)',
                          'label']
    f1 = f1[important_features]
    f2.columns = important_features
    f1 = f1.append(f2)
    f1 = f1.reset_index(drop = True)
    result = 'combinations/HAR_OSAKA.csv'
    ef = f1.to_csv(result, index=None)
    return result

def concat_with_adding_features(file1, file2, sensors):
    f1 = pd.read_csv(file1)
    f2 = pd.read_csv(file2)
    important_features = ['x-axis (g)',
                          'y-axis (g)',
                          'z-axis (g)',
                          'x-axis (deg/s)',
                          'y-axis (deg/s)',
                          'z-axis (deg/s)',
                          'label']
    f1 = f1[important_features]
    f2 = f2[important_features]
    f2.columns = ['x-axis (g)_2',
                          'y-axis (g)_2',
                          'z-axis (g)_2',
                          'x-axis (deg/s)_2',
                          'y-axis (deg/s)_2',
                          'z-axis (deg/s)_2',
                          'label_2']
    print(f1.info())
    print(f2.info())
    result = pd.concat([f1, f2], axis=1)
    indeces = result[result['label'] != result['label_2']].index
    result.drop(indeces, inplace=True)
    result = result.reset_index(drop=True)
    print(result.info())
    result = result.drop(['label_2'], axis=1)

    file_name = 'combinations/HAR_' + sensors + '.csv'
    ef = result.to_csv(file_name, index=None)
    return file_name



if __name__ == "__main__":

    sensors = ['LUA', 'RUA', 'LC', 'RC', 'back', 'waist']
    s1 = ['RC', 'back', 'waist']
    for sensor in s1:
        file1 = 'HAR_DataSet_' + sensor + '_Labeled.csv'
        for sensor2 in sensors:
            print("The sensors are", sensor, sensor2)
            if sensor == sensor2:
                continue
            file2 = 'HAR_DataSet_' + sensor2 + '_Labeled.csv'
            #df,  important_features, sampling_rate= load_Osaka_dataset()

            # file = concat_with_same_features('HAR_DataSet_waist_Labeled.csv', 'Tokyo_DataSet_FixedLength_Labeled.csv')

            file = concat_with_adding_features(file1, file2, sensor + '_' + sensor2)
            df, sampling_rate= load_HAR_dataset(file)

            df.info()
            print(df['label'].value_counts())

            splitted_dataset = splitting_into_samples(df, sampling_rate)

            print("Number of samples and their shape :  ", splitted_dataset.shape)

            features, labels = separate_labels(splitted_dataset)

            # features, labels = Autocorrelation(features, labels)
            # features, labels = remove_na(features, labels)


            x = features
            y = np.array(labels)

            #train_signals_ucihar, test_signals_ucihar, train_labels_ucihar, test_labels_ucihar = test_on_different_people()
            train_signals_ucihar, test_signals_ucihar, train_labels_ucihar, test_labels_ucihar = train_test_split(x, y, test_size=0.2, random_state=0)  # Acc 95.36%

            print(train_signals_ucihar.shape)
            print(test_signals_ucihar.shape)
            print(train_labels_ucihar.shape)
            print(test_labels_ucihar.shape)

            # x_train, y_train, x_test, y_test = train_signals_ucihar, train_labels_ucihar, test_signals_ucihar, test_labels_ucihar

            x_train, y_train, x_test, y_test = wavelet_transform(train_signals_ucihar, test_signals_ucihar, train_labels_ucihar, test_labels_ucihar)

            print(x_train.shape)
            print(len(y_train))
            print(x_test.shape)
            print(len(y_test))

            RF_classifier(x_train, y_train, x_test, y_test)
            #svm_classifier(x_train, y_train, x_test, y_test)
            #CNN(x_train, y_train, x_test, y_test)


