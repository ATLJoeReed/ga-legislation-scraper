#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_legislative_details


legislative_ids = [
    '58786',
    '58787',
    '58788',
    '58789',
    '58790',
    '58791',
    '58792',
    '58793',
    '58794',
    '58795',
]

results = fetch_legislative_details.process(legislative_ids)
helpers.write_json_file('legislative_details.json', results)

# Busting out each legislative bills html and parsing it to text
# and putting in json file and writing out.
for r in results:
    document_json = {}
    results_values = list(r.values())
    # bill details are stored in first element
    details = results_values[0]
    legislative_id = details.get('id')
    legislative_title = details.get('title')
    # html is stored in the second elememt of the dictionary...
    document = results_values[1]
    # We need to get the array of pages into a single html stream...
    html = ''
    for d in document:
        html += d
    document_text = helpers.extract_text_from_html(html)
    document_json['legislative_id'] = legislative_id
    document_json['legislative_title'] = legislative_title
    document_json['document_text'] = document_text
    helpers.write_json_file(f'legislation_{legislative_id}_document_text.json', document_json) # noqa
