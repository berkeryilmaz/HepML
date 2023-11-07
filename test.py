import os
import json
from Oscilloscope.FileReader import FileReader
from Oscilloscope.Oscilloscope import Oscilloscope

file = 'detektor data 2/P20/Kare/Kare 10x10/8x8/6000V Cs/0.bin'
osiloskop_info = Oscilloscope([file])

osiloskop_info.getActiveChannel()[0].showPlot()



