#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from workers import fetch_current_session


results = fetch_current_session.process()
print(results)
