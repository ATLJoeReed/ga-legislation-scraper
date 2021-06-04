#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

from playwright.sync_api import sync_playwright

from utils import helpers


playwright = sync_playwright().start()


# url = 'https://www.legis.ga.gov'
# intercept_routes = ['api/news/house', 'api/news/senate', 'api/sessions/currentDay'] # noqa

url = 'https://www.legis.ga.gov/legislation/all'
# intercept_routes = ['api/sessions', 'api/members/']
intercept_routes = ['api/Legislation/']

results = helpers.intercept_api_calls(playwright, url, intercept_routes)
# print(len(results.get('https://www.legis.ga.gov/api/Legislation/Search/20/0').get('results')))
print(results)

playwright.stop()
