#!/usr/bin/env python


def find_county(name, lib, state=None):
    for ct in lib:
        if state != None:
            if not state.lower() in ct.state.lower():
                # print("%s not in %s" %
                #       (state.lower(), ct.state.lower()))
                continue

        if name.lower().split(' ')[0] in ct.literal_name.lower():
            return ct

    return None


def find_county_index(name, lib):
    for i in range(len(lib)):
        if name.lower().split(' ')[0] in lib[i].literal_name.lower():
            return i
        # print("%s not in %s" % (name.lower(), ct.literal_name.lower()))
    return None
