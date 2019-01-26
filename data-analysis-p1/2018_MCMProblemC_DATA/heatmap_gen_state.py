#!/usr/bin/env python

import csv
import pickle

from drug import drug_list
from utils import find_county_index
from structor import County, Record


target_states = ['Ohio', 'Kentucky',
                 'West Virginia', 'Virginia', 'Pennsylvania']


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

state_info = []

for state in target_states:
    for year in range(2010, 2018):
        state_info.append([state, year, 0])


for r in recs:
    if limit_drug != "":
        if drug_list[r.substance_id] != limit_drug:
            continue

    idx = target_states.index(r.county.state)
    print("%d - %s, year %d, count %d" %
          (idx, r.county.state, r.year, r.drug_report_count))
    state_info[idx * 8 + r.year - 2010][2] += r.drug_report_count


savefilename = input("Save it to [where].csv... \n>>> ")

if limit_drug != "":
    savefilename = '%s - %s.csv' % (savefilename, limit_drug)
else:
    savefilename += ' - all.csv'

with open(savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["州名", "年份", "数量"])
    for row in state_info:
        spamwriter.writerow(row)
