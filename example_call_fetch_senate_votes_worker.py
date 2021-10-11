#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_senate_votes


results = fetch_senate_votes.process()
helpers.write_json_file('senate_votes.json', results)
