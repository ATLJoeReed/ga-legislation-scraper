#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import json
import os
import unittest

from workers import fetch_committees


class FetchCommitteesTestCase(unittest.TestCase):

    def test_fetch_committees(self):
        # TODO: Better pattern for loading these expected json results
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        with open('json_results/committees_27.json') as json_file:
            expected_json = json.load(json_file)
        results = fetch_committees.process(session=27)
        self.assertEqual(results, expected_json)
