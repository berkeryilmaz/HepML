class Channel:
    def __init__(self, channel_dict):
        channel_dict = { key.lower() : channel_dict[key] for key in channel_dict }
        self.name = channel_dict['name']
        self.display = channel_dict['display']
        self.current_rate = channel_dict['current_rate']
        self.current_ratio = channel_dict['current_ratio']
        self.measure_current_switch = channel_dict['measure_current_switch']
        self.coupling = channel_dict['coupling']
        self.probe = channel_dict['probe']
        self.scale = channel_dict['scale']
        self.offset = channel_dict['offset']
        self.frequence = channel_dict['frequence']
        self.inverse = channel_dict['inverse']
        self.data = channel_dict['data'] if 'data' in channel_dict else []

    def setData(self,raw_data):
        for value in raw_data:
            num = round(value / (self.current_rate / self.current_ratio) + 0, 5)
            self.data.append(num)
