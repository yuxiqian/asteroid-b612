#!/usr/bin/env python


def find_county(name, lib):
    for ct in lib:
        if name in ct.literal_name:
            return ct
        # print("%s != %s" % (name, ct.literal_name))
    return None
