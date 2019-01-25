#!/usr/bin/env python

import pickle
import numpy as np
import pandas as pd
import seaborn as sns


from drug import drug_list
from abbr import abbr_to_full
from utils import find_county
from structor import County, Record

readfilename = input("Input [filename].loc... \n>>> ")
rq = []

if readfilename == "":
    readfilename = "cnt_db"

with open("%s.loc" % readfilename, 'rb') as file:
    rq = pickle.loads(file.read())


if type(rq) != list:
    raise TypeError("Bad File Format")

print("Successfully get %d items." % len(rq))

rcd_data = pd.read_csv('MCM_NFLIS_Data.csv')

data_len = len(rcd_data)

records = []

for rec in range(data_len):
    rec_item = rcd_data.iloc[rec]

    county = find_county(rec_item['COUNTY'], rq,
                         abbr_to_full(rec_item['State']))
    if county == None:
        print("Can't detect county %s." % rec_item['COUNTY'])
        continue

    print("Get county %s." % rec_item['COUNTY'])
    substance_id = drug_list.index(rec_item['SubstanceName'])

    irec = Record(int(rec_item['YYYY']),
                  county,
                  substance_id,
                  rec_item['DrugReports'],
                  rec_item['TotalDrugReportsCounty'],
                  rec_item['TotalDrugReportsState'])

    print(irec)
    records.append(irec)


savefilename = input("Save it to [where].rec... \n>>> ")
output_hal = open("%s.rec" % savefilename, 'wb')

str_data = pickle.dumps(records)
output_hal.write(str_data)
output_hal.close()
