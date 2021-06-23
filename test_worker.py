#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from workers import fetch_legislative_details


urls = [
    'https://www.legis.ga.gov/legislation/58786',
    'https://www.legis.ga.gov/legislation/58787',
    'https://www.legis.ga.gov/legislation/58788',
    'https://www.legis.ga.gov/legislation/58789',
    'https://www.legis.ga.gov/legislation/58790',
    'https://www.legis.ga.gov/legislation/58791',
    'https://www.legis.ga.gov/legislation/58792',
    'https://www.legis.ga.gov/legislation/58793',
    'https://www.legis.ga.gov/legislation/58794',
    'https://www.legis.ga.gov/legislation/58795',
]

results = fetch_legislative_details.process(urls)
print(len(results))
