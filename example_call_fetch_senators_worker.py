#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_senators


results = fetch_senators.process()
helpers.write_json_file('senators.json', results)
