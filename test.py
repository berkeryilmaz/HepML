import os
from Oscilloscope.FileReader import FileReader
from Oscilloscope.Oscilloscope import Oscilloscope

filelist = os.listdir()

osiloskop = Oscilloscope(['0.bin', '1.bin'])

for name, value in dict.items():
    print(name, value)

file = FileReader('0.bin').readFileInfo()
print(file.filePath)
