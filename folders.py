import os
from helper import *
import pandas as pd
from Oscilloscope.Oscilloscope import Oscilloscope

path = "detektor data 2"

time_slice_list = [1, 3, 5, 10, 15, 25]

liste = []
walk = os.walk(path)
i = 1
for (root, dirs, file) in os.walk(path):
    splitRoot = root.lower().split('/')
    image_root = root.replace(path, 'berker')
    if (len(splitRoot) == 6 and len([name for name in file if name.endswith('.bin')]) > 0):
        osci = Oscilloscope([root + '/' + file_name for file_name in getOrderedFileList(root)])
        active_channel = osci.getActiveChannel()
        data_length = len(active_channel[0].data)
        params = createMeasureParams(splitRoot)
        params['Peak_Count'] = active_channel[0].countPeaks()
        params['Data_Length'] = data_length
        params['Folder'] = root
        params['Successful_Read'] = active_channel[0].successful_read
        liste.append(params)

        print(i, root)
        i += 1
    if i > 20:
        break

df = pd.DataFrame.from_records(liste)
df.to_csv('out.csv')
print(df)
