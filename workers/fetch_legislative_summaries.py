#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio
import os

from playwright.async_api import async_playwright

from utils import helpers


async def get_current_session(browser, logger, url_intercept_routes):
    if not url_intercept_routes:
        url, intercept_routes = helpers.get_url_intercept_routes('legislative_summaries', logger) # noqa
    else:
        url, intercept_routes = url_intercept_routes
    logger.info('Intercepting session route')
    context = await browser.new_context()
    results = await helpers.intercept_api_calls(context, url, intercept_routes)
    return helpers.extract_first_item(results, 'summaries', logger)


async def main(logger, url_intercept_routes):
    async with async_playwright() as playright:
        browser = await playright.chromium.launch()
        results = await get_current_session(browser, logger, url_intercept_routes)
    return results


def process(url_intercept_routes=None):
    logger = helpers.setup_logger_stdout(os.path.basename(__file__))
    logger.info('<<Starting to fetch legislative summaries>>')
    results = asyncio.run(main(logger, url_intercept_routes))
    logger.info('<<Ending fetching legislative summaries>>')
    return results
