#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_legislative_summaries

# This is the initial call...no parameters
results = fetch_legislative_summaries.process()
result_count = results.get('resultCount')
print(f'Found {result_count} legislative bills')
helpers.write_json_file('legislative_summaries.json', results)

"""
Need to parse out the resultCount from this response...
This is neede to build out the remaining calls
  * recordCount is part of the derived URL
  * Used to determine the last page to fetch
    * Logic to get last page: math.ceil(recordCount/20)

2100 / 20 = 105 pages to fetch summary details from
"""

# This is the second call...
# derived_url = 'https://www.legis.ga.gov/search?s=1029&p=2&rc=2100'
# results = fetch_legislative_summaries.process(derived_url)
# helpers.write_json_file('legislative_summaries_2.json', results)

# This is the third call...
# derived_url = 'https://www.legis.ga.gov/search?s=1029&p=3&rc=2100'
# results = fetch_legislative_summaries.process(derived_url)
# helpers.write_json_file('legislative_summaries_3.json', results)

# This is the final call...
# derived_url = 'https://www.legis.ga.gov/search?s=1029&p=105&rc=2100'
# results = fetch_legislative_summaries.process(derived_url)
# helpers.write_json_file('legislative_summaries_105.json', results)

"""
The pattern for the derived_urls is:
  * s = current session (constants.CURRENT_SESSION)
  * p = page to fetch - for session 1029 it's: 2 - 105
  * rc = resultCount pulled from inital call
"""
