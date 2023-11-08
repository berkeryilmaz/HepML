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
        for time_slice in time_slice_list:
            duration = time_slice * 5000
            begin, end = 0, duration
            while (end < data_length):
                params = createMeasureParams(splitRoot)
                params['Time_Window'] = time_slice
                params['Peak_Count'] = active_channel[0].countPeaks(begin, end)
                liste.append(params)
                begin, end = end, end + duration

        print(i, root)
        i += 1

df = pd.DataFrame.from_records(liste)
df.to_csv('out.csv')
print(df)
