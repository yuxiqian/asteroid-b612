#!/usr/bin/env python

import pickle
import pandas as pd

from structor import County

loc_data = pd.read_csv('locations.csv')

target_states = ['Ohio', 'Kentucky', 'West Virginia', 'Virginia', 'Tennessee']

order_count = len(loc_data)

counties = []

for loc_item in range(order_count):
    it = loc_data.iloc[loc_item]
    if it['state_name'] in target_states:
        it_ct = County(it['city_ascii'], it['state_name'],
                       it['lat'], it['lng'], it['density'])
        print(it_ct)
        counties.append(it_ct)


savefilename = input("Save it to [where].pkl... \n>>> ")
output_hal = open("%s.pkl" % savefilename, 'wb')

str_data = pickle.dumps(counties)
output_hal.write(str_data)
output_hal.close()
