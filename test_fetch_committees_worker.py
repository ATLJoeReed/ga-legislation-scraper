#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_committees


results = fetch_committees.process()
helpers.write_json_file('committees.json', results)
