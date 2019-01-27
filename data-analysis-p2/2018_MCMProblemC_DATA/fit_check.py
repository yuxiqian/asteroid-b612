import csv
import pickle
import subprocess
import numpy as np
import pandas as pd

from pack import Pack
from copy import deepcopy
from math import sqrt, inf


def get_blocks(lst):
    family = []
    education = []
    culture = []
    for i in lst:
        # print(i)
        family.append(sqrt(pow(i[1], 2) * pow((i[2] + i[3]) / 2, 2)))
        education.append(sqrt(pow(i[4], 2) * pow(i[5], 2)))
        culture.append(sqrt(pow(i[6], 2) * pow(i[7], 2)))
    return family, education, culture


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


description = ['Family * x + Education',
               'Education * x + Culture', 'Family * x + Culture']

mma_fitting_script = "FindFit[dt,Avg * E ^ Sin[p + t w]((C1 P1[[t]])/Log[1 + D1] + (C2 P2[[t]])/Log[1 + D2] + (C3  P3[[t]])/Log[1 + D3] + 1)*((Culture[[t]]/0.46556 + 2.28335*Family[[t]] + Education[[t]]))/(1/0.46556 + 2.28335 + 1), {p, w, C1, C2, C3}, t]"

readfilename = input("Input [awesome].bf... \n>>> ")
locs = []

if readfilename == "":
    readfilename = "awesome"

with open("%s.bf" % readfilename, 'rb') as file:
    pkgs = pickle.loads(file.read())

flow_items = []

if type(pkgs) != list:
    raise TypeError("Bad File Format")

print("Successfully opened %d packages." % len(pkgs))


packages = []
for i in pkgs:
    packages.append(i[1])

for index in range(451):
    idx = pkgs[index]
    # print(idx)
    l = idx[1]

    family, education, culture = get_blocks(idx[2])

    init = packages[index].get_mma_script_for_phase_2(
        packages, family, education, culture)

    print(init)
    # input()

    txt = subprocess.check_output(
        ["wolframscript", "-code", init + mma_fitting_script]).decode('utf-8')

    txt = txt.split('\n')[-2].replace(' ', '')
    # print(txt)

    lst = txt.replace('\n', '').replace('{p->', '').replace(',w->',
                                                            ' ').replace(',C1->', ' ').replace(',C2->', ' ').replace(',C3->', ' ').replace(',C4->', ' ').replace(',C5->', ' ').replace('}', '').split(' ')
    print(lst)
    print()
    if len(lst) != 5:
        txt = input("Failed to dump %s." % txt)
        continue

    try:
        length = len(lst)
        l.p = float(lst[0].replace('*^', 'e'))
        l.w = float(lst[1].replace('*^', 'e'))
        l.affect_index_a = float(lst[2].replace('*^', 'e'))
        if length > 3:
            l.affect_index_b = float(lst[3].replace('*^', 'e'))
            if length > 4:
                l.affect_index_c = float(lst[4].replace('*^', 'e'))
                if length > 5:
                    l.affect_index_d = float(lst[5].replace('*^', 'e'))
                    if length > 6:
                        l.affect_index_e = float(lst[6].replace('*^', 'e'))
    except:
        print("Throwing data %s.\n\n" % lst)
        l.affect_index_a = 0.0
        l.affect_index_b = 0.0
        l.affect_index_c = 0.0
        l.affect_index_d = 0.0
        l.affect_index_e = 0.0
        # input()
        continue
    if l.affect_index_a == 1.0 or l.affect_index_b == 1.0 or l.affect_index_c == 1.0:
        print("Throwing data %s.\n\n" % lst)
        l.p = 0.0
        l.w = 0.0
        l.affect_index_a = 0.0
        l.affect_index_b = 0.0
        l.affect_index_c = 0.0
        l.affect_index_d = 0.0
        l.affect_index_e = 0.0
        # input()


savefilename = input("Save it to [where].ans... \n>>> ")
if savefilename == "":
    savefilename = "awesome - improved"
output_hal = open("%s.ans" % savefilename, 'wb')

str_data = pickle.dumps(packages)
output_hal.write(str_data)
output_hal.close()
