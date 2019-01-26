#!/usr/bin/env python


import heapq
import pickle
import subprocess
import numpy as np
import pandas as pd

from pack import Pack
from copy import deepcopy
from math import sqrt, inf


def set_history_data(lib, name, year, count):
    year_id = int(year) - 2010
    for loc in lib:
        if loc.name == name:
            loc.history[year_id] = count
            return
    raise TypeError("Nothing suitable found for %s, %d" % (name, year))


default_file = input(
    "Input the clean location csv file: [clean_locs].csv >>> ")

if default_file == "":
    default_file = 'clean_locs.csv'

dat = pd.read_csv(default_file)

length = len(dat)
print("Successfully read %d items." % length)


default_file = input(
    "Input the complete spread csv file: [spread - all.csv].csv >>> ")

if default_file == "":
    default_file = 'spread - all.csv'

spread_dat = pd.read_csv(default_file)

spread_len = len(spread_dat)
print("Successfully read %d items." % spread_len)

target_k = input("Input K as distance check limit: [3] >>> ")

if target_k != "":
    target_k = int(target_k)
else:
    target_k = 3

packages = []


for i in range(length):
    item = dat.iloc[i]
    packages.append(Pack(i, item['经度'], item['纬度'],
                         item['名称'].replace(', ', '/')))

for j in range(spread_len):
    item = spread_dat.iloc[j]
    set_history_data(packages, item['Name'], item['Year'], item['Amount'])

for it in packages:
    x_0 = it.x
    y_0 = it.y
    distances = []
    for item in packages:
        x = item.x
        y = item.y
        dist = sqrt((x - x_0) ** 2 + (y - y_0) ** 2)
        if dist == 0.0:
            dist = inf
        distances.append(dist)
    it.nearest_id = np.argpartition(np.array(distances), target_k)[: target_k]

for l in packages:
    l.print(packages)
    l.print_for_fitting(packages)

    init = l.get_mma_script(packages)

    txt = subprocess.check_output(["wolframscript", "-code", init + """
        FindFit[dt,
 Avg* E^Sin[
   p + t w] ((C1 P1[[t]])/Log[1 + D1] + (C2 P2[[t]])/Log[1 + D2] + (
    C3  P3[[t]])/Log[1 + D3]), {p, w, C1, C2, C3}, t]
    """]).decode('utf-8')

    txt = txt.split('\n')[-2].replace(' ', '')
    # print(txt)

    lst = txt.replace('\n', '').replace('{p->', '').replace(',w->',
                                                            ' ').replace(',C1->', ' ').replace(',C2->', ' ').replace(',C3->', ' ').replace('}', '').split(' ')
    print(lst)
    print()
    if len(lst) != 5:
        txt = input("Failed to dump %s." % txt)
        continue

    try:
        l.p = float(lst[0].replace('*^', 'e'))
        l.w = float(lst[1].replace('*^', 'e'))
        l.affect_index[0] = float(lst[2].replace('*^', 'e'))
        l.affect_index[1] = float(lst[3].replace('*^', 'e'))
        l.affect_index[2] = float(lst[4].replace('*^', 'e'))
    except:
        print("Throwing data %s.\n\n" % lst)
        l.affect_index = [0.0] * 3
        input()
        continue
    if l.affect_index[0] == 1.0:
        print("Throwing data %s.\n\n" % lst)
        l.p = 0.0
        l.w = 0.0
        l.affect_index = [0.0] * 3
        input()
        continue
    # input()

savefilename = input("Save it to [where].ans... \n>>> ")
if savefilename == "":
    savefilename = "awesome"
output_hal = open("%s.ans" % savefilename, 'wb')

str_data = pickle.dumps(packages)
output_hal.write(str_data)
output_hal.close()
