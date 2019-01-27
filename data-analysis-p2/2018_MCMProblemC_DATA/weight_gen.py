#!/usr/bin/env python

import csv
import pickle
import numpy as np
import pandas as pd
from pack import Pack

target_params_before = ['HC01_VC25', 'HC01_VC04',
                        'HC01_VC37', 'HC01_VC37', 'HC01_VC85', 'HC01_VC80', 'HC01_VC144',
                        'HC01_VC118']

target_params_after = ['HC01_VC26', 'HC01_VC04',
                       'HC01_VC38', 'HC01_VC45', 'HC01_VC86', 'HC01_VC81', 'HC01_VC146',
                       'HC01_VC120']

result = ['Weight', 'Families',
          'Happy Marriage Men', 'Happy Marriage Women', 'Drop out ones of school before Grade 9', 'College School Students', 'Born Outside people', 'The Settled'
          ]


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

counties_dat = [[]] * 451

results = []

for year in range(7):
    print("=== Processing year %d ===" % (year + 2010))
    csv_file = get_filehead(year)
    fs = pd.read_csv(csv_file)
    size = len(fs)
    for pk in packages:
        if counties_dat[pk.id] == []:
            counties_dat[pk.id] = [pk.name, pk, [[]] * 7]

        print(pk)
        internal_index = pk.get_interior_index(year)
        params = [year + 2010, pk.id, pk.name, internal_index]
        fine = False
        for i in range(size):
            itm = fs.iloc[i]
            if itm['GEO.display-label'].replace(' County', '').replace(' city', '') == pk.name.replace(' (city)', ''):
                if year < 3:
                    prm = target_params_before
                else:
                    prm = target_params_after
                for p in prm:
                    try:
                        params.append(itm[p])
                    except:
                        params.append('0')
                fine = True
                break
        if not fine:
            for p in prm:
                params.append(0)
                input("No data found for #%d %s." % (pk.id, pk.name))
        print(params)
        results.append(params)
        counties_dat[pk.id][2][year] = params[4:]


input()

for dat in counties_dat:
    # 八件
    dat[2][0][0] = int(dat[2][0][0])
    weight = dat[2][0][0]
    for j in range(1, 8):
        # 七年
        nums = []
        for i in range(7):
            nums.append(int(dat[2][i][j]))
        print(nums)
        # input()
        avg = np.mean(nums)
        for i in range(7):
            if not i in [4, 6]:
                dat[2][i][j] = nums[i] / avg
            else:
                dat[2][i][j] = 2.0 - nums[i] / avg
    print("标准化了： %s" % dat[2])


savefilename = input("Save csv file to [where].csv... \n>>> ")

if savefilename == "":
    savefilename = "weight"

savefilename += '.csv'

with open(savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)

    spamwriter.writerow(
        ["Year", "ID", "Name", "InnerIndex"] + result)
    for row in results:
        spamwriter.writerow(row)


savebinaryfile = input("Save binary file to [where].bf... \n>>> ")
if savebinaryfile == "":
    savebinaryfile = "awesome"
output_hal = open("%s.bf" % savebinaryfile, 'wb')

str_data = pickle.dumps(counties_dat)
output_hal.write(str_data)
output_hal.close()
