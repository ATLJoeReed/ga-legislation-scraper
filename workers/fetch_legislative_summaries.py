#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio
import os

from playwright.async_api import async_playwright

from utils import helpers


async def get_current_session(browser, logger, derived_url):
    url, intercept_routes = helpers.get_url_intercept_routes('legislative_summaries', logger) # noqa
    if derived_url:
        url = derived_url
    logger.info('Intercepting session route')
    context = await browser.new_context()
    results = await helpers.intercept_api_calls(context, url, intercept_routes)
    return helpers.extract_first_item(results, 'summaries', logger)


async def main(logger, derived_url):
    async with async_playwright() as playright:
        browser = await playright.chromium.launch()
        results = await get_current_session(browser, logger, derived_url)
    return results


def process(derived_url=None):
    logger = helpers.setup_logger_stdout(os.path.basename(__file__))
    logger.info('<<Starting to fetch legislative summaries>>')
    results = asyncio.run(main(logger, derived_url))
    logger.info('<<Ending fetching legislative summaries>>')
    return results
