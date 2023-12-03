import os
from multiprocessing import Pool
import helper
from helper import *
import pandas as pd
from Oscilloscope.Oscilloscope import Oscilloscope

path = "detektor data 2"

time_slice_list = [1, 3, 5, 10, 15, 25]


walk = os.walk(path)
i = 1

def saveTimeSepatedData(root):
    liste = []
    splitRoot = root.lower().split('/')
    osci = Oscilloscope([root + '/' + file_name for file_name in getOrderedFileList(root)])
    active_channel = osci.getActiveChannel()
    data_length = len(active_channel[0].data)
    for time_slice in time_slice_list:
        duration = time_slice * 5000
        begin, end = 0, duration
        while (end < data_length):
            params = createMeasureParams(splitRoot)
            params['Time_Window'] = time_slice
            params['Peak_Count'] = active_channel[0].countPeaks(begin, end)
            params['Folder'] = root
            params['Successful_Read'] = active_channel[0].successful_read
            liste.append(params)
            begin, end = end, end + duration
            print(time_slice,root)
    return liste

if __name__ == '__main__':
    pool = Pool()
    path = "detektor data 2"
    dir_list = helper.getFileDirs(path)
    results = pool.map(saveTimeSepatedData, dir_list)

    liste = []
    for row in results:
        liste.extend(row)

    df = pd.DataFrame.from_records(liste)
    df.to_csv('out time separated 2.csv')
    print(df)
