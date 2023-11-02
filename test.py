from Oscilloscope.FileReader import FileReader

file = FileReader('0.bin').readFileInfo()
print(file.filePath)