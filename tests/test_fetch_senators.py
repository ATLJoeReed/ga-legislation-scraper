#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import json
import os
import unittest

from workers import fetch_senators


class FetchSenatorsTestCase(unittest.TestCase):

    def test_fetch_senators(self):
        # TODO: Better pattern for loading these expected json results
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        with open('json_results/senators_session_27.json') as json_file:
            expected_json = json.load(json_file)
        results = fetch_senators.process(session=27)
        self.assertEqual(results, expected_json)
