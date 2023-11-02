class TrigItems:
    def __init__(self, trig_items_dict):
        self.channel = trig_items_dict['Channel']
        self.level = trig_items_dict['Level']
        self.edge = trig_items_dict['Edge']
        self.coupling = trig_items_dict['Coupling']
        self.hold_off = trig_items_dict['HoldOff']