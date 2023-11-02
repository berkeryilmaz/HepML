import numpy as np
import pandas as pd
import json

with open("data/filename.ini", "r") as f:
    file_list = list(filter(bool, f.read().split("\n")))

#excel_writer = pd.ExcelWriter("excel_file.xlsx", mode="w")

arr = []

for filename in file_list:
    with open(f"data/{filename}", "rb") as data_file:
        data = data_file.read()
        split_data = data.split(0xf0050000.to_bytes(4,"big"))
        headers = split_data[0].decode().split('\x00')[2]
        jsonHeader = json.loads(headers)

        byte_data = np.frombuffer(split_data[-1], dtype=np.int16)
        tmp_arr = []
        for num in byte_data:
            num = round(num/400.0 + 0, 5)
            arr.append(num)
            tmp_arr.append(num)
        print(len(tmp_arr))

print(jsonHeader)
print(len(arr))
