from Oscilloscope.TimeBase import TimeBase
from Oscilloscope.Sample import Sample
from Oscilloscope.Channel import Channel
from Oscilloscope.Trig import Trig

class OscilloscopeSetup:
    def __init__(self, setup_dict):
        self.timebase = TimeBase(setup_dict['TIMEBASE'])
        self.sample = Sample(setup_dict['SAMPLE'])
        self.channel = [Channel(ch) for ch in setup_dict['CHANNEL']]
        self.datatype = setup_dict['DATATYPE']
        self.runstatus = setup_dict['RUNSTATUS']
        self.idn = setup_dict['IDN']
        self.model = setup_dict['MODEL']
        self.trig = Trig(setup_dict['Trig'])
