from Oscilloscope.FileReader import FileReader
from Oscilloscope.TimeBase import TimeBase
from Oscilloscope.Sample import Sample
from Oscilloscope.Trig import Trig


class Oscilloscope:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.files = self.getRecordFiles()
        self.timebase = None
        self.sample = None
        self.channel = None
        self.datatype = None
        self.runstatus = None
        self.idn = None
        self.model = None
        self.trig = None

        self.setOscilloscopeParams()

    def getRecordFiles(self):
        record_files = []
        for file_path in self.file_paths:
            file = FileReader(file_path).readFileInfo()
            record_files.append(file)
        return record_files

    def mergeRecordFiles(self):
        firstFile = self.files[0]
        for currentFile in self.files[1:]:
            for i, channel in enumerate(currentFile.channel):
                firstFile.channel[i].data += channel.data
        return firstFile

    def setOscilloscopeParams(self):
        file = self.mergeRecordFiles()
        for attr in file.__dict__:
            setattr(self, attr, getattr(file,attr))
