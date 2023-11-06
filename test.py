import os
import json
from Oscilloscope.FileReader import FileReader
from Oscilloscope.Oscilloscope import Oscilloscope

filelist = os.listdir()
osiloskop_info = Oscilloscope(['0.bin'])
osiloskop1 = Oscilloscope(['detektor data 2/P20/Kare/Kare 10x10/6x6/4000V kaynaksız/5.bin'])


osiloskopfromjson = Oscilloscope.loadFromJson('berker/data.json')
info = {'key' : 1234,'key2':456}
for name, value in info.items():
    pass
    #print(name, value)



