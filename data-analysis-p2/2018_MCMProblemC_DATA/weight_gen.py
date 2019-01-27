#!/usr/bin/env python

import csv
import pickle
import numpy as np
import pandas as pd
from pack import Pack

target_params = ['HC01_VC04',
                 'HC01_VC37', 'HC01_VC86', 'HC01_VC85', 'HC01_VC80']

result = ['Families - 1',
          'Happy Marriage - 2', '25 year+ total - 4 Total', 'College - 5']


def get_filehead(yr):
    return "ACS_%d_5YR_DP02/ACS_%d_5YR_DP02_with_ann.csv" % (
        yr + 10, yr + 10)


readfilename = input("Input [filename].obj... \n>>> ")
packages = []

if readfilename == "":
    readfilename = "raw_model"

with open("%s.obj" % readfilename, 'rb') as file:
    packages = pickle.loads(file.read())


if type(packages) != list:
    raise TypeError("Bad File Format")

print("Successfully get %d items." % len(packages))


results = []

for year in range(7):
    print("=== Processing year %d ===" % (year + 2010))
    csv_file = get_filehead(year)
    fs = pd.read_csv(csv_file)
    size = len(fs)
    for pk in packages:
        print(pk)
        internal_index = pk.get_interior_index(year)
        params = [year + 2010, pk.id, pk.name, internal_index]
        fine = False
        for i in range(size):
            itm = fs.iloc[i]
            if itm['GEO.display-label'].replace(' County', '').replace(' city', '') == pk.name.replace(' (city)', ''):
                for p in target_params:
                    try:
                        params.append(itm[p])
                    except:
                        params.append('0')
                fine = True
                break
        if not fine:
            for p in target_params:
                params.append(0)
                input("No data found for #%d %s." % (pk.id, pk.name))
        print(params)
        results.append(params)

savefilename = input("Save it to [where].csv... \n>>> ")

if savefilename == "":
    savefilename = "weight"

savefilename += '.csv'

with open(savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(
        ["Year", "ID", "Name", "InnerIndex"] + target_params)
    spamwriter.writerow(
        ["Year", "ID", "Name", "InnerIndex"] + result)
    for row in results:
        spamwriter.writerow(row)
