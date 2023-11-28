import os
from multiprocessing import Pool
from helper import *
import pandas as pd
from Oscilloscope.Oscilloscope import Oscilloscope

i = 0
def getFileDirs(root):
    dir_list = []
    for (root, dirs, file) in os.walk(path):
        splitRoot = root.lower().split('/')
        if (len(splitRoot) == 6 and len([name for name in file if name.endswith('.bin')]) > 0):
            dir_list.append(root)
    return dir_list

def countRootPeaks(root):
    osci = Oscilloscope([root + '/' + file_name for file_name in getOrderedFileList(root)])
    active_channel = osci.getActiveChannel()
    data_length = len(active_channel[0].data)
    splitRoot = root.lower().split('/')
    params = createMeasureParams(splitRoot)
    params['Peak_Count'] = active_channel[0].countPeaks()
    params['Data_Length'] = data_length
    params['Folder'] = root
    params['Successful_Read'] = active_channel[0].successful_read
    print(root)
    return params


if __name__ == '__main__':
    pool = Pool()
    path = "detektor data 2"
    dir_list = getFileDirs(path)
    results = pool.map(countRootPeaks, dir_list)

    df = pd.DataFrame.from_records(results)
    df.to_csv('out.csv')
    print(df)
