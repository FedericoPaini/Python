#!/usr/bin/python

import sys, os, os.path, re, time, datetime, locale, requests
import pandas as pd
import numpy as np

data_set = '/home/fedderico/Documents/code/python/FlaLottoDataset.csv'

df = pd.read_csv(data_set)

df.sort_values(by=['Date'])
df.set_index('Date')

print (df.head())