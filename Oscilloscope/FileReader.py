import numpy as np
import json
from Oscilloscope.OscilloscopeSetup import OscilloscopeSetup

class FileReader:
    def __init__(self, filepath=None):
        self.filePath = filepath
        self.fileData = ''
        with open(self.filePath, "rb") as data_file:
            self.fileData = data_file.read()

    def readFileInfo(self):
        split_data = self.fileData.split(0xf0050000.to_bytes(4, "big"))
        oscilloscope_setup_str = split_data[0].decode('unicode_escape').split('\x00')[2]
        oscilloscope_setup_dict = json.loads(oscilloscope_setup_str)
        oscilloscope_setup = OscilloscopeSetup(oscilloscope_setup_dict)

        for i, channel in enumerate(oscilloscope_setup.channel):
            byte_data = np.frombuffer(split_data[1 + i], dtype=np.int16)
            channel.setData(byte_data)
        return oscilloscope_setup

    def readFromJson(self):
        oscilloscope_setup_dict = json.loads(self.fileData)
        oscilloscope_setup = OscilloscopeSetup(oscilloscope_setup_dict)
        return oscilloscope_setup
