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

print("Successfully opened %s packages." % len(pkgs))


csvfilename = input("Input [weight].csv... \n>>> ")

weight_csv = pd.read_csv(csvfilename)

packages = []
for i in pkgs:
    packages.append(i[1])

for index in range(451):
    pass
