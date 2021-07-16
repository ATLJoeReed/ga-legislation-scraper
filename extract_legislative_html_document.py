#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from workers import fetch_legislative_details


legislative_ids = ['58786']

results = fetch_legislative_details.process(legislative_ids)
# helpers.write_json_file('legislative_details.json', results[0])

results_values = list(results[0].values())
document = results_values[1]

print(f'Length of document is {len(document)}')

for index, d in enumerate(document):
    file_name = f'research_{index}.html'
    with open(file_name, 'w') as f:
        f.write(d)

with open("document.html", "w") as f:
    for d in document:
        f.write(d)
