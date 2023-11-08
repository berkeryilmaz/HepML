import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
from matplotlib import interactive
import os

interactive(True)


class Channel:
    def __init__(self, channel_dict):
        channel_dict = {key.lower(): channel_dict[key] for key in channel_dict}
        self.name = channel_dict['name']
        self.display = channel_dict['display']
        self.current_rate = channel_dict['current_rate']
        self.current_ratio = channel_dict['current_ratio']
        self.measure_current_switch = channel_dict['measure_current_switch']
        self.coupling = channel_dict['coupling']
        self.probe = channel_dict['probe']
        self.scale = channel_dict['scale']
        self.offset = channel_dict['offset']
        self.frequence = channel_dict['frequence']
        self.inverse = channel_dict['inverse']
        self.data = channel_dict['data'] if 'data' in channel_dict else []

    def setData(self, raw_data):
        for value in raw_data:
            num = round(value / (self.current_rate / self.current_ratio) + 0, 5)
            self.data.append(num)

    def findPeaks(self, begin=None, end=None):
        if (begin != None and end != None):
            readData = pd.DataFrame(self.data[begin:end])
        else:
            readData = pd.DataFrame(self.data)
        smootedData = readData[[0]].apply(savgol_filter, window_length=4, polyorder=3)
        sorted = readData.sort_values(0)
        filtered = sorted[int(len(sorted) * 0.2):int(len(sorted) * 0.80)]
        std = np.std(filtered[0])
        peaks, _ = find_peaks(smootedData[0], prominence=std * 3, wlen=21)
        return peaks

    def countPeaks(self, begin=None, end=None):
        return len(self.findPeaks(begin, end))

    def showPlot(self, title='', begin=None, end=None):
        self.setPlot(title, begin, end)
        plt.show(block=True)

    def savePlot(self, path, title, begin=None, end=None):
        self.setPlot(title, begin, end)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path)
        plt.close('all')

    def setPlot(self, title, begin=None, end=None):
        if (begin != None and end != None):
            readData = pd.DataFrame(self.data[begin:end])
        else:
            readData = pd.DataFrame(self.data)
        peaks = self.findPeaks(begin, end)

        plt.figure(figsize=(12, 6))
        plt.xlabel("Time")
        plt.ylabel("Volt")
        plt.title(title)

        plt.plot(readData, color="orange", linewidth=1, label='Volt')
        plt.scatter(peaks, readData[0][peaks], color="red", linewidth=2, label=f"Peaks ({len(peaks)})")
        plt.legend(loc="upper left")
