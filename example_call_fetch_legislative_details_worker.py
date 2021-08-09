#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_legislative_details


legislative_ids = [
    '58911',
    '59252',

]

results = fetch_legislative_details.process(legislative_ids)
helpers.write_json_file('legislative_details.json', results)
