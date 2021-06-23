#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio

from playwright.async_api import async_playwright

from utils import helpers


async def get_legislative_details(browser, urls, logger):
    intercept_routes = ['/api/legislation/detail', '/api/legislation/html']
    context = await browser.new_context()
    tasks = []
    for u in urls:
        logger.info(f'Processing url: {u}')
        tasks.append(
            asyncio.ensure_future(
                helpers.intercept_api_calls(context, u, intercept_routes)
            )
        )
    fetched_results = await asyncio.gather(*tasks)
    return fetched_results


async def main(urls, logger):
    async with async_playwright() as playright:
        browser = await playright.chromium.launch()
        results = await get_legislative_details(browser, urls, logger)
    return results


def process(urls):
    logger = helpers.setup_logger_stdout('fetch_legislative_details') # noqa
    logger.info('<<Starting to fetch legislative details>>')

    results = asyncio.run(main(urls, logger))
    logger.info(f'final_results length: {len(results)}')

    logger.info('<<Ending fetching legislative details>>')
    return results
