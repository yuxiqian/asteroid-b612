#!/usr/bin/env python

import numpy as np
from math import sqrt, e, sin


class Pack:
    id = 0
    name = ""
    x = 0.0
    y = 0.0
    nearest_id = []
    history = []
    estm_history = []
    w = 0.0
    p = 0.0
    affect_index_a = 0.0
    affect_index_b = 0.0
    affect_index_c = 0.0
    affect_index_d = 0.0
    affect_index_e = 0.0

    def get_interior_index(self, t):
        return np.mean(self.history) * pow(e, sin(self.p + t * self.w))

    def get_distance(self, lib):
        dists = []
        for i in self.nearest_id:
            dists.append(
                sqrt((self.x - lib[i].x) ** 2 + (self.y - lib[i].y) ** 2))
        return dists

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
        w = %.4f, p = %.4f, affect_index = %.4f, %.4f, %.4f
        """ % (self.id, self.name, self.x, self.y, self.nearest_id, self.w, self.p, self.affect_index_a, self.affect_index_b, self.affect_index_c)

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

    def get_mma_script(self, lib):
        result = ""
        result += ("Avg = %d\n" % (int(np.mean(self.history))))

        result += ("dt = {%s}\n" % (', '.join(str(v) for v in self.history)))

        count = 1
        for i in self.nearest_id:
            result += ("D%d = %.4f\n" % (count,
                                         sqrt((self.x - lib[i].x) ** 2 + (self.y - lib[i].y) ** 2)))
            count += 1

        count = 1
        for i in self.nearest_id:
            result += ("P%d = {%s}\n" % (count, ', '.join(str(v)
                                                          for v in lib[i].history)))

            count += 1

        return result

    def print_for_fitting(self, lib):

        print("Avg = %d" % (int(np.mean(self.history))))

        print("dt = {%s}" % (', '.join(str(v) for v in self.history)))

        count = 1
        for i in self.nearest_id:
            print("D%d = %.4f" % (count,
                                  sqrt((self.x - lib[i].x) ** 2 + (self.y - lib[i].y) ** 2)))
            count += 1

        count = 1
        for i in self.nearest_id:
            print("P%d = {%s}" % (count, ', '.join(str(v)
                                                   for v in lib[i].history)))

            count += 1
