'''
Egypt-Japan University of Science and Technology
Cyber-Physical Systems Lab

Author: Osama Adel
Date: 19 Dec 2019

Description:

This script is written primarily for the aggregation of the dataset on Human Activity Recognition.
The dataset is collected using 6 units mounted on 6 different parts of the volunteers body namely,
the Right Upper Arm (RUA), the Left Uppder Arm (LUA), Left Cube (LC), Right Cube (RC), Waist and 
Back. Two Apple watches are also used in the data collection but they are not involved in this data
aggregation script.

Each unit of the six generates 4 files for the Accelerometer, Gyroscope, Magnetometer and Pressures
sensors. These readings should be merged together in one file in order to be processed. This script
reads the any number of files related to each unit (as configured in the configuration file) and
aggregates their data in one new file then save it to the location specified in the configuration
file or in the current directory if no folder is specified (an empty string).

The output of this script is, for each folder containing units' files, it will generate one file
per unit which contains all the unit's data joint or aggregated together as columns.

How to use:
1. Edit the configuration file to specify the folders to consider and the units and sensors to
    aggregate in each folder.
2. At this file's directory, write the following command in the terminal:
    python aggregate.py experiment_config.json
3. If you changed the configuration file's name (and you shouldn't), please change
    "experiment_config.json" to the new name.

NOTICE: For every folder in the configuration file, you have to create the output folders
        manually for now, because if the folders are not provided, it will raise an error.
'''

def getConfigs(file:str):
    import json
    with open(file, 'r') as json_file:
        config = json.load(json_file)
    return config


def getFileNames(folder:str):
    '''
    input:
        folder: path to folder containing all units data.
    output:
        a list of all file names inside folder.
    '''
    from os import listdir
    files = listdir(folder)
    return [folder + f for f in files]


def filterNames(unitName:str, filesNames:list):
    '''
    Takes in a unit name and list of file names and returns a list of the file names containing the unit name.
    input:
        unitName: the unit name.
        filesNames: a list of file names to filter.
    output:
        a list which is a subset of fileNames with the unitNames in it.
    '''
    unitFilesNames = []
    for fileName in filesNames:
        if unitName in fileName:
            unitFilesNames.append(fileName)
    return unitFilesNames


def readAndMerge(csvfiles:list, on:str, droppedColumns:list):
    '''
    Reads every csv file in csvFiles and merge them on the common column on.
    input:
        csvFiles: a list of csv file names.
        on: name of the common column to merge all csv files on.
    output:
        a pandas.DataFrame object that is the merge of all csvFiles
    '''
    import pandas as pd
    data = None
    for fileName in csvfiles:
        if data is None:
            data = pd.read_csv(fileName, sep=',').drop(droppedColumns, axis=1)
        else:
            temp = pd.read_csv(fileName, sep=',').drop(droppedColumns, axis=1)
            data = pd.merge(data, temp, on=on)
            del temp
    return data


def aggregate(filesNames:list, units:list, sensors:list, droppedColumns:list, commonColumn:str):
    '''
    Receives files' names in a folder, the units' names, the sensors' names, columns to drop, and the column to merge
    tables on, then return an aggregated table of all the sensors of every unit after dropping the columns to drop,
    and merging them on the common column.
    input:
        filesNames: a list of file names in the data folder.
        units: a list of units' names to consider.
        sensors: a list of sensors' names to consider.
        droppedColumns: a list of column names to drop at each sensor.
        commonColumn: the name of the column on which to merge tables
    output:
        a dictionary with keys as unit names and values as pandas.DataFrame object that are
         the aggregated data of all sensors of that unit.
    '''
    data = {}
    for unit in units:
        csvFiles = []
        names = filterNames(unit, filesNames)
        for sensor in sensors:
            csvFiles.extend(filterNames(sensor, names))
        data[unit] = readAndMerge(csvFiles, commonColumn, droppedColumns)
    return data


def saveData(data, dest):
    for unit in data:
        data[unit].to_csv(dest + unit + '.csv')


if __name__ == '__main__':
    import argparse

    # define positional arguments
    parser = argparse.ArgumentParser(description="Aggregate every unit's sensory files into one aggregate CSV file")
    parser.add_argument('config', help='path to configuration file')
    parser.add_argument('--on', help='column name to join tables on')

    # parsing
    args = parser.parse_args()
    
    # reading configuration file
    conf = getConfigs(args.config)
    
    # Aggregating files in every folder in the configuration file
    for folder in conf:
        # LOGGING
        print("Aggregating Files in", folder)

        # retreiving configuration
        files = getFileNames(folder)
        units = conf[folder]['units']
        sensors = conf[folder]['sensors']
        droppedColumns = conf[folder]['dropped']    
        
        # LOGGING
        print('Configurations Retreived Successfully ...')

        # aggregating the units' files
        data = aggregate(files, units, sensors, droppedColumns, args.on if args.on else 'timestamp (+0200)')
        
        # LOGGING
        print('Data Aggregated Successfully ...')

        # saving the aggregated files to the output folder if provided, or the current folder
        saveData(data, conf[folder]['out'])

        # LOGGING
        print('Data Saved Successfully in {}...\n\n'.format(
            conf[folder]['out'] if conf[folder]['out'] else "current directory"))
    
    # LOGGING
    print('Terminated')
