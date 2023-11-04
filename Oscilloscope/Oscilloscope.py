from Oscilloscope.FileReader import FileReader
import json
import os

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
            setattr(self, attr, getattr(file, attr))

    @property
    def __dict__(self):
        return {
            'file_paths': self.file_paths,
            'timebase': self.timebase.__dict__,
            'sample': self.sample.__dict__,
            'channel': [ch.__dict__ for ch in self.channel],
            'datatype': self.datatype,
            'runstatus': self.runstatus,
            'idn': self.idn,
            'model': self.model,
            'trig': self.trig.__dict__
        }

    def saveAsJson(self, filePath):
        json_object = json.dumps(self.__dict__)
        os.makedirs(os.path.dirname(filePath), exist_ok=True)
        with open(filePath, "w") as outfile:
            outfile.write(json_object)