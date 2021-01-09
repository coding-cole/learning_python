import time
import os
import pandas

file_path = "files/temps.csv"
read_file = "r"
station1 = "st1"
station2 = "st2"
no_file_message = "File does not exist"

while True:
    if os.path.exists(file_path):
        data = pandas.read_csv(file_path)
        print(data.mean()[station1])
    else:
        print(no_file_message)

    time.sleep(10)
    