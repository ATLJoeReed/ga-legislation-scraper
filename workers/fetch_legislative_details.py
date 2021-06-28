#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio
import os

from playwright.async_api import async_playwright

from utils import helpers


async def get_legislative_details(browser, urls, logger):
    _, intercept_routes = helpers.get_url_intercept_routes('legislative_details', logger) # noqa
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


def process(legislative_ids):
    logger = helpers.setup_logger_stdout(os.path.basename(__file__))
    logger.info('<<Starting to fetch legislative details>>')

    logger.info('Building URLs')
    urls = []
    base_url, _ = helpers.get_url_intercept_routes('legislative_details', logger) # noqa

    for id in legislative_ids:
        url = base_url.format(**{'legislation_id': id})
        urls.append(url)
    logger.info(f'Built {len(urls)} URLs for processing')

    results = asyncio.run(main(urls, logger))
    logger.info(f'fetched_results length: {len(results)}')

    logger.info('<<Ending fetching legislative details>>')
    return results
