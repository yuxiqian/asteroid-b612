#!/usr/bin/env python

import csv
import pickle

from drug import drug_list
from utils import find_county_index
from structor import County, Record

limit_year = input("Which year would you want? Press <Enter> to show all >>> ")


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
    itm = [loc.latitude, loc.longitude, loc.literal_name + ", " + loc.state, 0]
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
    if limit_year != "":
        if str(r.year) != limit_year:
            continue

    county_index = find_county_index(
        r.county.literal_name, locs, r.county.state)
    heat_loc[county_index][3] += r.drug_report_count


savefilename = input("Save it to [where].csv... \n>>> ")

if limit_year != "":
    savefilename = '%s - %s.csv' % (savefilename, limit_year)
else:
    savefilename += '.csv'

with open(savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["纬度", "经度", "名称", "数量"])
    for row in heat_loc:
        spamwriter.writerow(row)
