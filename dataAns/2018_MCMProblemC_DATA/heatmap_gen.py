#!/usr/bin/env python

import csv
import pickle

from drug import drug_list
from utils import find_county_index
from structor import County, Record


readfilename = input("Input [filename].loc... \n>>> ")
locs = []

if readfilename == "":
    readfilename = "cnt_db"

with open("%s.loc" % readfilename, 'rb') as file:
    locs = pickle.loads(file.read())


if type(locs) != list:
    raise TypeError("Bad File Format")

heat_loc = []

for loc in locs:
    itm = [loc.latitude, loc.longitude, loc.literal_name.split(',')[0], 0]
    heat_loc.append(itm)

print("Successfully get %d counties." % len(locs))

readfilename = input("Input [filename].rec... \n>>> ")
recs = []

if readfilename == "":
    readfilename = "rec_db"

with open("%s.rec" % readfilename, 'rb') as file:
    recs = pickle.loads(file.read())


if type(recs) != list:
    raise TypeError("Bad File Format")

print("Successfully get %d records." % len(recs))

for r in recs:
    county_index = find_county_index(r.county.literal_name, locs)
    heat_loc[county_index][3] += r.drug_report_count


savefilename = input("Save it to [where].csv... \n>>> ")


with open('%s.csv' % savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["经度", "纬度", "名称", "数量"])
    for row in heat_loc:
        spamwriter.writerow(row)
