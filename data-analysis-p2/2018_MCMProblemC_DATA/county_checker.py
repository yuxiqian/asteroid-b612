#!/usr/bin/env python

import pickle
import numpy as np
import pandas as pd
import seaborn as sns


from drug import drug_list
from abbr import abbr_to_full
from utils import find_county
from structor import County, Record

readfilename = input("Input [filename].loc... \n>>> ")
rq = []

if readfilename == "":
    readfilename = "cnt_db"

with open("%s.loc" % readfilename, 'rb') as file:
    rq = pickle.loads(file.read())


if type(rq) != list:
    raise TypeError("Bad File Format")

print("Successfully get %d items." % len(rq))

for ct in rq:
    print(" - %s, %s" % (ct.literal_name, ct.state))
