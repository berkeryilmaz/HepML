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
    if (len(splitRoot) == 6 and len([name for name in file if name.endswith('.bin')]) > 0):
        osci = Oscilloscope([root + '/' + file_name for file_name in getOrderedFileList(root)])
        active_channel = osci.getActiveChannel()
        data_length = len(active_channel[0].data)
        for time_slice in time_slice_list:
            params = createMeasureParams(splitRoot)
            params['Time_Window'] = time_slice
            for x in range(0, 100):
                begin, end = getRandomPart(data_length, time_slice * 5000)
                params['Peak_Count'] = active_channel[0].countPeaks(begin, end)
                liste.append(params)

        print(i, root)
        i += 1

df = pd.DataFrame.from_records(liste)
df.to_csv('out.csv')
print(df)

