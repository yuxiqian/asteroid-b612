#!/usr/bin/env python

from drug import drug_list


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
    year = 0
    substance_id = 0
    drug_report_count = 0
    county_drug_report_count = 0
    state_drug_report_count = 0

    def __init__(self, year, county, substance_id, drug_report_count, county_drug_report_count, state_drug_report_count):
        self.year = year
        self.county = county
        self.substance_id = substance_id
        self.drug_report_count = drug_report_count
        self.county_drug_report_count = county_drug_report_count
        self.state_drug_report_count = state_drug_report_count

    def __str__(self):
        return """
        In %s, %s, %d, Drug %s
        ==================
        Report, County Total, State Total
        %d, %d, %d
        """ % (self.county.literal_name, self.county.state, self.year, drug_list[self.substance_id], self.drug_report_count, self.county_drug_report_count, self.state_drug_report_count)
