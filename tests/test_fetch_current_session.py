#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import unittest

from utils import constants
from workers import fetch_current_session


class FetchCurrentSessionTestCase(unittest.TestCase):

    def test_fetch_current_session(self):
        results = fetch_current_session.process()
        self.assertEqual(results, constants.CURRENT_SESSION)
