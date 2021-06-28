#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
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
print(len(results))
