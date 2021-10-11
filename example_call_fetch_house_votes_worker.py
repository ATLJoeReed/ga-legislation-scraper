#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_house_votes


results = fetch_house_votes.process()
helpers.write_json_file('house_votes.json', results)
