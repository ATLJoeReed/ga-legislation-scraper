#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio
import os

from playwright.async_api import async_playwright

from utils import helpers
from workers import fetch_member_votes


async def get_legislative_details(browser, urls, intercept_routes, logger):
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


async def main(urls, intercept_routes, logger):
    async with async_playwright() as playright:
        browser = await playright.chromium.launch()
        results = await get_legislative_details(browser, urls, intercept_routes, logger) # noqa
    return results


def process(legislative_ids):
    logger = helpers.setup_logger_stdout(os.path.basename(__file__))
    logger.info('<<Starting to fetch legislative details>>')

    logger.info('Building URLs')
    urls = []
    base_url, intercept_routes = helpers.get_url_intercept_routes('legislative_details', logger) # noqa

    # Build URLs for each legislative id passed in...
    for id in legislative_ids:
        url = base_url.format(**{'legislation_id': id})
        urls.append(url)
    logger.info(f'Built {len(urls)} URLs for processing')

    results = asyncio.run(main(urls, intercept_routes, logger))
    logger.info(f'fetched_results length: {len(results)}')

    final_results = []
    for r in results:
        legislative_info = {}
        results_values = list(r.values())
        # bill details are stored in first element
        legislative_info['details'] = results_values[0]
        # Lets check and see if the legislation has votes associated with it.
        votes = legislative_info.get('details').get('votes')
        if votes:
            vote_params = []
            logger.info(f'Found {len(votes)} votes associated with this legislation') # noqa
            # Loop thru each vote and fetch the member votes for each
            for v in votes:
                # Pulling out (3) data points needed to extract member votes
                vote_params.append((v.get('id'), v.get('number'), v.get('name'))) # noqa
            results = fetch_member_votes.process(vote_params)
            # legislative_info['member_votes'] = results
        # html is stored in second element
        document_html = results_values[1]
        # We need to get the array of html pages into a single html stream
        logger.info('Parsing text from HTML and repackaging results')
        html = ''
        for d in document_html:
            html += d
        document_text = helpers.extract_text_from_html(html)
        legislative_info['document_number_pages'] = len(document_html)
        legislative_info['document_text'] = document_text
        legislative_info['document_html'] = document_html
        final_results.append(legislative_info)

    logger.info('<<Ending fetching legislative details>>')
    return final_results
