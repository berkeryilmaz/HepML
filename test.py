import os
import json
from Oscilloscope.FileReader import FileReader
from Oscilloscope.Oscilloscope import Oscilloscope

filelist = os.listdir()
#osiloskop_info = Oscilloscope(['0.bin'])
osiloskopLocal = Oscilloscope(['data_test/local/0.bin'])
osiloskopRemote = Oscilloscope(['data_test/remote/1.bin'])

if(osiloskopLocal.getActiveChannel()[0].data == osiloskopRemote.getActiveChannel()[0].data):
    print(True)
else:
    print(False)

osiloskopfromjson = Oscilloscope.loadFromJson('berker/data.json')
info = {'key' : 1234,'key2':456}
for name, value in info.items():
    pass
    #print(name, value)



