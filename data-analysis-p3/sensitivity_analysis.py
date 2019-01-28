#!/usr/bin/env python

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


def estmt(t, avg, p, w, C1, C2, C3, P1, P2, P3, D1, D2, D3, F, E, C, alpha=0.16017, beta=0.31820, gamma=0.52163):
    # print(t, avg, p, w, C1, C2, C3, P1, P2, P3, D1, D2, D3)
    # alpha_dft = 0.16017
    # beta_dft = 0.31820
    # gamma_dft = 0.52163
    sum = 1.0
    return avg * pow(e, sin(p + t * w)) * (1 + C1 * P1 / log(1 + D1) + C2 * P2 / log(1 + D2) + C3 * P3 / log(1 + D3)) * (alpha * F + beta * E + gamma * C) / sum


id = 0

alpha_dft = 0.16017
beta_dft = 0.31820
gamma_dft = 0.52163

sensitive_check = []

i = locs[9]

try:
    print(i)

    name = i.name

    loc_x = i.x
    loc_y = i.y

    dist = i.get_distance(locs)

    avg = np.mean(i.history)

    Family, Education, Culture = get_blocks(pkgs[id][2])
    # print(Family)
    # print(Education)
    # print(Culture)
    # input()
    for year in range(7):
        sensitive_check.append([])
        sensitive_check[-1].append(
            estmt(year, avg, i.p, i.w,
                  i.affect_index_a, i.affect_index_b, i.affect_index_c,
                  locs[i.nearest_id[0]].history[year],
                  locs[i.nearest_id[1]].history[year],
                  locs[i.nearest_id[2]].history[year],
                  dist[0], dist[1], dist[2], Family[year], Education[year], Culture[year]))

        sensitive_check[-1].append(
            estmt(year, avg, i.p, i.w,
                  i.affect_index_a, i.affect_index_b, i.affect_index_c,
                  locs[i.nearest_id[0]].history[year],
                  locs[i.nearest_id[1]].history[year],
                  locs[i.nearest_id[2]].history[year],
                  dist[0], dist[1], dist[2], Family[year], Education[year], Culture[year], alpha=alpha_dft * 0.9))

        sensitive_check[-1].append(
            estmt(year, avg, i.p, i.w,
                  i.affect_index_a, i.affect_index_b, i.affect_index_c,
                  locs[i.nearest_id[0]].history[year],
                  locs[i.nearest_id[1]].history[year],
                  locs[i.nearest_id[2]].history[year],
                  dist[0], dist[1], dist[2], Family[year], Education[year], Culture[year], alpha=alpha_dft * 1.1))

        sensitive_check[-1].append(
            estmt(year, avg, i.p, i.w,
                  i.affect_index_a, i.affect_index_b, i.affect_index_c,
                  locs[i.nearest_id[0]].history[year],
                  locs[i.nearest_id[1]].history[year],
                  locs[i.nearest_id[2]].history[year],
                  dist[0], dist[1], dist[2], Family[year], Education[year], Culture[year], beta=beta_dft * 0.9))

        sensitive_check[-1].append(
            estmt(year, avg, i.p, i.w,
                  i.affect_index_a, i.affect_index_b, i.affect_index_c,
                  locs[i.nearest_id[0]].history[year],
                  locs[i.nearest_id[1]].history[year],
                  locs[i.nearest_id[2]].history[year],
                  dist[0], dist[1], dist[2], Family[year], Education[year], Culture[year], beta=beta_dft * 1.1))

        sensitive_check[-1].append(
            estmt(year, avg, i.p, i.w,
                  i.affect_index_a, i.affect_index_b, i.affect_index_c,
                  locs[i.nearest_id[0]].history[year],
                  locs[i.nearest_id[1]].history[year],
                  locs[i.nearest_id[2]].history[year],
                  dist[0], dist[1], dist[2], Family[year], Education[year], Culture[year], gamma=gamma_dft * 0.9))

        sensitive_check[-1].append(
            estmt(year, avg, i.p, i.w,
                  i.affect_index_a, i.affect_index_b, i.affect_index_c,
                  locs[i.nearest_id[0]].history[year],
                  locs[i.nearest_id[1]].history[year],
                  locs[i.nearest_id[2]].history[year],
                  dist[0], dist[1], dist[2], Family[year], Education[year], Culture[year], gamma=gamma_dft * 1.1))

    print(sensitive_check)
    input()

    id += 1

    # input()

except:
    pass


savefilename = input("Save sensitivity analysis to [where].csv... \n>>> ")
with open(savefilename + " - sense.csv", 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(
        ["year", "real", "90% a", "110% a", "90% b", "110% b", "90% c", "110% c", ])
    count = 2010
    for row in sensitive_check:
        spamwriter.writerow([count] + row)
        count += 1
