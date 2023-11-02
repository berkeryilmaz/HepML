class Sample:
    def __init__(self, sample_dict):
        self.fullscreen = sample_dict['FULLSCREEN']
        self.slowmove = sample_dict['SLOWMOVE']
        self.datalen = sample_dict['DATALEN']
        self.samplerate = sample_dict['SAMPLERATE']
        self.type = sample_dict['TYPE']
        self.depmem = sample_dict['DEPMEM']
        self.precision = sample_dict['PRECISION']
