#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio

from playwright.async_api import async_playwright

from utils import helpers


urls = [
    'https://www.legis.ga.gov/legislation/58786',
    'https://www.legis.ga.gov/legislation/58787',
    'https://www.legis.ga.gov/legislation/58788',
    'https://www.legis.ga.gov/legislation/58789',
    'https://www.legis.ga.gov/legislation/58790',
    'https://www.legis.ga.gov/legislation/58791',
    'https://www.legis.ga.gov/legislation/58792',
    'https://www.legis.ga.gov/legislation/58793',
    'https://www.legis.ga.gov/legislation/58794',
    'https://www.legis.ga.gov/legislation/58795',
]

final_results = []


def chunk_records(records, n):
    for i in range(0, len(records), n):
        yield records[i:i + n]


async def intercept_api_calls(context, url):
    intercepted_json = {}
    intercept_routes = ['/api/legislation/detail', '/api/legislation/html']

    async def extract_json(response):
        if any(route in response.url for route in intercept_routes):
            intercepted_json[response.url] = await response.json()

    page = await context.new_page()
    page.on("response", extract_json)
    await page.goto(url, wait_until="networkidle")
    await page.close()
    return intercepted_json


async def get_legislative_details(browser, logger):
    chunk_size = 5
    chunked_records = list(chunk_records(urls, chunk_size))

    context = await browser.new_context()

    for chunk in chunked_records:
        tasks = []
        for c in chunk:
            logger.info(f'Processing url: {c}')
            tasks.append(
                asyncio.ensure_future(
                    intercept_api_calls(context, c)
                )
            )
        legislative_detail_results = await asyncio.gather(*tasks)
        final_results.append(legislative_detail_results)
    # helpers.writeout_results(final_results, 'results.json', '.', logger)
    # flat_results = list(itertools.chain(*final_results))
    logger.info(f'final_results length: {len(final_results)}')
    for x in final_results[0]:
        logger.info(x.keys())
        for k in x.keys():
            if '/api/legislation/html' in k:
                logger.info(len(x.get(k)[0]))
                logger.info(x.get(k)[0][0:50])
    for x in final_results[1]:
        logger.info(x.keys())
        for k in x.keys():
            if '/api/legislation/html' in k:
                logger.info(len(x.get(k)[0]))
                logger.info(x.get(k)[0][0:50])
    return final_results


async def main(logger):
    async with async_playwright() as playright:
        browser = await playright.chromium.launch()
        await get_legislative_details(browser, logger)


logger = helpers.setup_logger_stdout('legislative_scraper')
asyncio.run(main(logger))
