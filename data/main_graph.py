import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# Constants
MIN_FREQ = 10_000

# Read
with open("data/filename.ini", "r") as f:
    file_list = list(filter(bool, f.read().split("\n")))

excel_writer = pd.ExcelWriter("excel_file.xlsx", mode="w")

arr = []

for filename in file_list:
    with open(f"data/{filename}", "rb") as data_file:
        data = data_file.read()
        split_data = data.split(0xf0050000.to_bytes(4))

        byte_data = np.frombuffer(split_data[-1], dtype=np.int16)

        for num in byte_data:
            num = round(num/800.0 + 2.1, 2)
            arr.append(num)

# FFT
fft_transform = np.fft.fft(arr)
fft_transform = fft_transform[:len(fft_transform)//2]  # Signals are all real numbers, ignore the second half.

# Eliminate noise
up_to_index = 1
start_from_index = MIN_FREQ

fft_transform = np.concatenate((fft_transform[:up_to_index], np.zeros(start_from_index - up_to_index, dtype=np.complex128), fft_transform[start_from_index:]))

# Inverse FFT
filtered_data = np.fft.ifft(fft_transform, n=len(arr))

# Write to Excel
pd.DataFrame(filtered_data).to_excel(
    excel_writer=excel_writer,
    #sheet_name=f"sheet_{filename}",
    index=False,
    header=False
)
excel_writer._save

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
