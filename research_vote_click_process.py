#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright

from utils import helpers


def extract_json(response):
    if 'legis.ga.gov/api' in response.url:
        print("<<", response.status, response.url)


logger = helpers.setup_logger_stdout('legislative_scraper')

logger.info('Getting playwright object')
playwright = sync_playwright().start()

logger.info('Starting chromium browswer')
browser = playwright.chromium.launch()

url = 'https://www.legis.ga.gov/votes/house'

page = browser.new_page()

page.goto(url, wait_until="networkidle")

page.on("response", extract_json)
# with page.expect_event("dialog") as popup_info:
with page.expect_response('https://www.legis.ga.gov/api/Vote/detail/18348') as word:
    page.click(':is(button:has-text(" 162 "))')

browser.close()
