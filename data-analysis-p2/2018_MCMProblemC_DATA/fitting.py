import csv
import pickle
import subprocess
import numpy as np
import pandas as pd

from pack import Pack
from copy import deepcopy
from math import sqrt, inf


class xval:
    x = 0.0
    weight = 0

    def __init__(self, x, w):
        self.x = x
        self.weight = w

    def __str__(self):
        return """
        x = %.4f, weight = %d
        """ % (self.x, self.weight)


param_dictionary = ['General Population', 'Families', 'Happy Marriage Men', 'Happy Marriage Women',
                    'Didn\'t Drop out ones of school before Grade 9', 'College School Students', 'Not Born Outside people', 'The Settled']

mma_fitting_script = ["FindFit[dt,Avg* E^Sin[p + t w] ((C1 P1[[t]])/Log[1 + D1] + (C2 P2[[t]])/Log[1 + D2] + (C3  P3[[t]])/Log[1 + D3] + 1)*(x Family[[t]] + Education[[t]]), {p, w, C1, C2, C3,x}, t]",
                      "FindFit[dt,Avg* E^Sin[p + t w] ((C1 P1[[t]])/Log[1 + D1] + (C2 P2[[t]])/Log[1 + D2] + (C3  P3[[t]])/Log[1 + D3] + 1)*(x Education[[t]] + Culture[[t]]), {p, w, C1, C2, C3,x}, t]",
                      "FindFit[dt,Avg* E^Sin[p + t w] ((C1 P1[[t]])/Log[1 + D1] + (C2 P2[[t]])/Log[1 + D2] + (C3  P3[[t]])/Log[1 + D3] + 1)*(x Family[[t]] + Culture[[t]]), {p, w,C1, C2, C3, x}, t]"
                      ]

description = ['Family * x + Education',
               'Education * x + Culture', 'Family * x + Culture']

x_values = [[], [], []]

readfilename = input("Input [model_alldrug].bf... \n>>> ")
locs = []

if readfilename == "":
    readfilename = "awesome"

with open("%s.bf" % readfilename, 'rb') as file:
    pkgs = pickle.loads(file.read())

flow_items = []

if type(pkgs) != list:
    raise TypeError("Bad File Format")

print("Successfully opened %s packages." % len(pkgs))

packages = []
for i in pkgs:
    packages.append(i[1])

for itm in pkgs:

    time_strip = []

    name = itm[0]
    l = itm[1]
    params = itm[2]

    l.print(packages)
    # l.print_for_fitting(packages)

    Family_Index = []
    Education_Index = []
    Culture_Index = []

    for year in range(7):
        # 七年
        Family_Index.append(sqrt(pow(params[year][1], 2) *
                                 pow((params[year][2] + params[year][3]) / 2.0, 2)))
        Education_Index.append(
            sqrt(pow(params[year][4], 2) * pow(params[year][5], 2)))

        Culture_Index.append(
            sqrt(pow(params[year][6], 2) * pow(params[year][7], 2)))

    for i in range(3):
        print(description[i])
        init = l.get_mma_script_for_phase_2(packages, Family_Index,
                                            Education_Index, Culture_Index)

        txt = subprocess.check_output(
            ["wolframscript", "-code", init + mma_fitting_script[i]]).decode('utf-8')
        # print(init + mma_fitting_script[i])
        # input()
        # print(txt)
        txt = txt.split('\n')[-2].replace(' ', '')
        # print(txt)

        lst = txt.replace('\n', '').replace('{p->', '').replace(',w->',
                                                                ' ').replace(',C1->', ' ').replace(',C2->', ' ').replace(',C3->', ' ').replace(',x->', ' ').replace('}', '').split(' ')
        print(lst)
        print()
        if len(lst) != 6:
            txt = input("Failed to dump %s." % txt)
            continue

        get_x = xval(float(lst[5]), int(params[0][0]))
        print(get_x)
        x_values[i].append(get_x)
        if l.affect_index_a == 1.0 or l.affect_index_b == 1.0 or l.affect_index_c == 1.0:
            print("Fitting %s results in a failure.\n\n" % lst)
            input()
        # input()


savefilename = input("Save csv file to [where].csv... \n>>> ")

if savefilename == "":
    savefilename = "fit_xs"

savefilename += '.csv'

with open(savefilename, 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)

    spamwriter.writerow(
        ["Type", "x value", "Weight"])
    for i in range(3):
        for x in x_values[i]:
            spamwriter.writerow([i, x.x, x.weight])
