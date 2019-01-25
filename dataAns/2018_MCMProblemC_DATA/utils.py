#!/usr/bin/env python


def find_county(name, lib):
    for ct in lib:
        if name.lower().split(' ')[0] in ct.literal_name.lower():
            return ct
        # print("%s not in %s" % (name.lower(), ct.literal_name.lower()))
    return None
