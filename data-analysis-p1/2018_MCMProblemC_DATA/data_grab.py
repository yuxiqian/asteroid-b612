#!/usr/bin/env python


import heapq
import pickle
import numpy as np
import pandas as pd
from copy import deepcopy
from math import sqrt, inf


def set_history_data(lib, name, year, count):
    year_id = int(year) - 2010
    for loc in lib:
        if loc.name == name:
            loc.history[year_id] = count
            return
    raise TypeError("Nothing suitable found for %s, %d" % (name, year))


class Pack:
    id = 0
    name = ""
    x = 0.0
    y = 0.0
    nearest_id = []
    history = []

    def __init__(self, id, x, y, name, nearest_id=[]):
        self.x = x
        self.y = y
        self.id = id
        self.name = name
        self.nearest_id = nearest_id
        self.history = [0] * 8

    def __str__(self):
        return """ #%d
        City [%s] at [%.4f, %.4f]
        Nearest to: %s
        """ % (self.id, self.name, self.x, self.y, self.nearest_id)

    def print(self, lib):
        print(""" #%d
        City [%s] at [%.4f, %.4f]
        History: %s
              """ % (self.id, self.name, self.x, self.y, ' -> '.join(str(v) for v in self.history)))

        for i in self.nearest_id:
            dist = sqrt((self.x - lib[i].x) ** 2 + (self.y - lib[i].y) ** 2)

            print("""
                Closest to: #%d, City [%s] at [%.4f, %.4f], distance = %.3f
                History: %s
            """ % (i, lib[i].name, lib[i].x, lib[i].y, dist, ' -> '.join(str(v) for v in lib[i].history)))

    def print_for_fitting(self, lib):
        sum_history = deepcopy(self.history)
        for i in range(len(sum_history) - 1):
            sum_history[i + 1] += sum_history[i]
        print("""
SumHis_%d = {%s}
              """ % (self.id, ', '.join(str(v) for v in sum_history)))
        return
        for i in self.nearest_id:
            dist = sqrt((self.x - lib[i].x) ** 2 + (self.y - lib[i].y) ** 2)

            print("""
                Closest to: #%d, City [%s] at [%.4f, %.4f], distance = %.3f
                History: %s
            """ % (i, lib[i].name, lib[i].x, lib[i].y, dist, ', '.join(str(v) for v in lib[i].history)))


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
    it.nearest_id = np.argpartition(np.array(distances), target_k)[:target_k]

for l in packages:
    l.print_for_fitting(packages)
