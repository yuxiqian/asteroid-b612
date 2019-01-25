#!/usr/bin/env python

import csv
import pickle

from drug import drug_list
from utils import find_county_index
from structor import County, Record


target_states = ['Ohio', 'Kentucky',
                 'West Virginia', 'Virginia', 'Pennsylvania']


for i in drug_list:
    print(" - %s" % i)

limit_drug = input(
    "Which drug would you want? Press <Enter> to select all >>> ")

for s in target_states:
    print(" - %s" % s)

target_state = input(
    "Which state would you want? Press <Enter> to select all >>> ")


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
    if limit_drug != "":
        if drug_list[r.substance_id] != limit_drug:
            continue

    if target_state != "":
        if r.county.state != target_state:
            continue

    print(r)
    drug_info.append([r.county.longitude, r.county.latitude,
                      r.year, r.drug_report_count, r.county.literal_name + "/" + r.county.state, drug_list[r.substance_id]])


savefilename = input("Save it to [where].csv... \n>>> ")

if target_state != "":
    savefilename += " - %s" % target_state

if limit_drug != "":
    savefilename = '%s - %s.csv' % (savefilename, limit_drug)
else:
    savefilename += ' - all.csv'

with open(savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["经度", "纬度", "年份", "数目", "地名", "药物"])
    for row in drug_info:
        spamwriter.writerow(row)
