#!/usr/bin/env python

import csv
import pickle
import pandas as pd
from math import sqrt
from pack import Pack
from utils import find_county_index

readfilename = input("Input [datagrab].ans... \n>>> ")
locs = []

if readfilename == "":
    readfilename = "datagrab"

with open("%s.ans" % readfilename, 'rb') as file:
    locs = pickle.loads(file.read())

flow_items = []

if type(locs) != list:
    raise TypeError("Bad File Format")

print("Successfully opened %s packages." % len(locs))

id = 0
for i in locs:
    print(i)
    count = 0

    for flowto in i.nearest_id:
        src_id = id
        dst_id = flowto
        if count == 0:
            affect_idx = i.affect_index_a
        elif count == 1:
            affect_idx = i.affect_index_b
        else:
            affect_idx = i.affect_index_c
        count += 1
        if affect_idx > 0.0:
            new_item = [src_id, dst_id, "%.9f" % affect_idx]
            flow_items.append(new_item)
            print(new_item)
            # input()
    id += 1

savefilename = input("Save it to [where].csv... \n>>> ")

savefilename += '.csv'

with open(savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["StartId", "DestId", "AffectIndex"])
    for row in flow_items:
        spamwriter.writerow(row)
