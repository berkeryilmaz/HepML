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

def saveFigures(root):
    splitRoot = root.lower().split('/')
    image_root = root.replace("detektor data 2", 'image')
    fileList = [file_name for file_name in getOrderedFileList(root)]
    for file in fileList[:10]:
        osci = Oscilloscope([root + '/' + file])
        active_channel_list = osci.getActiveChannel()
        for active_channel in active_channel_list:
            title = ' > '.join(splitRoot[1:]) + ' > ' + file + f"({active_channel.name} - {active_channel.scale})"
            active_channel.savePlot(
                image_root + '/' + file.replace('.bin', f"({active_channel.name} - {active_channel.scale}).png"),
                title)
            df = pd.DataFrame(active_channel.data)
            df.to_csv(
                image_root + '/' + file.replace('.bin', f"({active_channel.name} - {active_channel.scale}).csv"),
                float_format='%.3f')
    print(root)
    return True

if __name__ == '__main__':
    pool = Pool()
    path = "detektor data 2"
    dir_list = getFileDirs(path)
    results = pool.map(saveFigures, dir_list)
    print(results)
