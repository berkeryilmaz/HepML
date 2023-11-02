import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# Constants
SECOND_BANDWIDTH_START = 10000
FIRST_BANWIDTH_END = 1

# Read
with open("data/filename.ini", "r") as f:
    file_list = list(filter(bool, f.read().split("\n")))

excel_writer = pd.ExcelWriter("excel_file.xlsx", mode="w")

arr = []

for filename in file_list:
    with open(f"data/{filename}", "rb") as data_file:
        data = data_file.read()
        split_data = data.split(0xf0050000.to_bytes(4, byteorder="big"))

        byte_data = np.frombuffer(split_data[-1], dtype=np.int16)

        for num in byte_data:
            num = round(num/800.0 + 2.1, 2)
            arr.append(num)

# FFT
fft_transform = np.fft.fft(arr)
fft_transform = fft_transform[:len(fft_transform)//2]  # Signals are all real numbers, ignore the second half.

# Eliminate noise
fft_transform = np.concatenate((
    fft_transform[:FIRST_BANWIDTH_END],
    np.zeros(SECOND_BANDWIDTH_START - FIRST_BANWIDTH_END, dtype=np.complex128),
    fft_transform[SECOND_BANDWIDTH_START:]
))

# Inverse FFT
filtered_data = np.fft.ifft(fft_transform, n=len(arr)) * 2

# Write to Excel
pd.DataFrame(filtered_data).to_excel(
    excel_writer=excel_writer,
    #sheet_name=f"sheet_{filename}",
    index=False,
    header=False
)
excel_writer.save()
excel_writer.close()

# Plot
y = filtered_data
x = range(len(filtered_data))

plt.title("Filtered Data")
plt.plot(x, y)
plt.show()

y = arr
x = range(len(arr))

plt.title("Original Data")
plt.plot(x, y)
plt.show()
