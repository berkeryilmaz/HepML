import os
from helper import *
import pandas as pd
from Oscilloscope.Oscilloscope import Oscilloscope
import matplotlib.pyplot as plt

path = "detektor data 2"
for (root, dirs, file) in os.walk(path):
    splitRoot = root.lower().split('/')
    image_root = root.replace(path, 'image')
    if (len(splitRoot) == 6 and len([name for name in file if name.endswith('.bin')]) > 0):
        print(root)
        fileList = [file_name for file_name in getOrderedFileList(root)]
        for file in fileList[:10]:
            osci = Oscilloscope([root + '/' + file])
            active_channel_list = osci.getActiveChannel()
            for active_channel in active_channel_list:
                title = ' > '.join(splitRoot[1:]) + ' > ' + file +f"({active_channel.name} - {active_channel.scale})"
                active_channel.savePlot(image_root + '/' + file.replace('.bin', f"({active_channel.name} - {active_channel.scale}).png"),title)
                df = pd.DataFrame(active_channel.data)
                df.to_csv(image_root + '/' + file.replace('.bin', f"({active_channel.name} - {active_channel.scale}).csv"))