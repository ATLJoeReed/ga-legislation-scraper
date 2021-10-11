#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import json
import os
import unittest

from workers import fetch_house_votes


class FetchHouseVotesTestCase(unittest.TestCase):

    def test_fetch_house_votes(self):
        # TODO: Better pattern for loading these expected json results
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        with open('json_results/house_votes_27.json') as json_file:
            expected_json = json.load(json_file)
        results = fetch_house_votes.process(session=27)
        self.assertEqual(results, expected_json)
