#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from utils import helpers
from workers import fetch_member_votes


votes = [
    (18348, 162, 'House Vote #162'),
]

results = fetch_member_votes.process(votes)
helpers.write_json_file('member_votes.json', results)
