import os
from Oscilloscope.FileReader import FileReader
from Oscilloscope.Oscilloscope import Oscilloscope

filelist = os.listdir()

osiloskop = Oscilloscope(['0.bin', '1.bin'])
osiloskopfromjson = Oscilloscope.loadFromJson('berker/data.json')
info = {'key' : 1234,'key2':456}
for name, value in info.items():
    print(name, value)



