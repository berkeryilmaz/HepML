class TimeBase:
    def __init__(self, time_base_dict):
        self.scale = time_base_dict['SCALE']
        self.hoffset = time_base_dict['HOFFSET']
