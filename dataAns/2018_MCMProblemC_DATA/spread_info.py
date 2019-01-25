#!/usr/bin/env python

import csv
import pickle

from drug import drug_list
from utils import find_county_index
from structor import County, Record

for i in drug_list:
    print(" - %s" % i)

limit_drug = input(
    "Which drug would you want? >>> ")


readfilename = input("Input [filename].rec... \n>>> ")
recs = []

if readfilename == "":
    readfilename = "rec_db"

with open("%s.rec" % readfilename, 'rb') as file:
    recs = pickle.loads(file.read())


if type(recs) != list:
    raise TypeError("Bad File Format")

print("Successfully get %d records." % len(recs))

drug_info = []

for r in recs:

    if drug_list[r.substance_id] != limit_drug:
        continue
    print(r)
    drug_info.append([r.county.latitude, r.county.longitude,
                      r.year, r.drug_report_count, r.county.literal_name])


savefilename = input("Save it to [where].csv... \n>>> ")

if limit_drug != "":
    savefilename = '%s - %s.csv' % (savefilename, limit_drug)
else:
    savefilename += '.csv'

with open(savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["经度", "纬度", "年份", "数目", "地名"])
    for row in drug_info:
        spamwriter.writerow(row)
