#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_member_votes


votes = [
    (18348, 162, 'House Vote #162'),
    (18349, 163, 'House Vote #163'),
    (18604, 251, 'Senate Vote #251'),
]

results = fetch_member_votes.process(votes)
helpers.write_json_file('member_votes.json', results)
