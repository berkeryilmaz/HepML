import os
from helper import *
import pandas as pd
from Oscilloscope.Oscilloscope import Oscilloscope

path = "detektor data 2"

# to store files in a list
liste = []
walk = os.walk(path)
# dirs=directories
i = 1
for (root, dirs, file) in os.walk(path):
    splitRoot = root.lower().split('/')
    if (len(splitRoot) == 6 and len([name for name in file if name.endswith('.bin')]) > 0):
        osci = Oscilloscope([root + '/' + file_name for file_name in getOrderedFileList(root)[0:5]])
        print(i, root)
        active_channel = osci.getActiveChannel()
        params = createMeasureParams(splitRoot)
        params['avg'] = sum(active_channel[0].data) / len(active_channel[0].data)
        params['root'] = root
        params['active_channel_count'] = len(active_channel)
        params['Time_Window'] = len(active_channel[0].data) / 5000
        params['Peak_Count'] = active_channel[0].countPeaks()
        liste.append(params)
        i += 1

df = pd.DataFrame.from_records(liste)
df.to_csv('out.csv')
print(df)
