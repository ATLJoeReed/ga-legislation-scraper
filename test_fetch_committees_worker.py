#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from workers import fetch_committees


results = fetch_committees.process()
print(results)
