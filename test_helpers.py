#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

from playwright.sync_api import sync_playwright

from utils import helpers


logger = helpers.setup_logger_stdout('legislative_scraper')

logger.info('Getting playwright object')
playwright = sync_playwright().start()

logger.info('Starting chromium browswer')
browser = playwright.chromium.launch()

# Get current session...
current_session = helpers.get_current_session(browser.new_context(), logger)
logger.info(f'Current session id: {current_session}')
params = {'current_session': current_session}

# Get committees...
committees = helpers.get_committees(browser.new_context(), params, logger)
logger.info(f'Found {len(committees)} committees')

# Get Representatives...
representatives = helpers.get_legistative_members(
    browser.new_context(),
    params,
    'representatives',
    logger
)
logger.info(f'Found {len(representatives)} Representatives')

# Get Senators...
representatives = helpers.get_legistative_members(
    browser.new_context(),
    params,
    'senators',
    logger
)
logger.info(f'Found {len(representatives)} Senators')

# Get all legislations...
# Need to put some thought into this to see how to do this quickly.
# For 2021 session we have 2100 items which is 105 calls to fetch.


logger.info('Starting legislation detail extract')

params['legislation_id'] = '58786'

# Get Legislation details...
legislation_details = helpers.get_legislation_details(
    browser.new_context(),
    params,
    logger
)
# clogger.info(legislation_details)

logger.info('Ending legislation detail extract')


logger.info('Cleanup playwright and browser objects')
browser.close()
playwright.stop()
