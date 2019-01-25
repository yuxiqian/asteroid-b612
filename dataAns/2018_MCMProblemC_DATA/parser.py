#!/usr/bin/env python

import pickle
import numpy as np
import pandas as pd
import seaborn as sns

from structor import County, Record

readfilename = input("Input [filename].pkl... \n>>> ")
rq = []

if readfilename == "":
    readfilename = "cnt_db"

with open("%s.pkl" % readfilename, 'rb') as file:
    rq = pickle.loads(file.read())


if type(rq) != list:
    raise TypeError("Bad File Format")

print("Successfully get %d items." % len(rq))

rcd_data = pd.read_csv('MCM_NFLIS_Data.csv')

data_len = len(rcd_data)

drug_type = set()

for rec in range(data_len):
    rec_item = rcd_data.iloc[rec]
    drug_type.add(rec_item['SubstanceName'])

print(drug_type)
