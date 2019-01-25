#!/usr/bin/env python

import csv
import pickle

from drug import drug_list
from utils import find_county_index
from structor import County, Record

for i in drug_list:
    print(" - %s" % i)

limit_drug = input(
    "Which drug would you want? Press <Enter> to select all >>> ")


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

    print(r)

    flag = True
    for dg in drug_info:
        if dg[4] == r.county.literal_name + "/" + r.county.state and dg[2] == r.year:
            dg[3] += r.drug_report_count
            flag = False
            break

    if flag:
        drug_info.append([r.county.latitude, r.county.longitude,
                          r.year, r.drug_report_count, r.county.literal_name + "/" + r.county.state])


savefilename = input("Save it to [where].csv... \n>>> ")

if limit_drug != "":
    savefilename = '%s - %s.csv' % (savefilename, limit_drug)
else:
    savefilename += ' - all.csv'

with open(savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["经度", "纬度", "Year", "Amount", "Name"])
    for row in drug_info:
        spamwriter.writerow(row)
