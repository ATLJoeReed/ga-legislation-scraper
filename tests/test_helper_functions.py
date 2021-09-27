#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import unittest

from utils import helpers


class HelperFunctionsTestCase(unittest.TestCase):

    def test_get_url_interceptor_routes_committees(self):
        expected_url = 'https://www.legis.ga.gov/committees/house'
        expected_intercept_routes = ['/api/committees/List/{current_session}']
        url, intercept_routes = helpers.get_url_intercept_routes('committees', None) # noqa
        self.assertEqual(url, expected_url)
        self.assertEqual(intercept_routes, expected_intercept_routes)

    def test_extract_first_item(self):
        pass
