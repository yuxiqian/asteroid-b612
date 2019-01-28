#!/usr/bin/env python

import csv
import pickle
import numpy as np
import pandas as pd
from math import sqrt, e, log, sin
from pack import Pack
from utils import find_county_index


def get_blocks(lst):
    family = []
    education = []
    culture = []
    for i in lst:
        # print(i)
        family.append(sqrt(pow(i[1], 2) * pow((i[2] + i[3]) / 2.0, 2)))
        education.append(sqrt(pow(i[4], 2) * pow(i[5], 2)))
        culture.append(sqrt(pow(i[6], 2) * pow(i[7], 2)))
    return family, education, culture


readfilename = input("Input [datagrab].ans... \n>>> ")
locs = []

if readfilename == "":
    readfilename = "awesome - improved"

with open("%s.ans" % readfilename, 'rb') as file:
    locs = pickle.loads(file.read())

real_dats = []
estm_dats = []
biases = []

if type(locs) != list:
    raise TypeError("Bad File Format")

print("Successfully opened %s ans." % len(locs))


readfilename = input("Input [awesome].bf... \n>>> ")
pkgs = []

if readfilename == "":
    readfilename = "awesome"

with open("%s.bf" % readfilename, 'rb') as file:
    pkgs = pickle.loads(file.read())

flow_items = []

if type(pkgs) != list:
    raise TypeError("Bad File Format")

print("Successfully opened %d bfs." % len(pkgs))


# 使用模型估计 2016、2017 年的数据

# 以便检查模型状态


def estmt(t, avg, p, w, C1, C2, C3, P1, P2, P3, D1, D2, D3, F, E, C):
    # print(t, avg, p, w, C1, C2, C3, P1, P2, P3, D1, D2, D3)
    return avg * pow(e, sin(p + t * w)) * (1 + C1 * P1 / log(1 + D1) + C2 * P2 / log(1 + D2) + C3 * P3 / log(1 + D3)) * (3.124 * F + 1.711 * E + C) / (3.124 + 1.711 + 1)


a_s = []
b_s = []
c_s = []


for i in locs:
    a_s.append(i.affect_index_a)
    b_s.append(i.affect_index_b)
    c_s.append(i.affect_index_c)


input()

a_arr = np.array(a_s)
b_arr = np.array(b_s)
c_arr = np.array(c_s)


print("A 方差 = %f" % np.var(a_arr))
print("B 方差 = %f" % np.var(b_arr))
print("C 方差 = %f" % np.var(c_arr))


input("Press <Enter> to calculate the bias >>> ")

id = 0

for i in locs:

    print(i)

    name = i.name

    loc_x = i.x
    loc_y = i.y

    calc_history = []

    dist = i.get_distance(locs)

    avg = np.mean(i.history)

    Family, Education, Culture = get_blocks(pkgs[id][2])
    print(Family)
    print(Education)
    print(Culture)
    # input()
    for year in range(7):
        calc_history.append(
            estmt(year, avg, i.p, i.w,
                  i.affect_index_a, i.affect_index_b, i.affect_index_c,
                  locs[i.nearest_id[0]].history[year],
                  locs[i.nearest_id[1]].history[year],
                  locs[i.nearest_id[2]].history[year],
                  dist[0], dist[1], dist[2], Family[year], Education[year], Culture[year]))

    i.estm_history = calc_history

    bias = 0.0
    for year in range(7):
        real = i.history[year]
        estm = i.estm_history[year]
        print("%d Real: %d\t%d Estm: %d" %
              (2010 + year, real, 2010 + year, estm))
        real_dats.append([year, loc_x, loc_y, real])
        estm_dats.append([year, loc_x, loc_y, estm])
        bias += (real - estm) ** 2
    # input()

    biases.append([id, name, bias])

    id += 1


savefilename = input("Save raw objects to [where].obj... \n>>> ")
output_hal = open("%s.obj" % savefilename, 'wb')

str_data = pickle.dumps(locs)
output_hal.write(str_data)
output_hal.close()


savefilename = input("Save bias analysis to [where].csv... \n>>> ")
with open(savefilename + " - bias.csv", 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(
        ["id", "name", "bias"])
    for row in biases:
        spamwriter.writerow(row)


savefilename = input("Save original data to [where].csv... \n>>> ")

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
