from Oscilloscope.TrigItems import TrigItems
class Trig:
    def __init__(self, trig_dict):
        self.mode = trig_dict['Mode']
        self.type = trig_dict['Type']
        self.items = TrigItems(trig_dict['Items'])
        self.sweep = trig_dict['Sweep']