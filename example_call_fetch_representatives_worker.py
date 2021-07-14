#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_representatives


results = fetch_representatives.process()
helpers.write_json_file('representatives.json', results)
