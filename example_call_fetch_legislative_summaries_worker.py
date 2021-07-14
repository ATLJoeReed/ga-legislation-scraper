#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_legislative_summaries

# This is the initial call...
results = fetch_legislative_summaries.process()
helpers.write_json_file('legislative_summaries.json', results)
# Need to parse out the resultCount from this response...
# This is neede to build out the remaining calls...
