#!/usr/bin/env python3

from pandas_ods_reader import read_ods
import pandas as pd
import os

files = [i for i in os.listdir() if '.ods' in i]

for file in files:
    print(file[5:-4])
    df = read_ods(file, 1)
    df.to_csv(f'csv/{file[5:-4]}.csv')



