class Channel:
    def __init__(self, channel_dict):
        self.name = channel_dict['NAME']
        self.display = channel_dict['DISPLAY']
        self.current_rate = channel_dict['Current_Rate']
        self.current_ratio = channel_dict['Current_Ratio']
        self.measure_current_switch = channel_dict['Measure_Current_Switch']
        self.coupling = channel_dict['COUPLING']
        self.probe = channel_dict['PROBE']
        self.scale = channel_dict['SCALE']
        self.offset = channel_dict['OFFSET']
        self.frequence = channel_dict['FREQUENCE']
        self.inverse = channel_dict['INVERSE']
        self.data = []

    def setData(self,raw_data):
        for value in raw_data:
            num = round(value / (self.current_rate / self.current_ratio) + 0, 5)
            self.data.append(num)
