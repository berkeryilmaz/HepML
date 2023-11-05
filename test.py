import os
import json
from Oscilloscope.FileReader import FileReader
from Oscilloscope.Oscilloscope import Oscilloscope

filelist = os.listdir()

osiloskop1 = Oscilloscope(['0.bin'])
osiloskop2 = Oscilloscope(['1.bin'])

if(osiloskop1.channel[1].data == osiloskop2.channel[1].data):
    print('true')

osiloskopfromjson = Oscilloscope.loadFromJson('berker/data.json')
info = {'key' : 1234,'key2':456}
for name, value in info.items():
    pass
    #print(name, value)



