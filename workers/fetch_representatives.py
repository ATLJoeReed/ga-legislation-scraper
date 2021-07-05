#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio
import os

from playwright.async_api import async_playwright

from utils import constants, helpers


async def get_representatives(browser, logger):
    url, intercept_routes = helpers.get_url_intercept_routes('representatives', logger) # noqa
    params = {'current_session': constants.CURRENT_SESSION}
    adjusted_routes = helpers.update_list_item(intercept_routes, params, logger) # noqa
    logger.info('Intercepting representatives route')
    context = await browser.new_context()
    results = await helpers.intercept_api_calls(context, url, adjusted_routes)
    return helpers.extract_first_item(results, 'representatives', logger)


async def main(logger):
    async with async_playwright() as playright:
        browser = await playright.chromium.launch()
        results = await get_representatives(browser, logger)
    return results


def process():
    logger = helpers.setup_logger_stdout(os.path.basename(__file__))
    logger.info('<<Starting to fetch representatives>>')
    results = asyncio.run(main(logger))
    logger.info('<<Ending fetching representatives>>')
    return results
