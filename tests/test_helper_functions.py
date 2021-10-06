#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import os
import unittest

from utils import helpers


class HelperFunctionsTestCase(unittest.TestCase):

    def setUp(self):
        self.logger = helpers.setup_logger_stdout(os.path.basename(__file__)) # noqa

    def test_get_url_interceptor_routes_committees(self):
        expected_url = 'https://www.legis.ga.gov/committees/house'
        expected_intercept_routes = ['/api/committees/List/{current_session}']
        url, intercept_routes = helpers.get_url_intercept_routes('committees', self.logger) # noqa
        self.assertEqual(url, expected_url)
        self.assertEqual(intercept_routes, expected_intercept_routes)

    def test_extract_first_item(self):
        test_object = {"first_item": [{"first_value": "some_value"}]}
        expected_results = [{"first_value": "some_value"}]
        results = helpers.extract_first_item(test_object, 'Test', self.logger)
        self.assertEqual(expected_results, results)
