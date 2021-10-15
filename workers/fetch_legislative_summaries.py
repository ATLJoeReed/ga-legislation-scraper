#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio
import os

from playwright.async_api import async_playwright

from utils import helpers


async def get_current_session(browser, derived_url, session, logger):
    url, intercept_routes = helpers.get_url_intercept_routes('legislative_summaries', logger) # noqa
    if session:
        url = f'https://www.legis.ga.gov/search?s={session}&p=1'
        logger.info(f'URL adjusted to {url}') 
    if derived_url:
        url = derived_url
        logger.info(f'URL adjusted to {url}') 
    logger.info('Intercepting session route')
    context = await browser.new_context()
    results = await helpers.intercept_api_calls(context, url, intercept_routes)
    return helpers.extract_first_item(results, 'summaries', logger)


async def main(derived_url, session, logger):
    async with async_playwright() as playright:
        browser = await playright.chromium.launch()
        results = await get_current_session(browser, derived_url, session, logger)
    return results


def process(derived_url=None, session=None):
    logger = helpers.setup_logger_stdout(os.path.basename(__file__))
    logger.info('<<Starting to fetch legislative summaries>>')
    results = asyncio.run(main(derived_url, session, logger))
    logger.info('<<Ending fetching legislative summaries>>')
    return results
