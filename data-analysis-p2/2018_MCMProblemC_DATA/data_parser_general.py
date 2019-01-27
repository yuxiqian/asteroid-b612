#!/usr/bin/env python

import csv
import pickle

from drug import drug_list
from utils import find_county_index
from structor import County, Record


target_states = ['Ohio', 'Kentucky',
                 'West Virginia', 'Virginia', 'Pennsylvania']


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

county_info = []

for r in recs:
    existed = False
    for l in county_info:
        if l[2] == r.year and l[4] == r.county.literal_name + ", " + r.county.state:
            existed = True
    if not existed:
        print(r)
        county_info.append([r.county.longitude, r.county.latitude,
                            r.year, r.county_drug_report_count, r.county.literal_name + ", " + r.county.state])


savefilename = input("Save it to [where].csv... \n>>> ")

if target_state != "":
    savefilename += " - %s.csv" % target_state
else:
    savefilename = "general_dp.csv"

with open(savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["经度", "纬度", "年份", "数目", "地名"])
    for row in county_info:
        spamwriter.writerow(row)
