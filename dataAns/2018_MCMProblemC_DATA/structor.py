#!/usr/bin/env python


state_dict = {

}


class County:
    literal_name = ""
    latitude = 0.0
    longitude = 0.0
    state_name = ""
    density = 0.0

    def __init__(self, literal_name, state_name, lat, lng, density):
        self.literal_name = literal_name
        self.state = state_name
        self.latitude = float(lat)
        self.longitude = float(lng)
        self.density = float(density)
        self.geo_data = [{}] * 8

    def __str__(self):
        return """
        County [%s] in State [%s]
        At [%.4f, %.4f]
        Density: %.2f
        """ % (self.literal_name, self.state, self.latitude, self.longitude, self.density)


class Record:
    county = None
    name = 0
    state_id = 0
    county_id = 0
