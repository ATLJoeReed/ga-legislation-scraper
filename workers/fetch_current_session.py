#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio
import os

from playwright.async_api import async_playwright

from utils import helpers


async def get_current_session(browser, logger):
    url, intercept_routes = helpers.get_url_intercept_routes('sessions', logger) # noqa
    logger.info('Intercepting session route')
    context = await browser.new_context()
    results = await helpers.intercept_api_calls(context, url, intercept_routes)
    return helpers.extract_current_sessions(results, logger)


async def main(logger):
    async with async_playwright() as playright:
        browser = await playright.chromium.launch()
        results = await get_current_session(browser, logger)
    return results


def process():
    logger = helpers.setup_logger_stdout(os.path.basename(__file__))
    logger.info('<<Starting to fetch current session>>')
    results = asyncio.run(main(logger))
    logger.info(f'Current session id: {results}')
    logger.info('<<Ending fetching current session>>')
    return results
