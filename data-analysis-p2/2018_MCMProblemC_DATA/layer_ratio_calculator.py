#!/usr/bin/env python

import csv
import pickle
import numpy as np
import pandas as pd
from math import log, e
from pack import Pack


readfilename = input("Input [filename].csv... \n>>> ")
packages = []

if readfilename == "":
    readfilename = "fit_xs"


description = ['Family * a + Education',
               'Education * b + Culture', 'Family * c + Culture']

words = ['a', 'b', 'c']


weight_csv = pd.read_csv(readfilename + ".csv")
length = len(weight_csv)

print("Successfully parsed %d items in csv file." % length)

Index_a = 0.0
Index_b = 0.0
Index_c = 0.0

total_weight = 0.0

for index in range(length):
    loc_x = weight_csv.iloc[index]
    weight = int(loc_x['Weight'])
    total_weight += weight
    type = int(loc_x['Type'])
    if type == 0:
        Index_a += float(loc_x['x value']) * weight
    elif type == 1:
        Index_b += float(loc_x['x value']) * weight
    else:
        Index_c += float(loc_x['x value']) * weight


total_weight /= 3.0

Index_a /= total_weight
Index_b /= total_weight
Index_c /= total_weight

result = [Index_a, Index_b, Index_c]

for i in range(3):
    print("""
Result:
    [%s]::%s = %.5f

""" % (description[i], words[i], result[i]))
