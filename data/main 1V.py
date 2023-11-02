import numpy as np
import pandas as pd

with open("data/filename.ini", "r") as f:
    file_list = list(filter(bool, f.read().split("\n")))

excel_writer = pd.ExcelWriter("excel_file.xlsx", mode="w")

arr = []

for filename in file_list:
    with open(f"data/{filename}", "rb") as data_file:
        data = data_file.read()
        split_data = data.split(0xf0050000.to_bytes(4,"big"))

        byte_data = np.frombuffer(split_data[-1], dtype=np.int16)

        for num in byte_data:
            num = round(num/400.0 + 4.36, 2)
            arr.append(num)

pd.DataFrame(arr).to_excel(
    excel_writer=excel_writer,
    #sheet_name=f"sheet_{filename}",
    index=False,
    header=False
)
excel_writer.close()