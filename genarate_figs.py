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
        fileList = [file_name for file_name in getOrderedFileList(root)]
        for file in fileList:
            osci = Oscilloscope([root + '/' + file])
            active_channel = osci.getActiveChannel()
            title = ' > '.join(splitRoot[1:]) + ' > ' + file
            active_channel[0].showPlot(title)
            active_channel[0].savePlot(image_root + '/' + file.replace('.bin', '.png'),title)