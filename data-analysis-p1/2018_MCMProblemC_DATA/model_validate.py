#!/usr/bin/env python

import csv
import pickle
import numpy as np
import pandas as pd
from math import sqrt, e, log, sin
from pack import Pack
from utils import find_county_index

readfilename = input("Input [datagrab].ans... \n>>> ")
locs = []

if readfilename == "":
    readfilename = "datagrab"

with open("%s.ans" % readfilename, 'rb') as file:
    locs = pickle.loads(file.read())

real_dats = []
estm_dats = []

if type(locs) != list:
    raise TypeError("Bad File Format")

print("Successfully opened %s packages." % len(locs))

# 使用模型估计 2016、2017 年的数据

# 以便检查模型状态


def estm(t, avg, p, w, C1, C2, C3, P1, P2, P3, D1, D2, D3):
    # print(t, avg, p, w, C1, C2, C3, P1, P2, P3, D1, D2, D3)
    return int(avg * pow(e, sin(p + t * w)) * (1 + C1 * P1 / log(1 + D1) + C2 * P2 / log(1 + D2) + C3 * P3 / log(1 + D3)))


for i in locs:
    print(i)

    loc_x = i.x
    loc_y = i.y

    calc_history = []

    dist = i.get_distance(locs)

    avg = np.mean(i.history)

    for year in range(8):
        calc_history.append(
            estm(year, avg, i.p, i.w,
                 i.affect_index_a, i.affect_index_b, i.affect_index_c,
                 locs[i.nearest_id[0]].history[year],
                 locs[i.nearest_id[1]].history[year],
                 locs[i.nearest_id[2]].history[year],
                 dist[0], dist[1], dist[2]))

    i.estm_history = calc_history

    for year in range(8):
        print("%d Real: %d\t%d Estm: %d" %
              (2010 + year, i.history[year], 2010 + year, i.estm_history[year]))
        real_dats.append([year, loc_x, loc_y, i.history[year]])
        estm_dats.append([year, loc_x, loc_y, i.estm_history[year]])
    # input()
    print()


savefilename = input("Save raw objects to [where].obj... \n>>> ")
output_hal = open("%s.obj" % savefilename, 'wb')

str_data = pickle.dumps(locs)
output_hal.write(str_data)
output_hal.close()


savefilename = input("Save it to [where].csv... \n>>> ")

saverealfilename = savefilename + '_real.csv'

saveestmfilename = savefilename + '_estm.csv'

with open(saverealfilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(
        ["year", "loc_x", "loc_y", "real_count"])
    for row in real_dats:
        spamwriter.writerow(row)

with open(saveestmfilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(
        ["year", "loc_x", "loc_y", "estm_count"])
    for row in estm_dats:
        spamwriter.writerow(row)
