#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio
import os

from playwright.async_api import async_playwright

from utils import helpers


async def get_member_voters(browser, vote_params, logger):
    context = await browser.new_context()
    tasks = []
    for param in vote_params:
        url, number, intercept_routes = param
        logger.info(f'Processing vote number: {number}')
        tasks.append(
            asyncio.ensure_future(
                helpers.intercept_api_call_with_click(context, url, number, intercept_routes) # noqa
            )
        )
    fetched_results = await asyncio.gather(*tasks)
    return fetched_results


async def main(vote_params, logger):
    async with async_playwright() as playright:
        browser = await playright.chromium.launch()
        results = await get_member_voters(browser, vote_params, logger)
    return results


def process(votes):
    logger = helpers.setup_logger_stdout(os.path.basename(__file__))
    logger.info('<<Starting to fetch member votes>>')
    for vote in votes:
        vote_params = []
        id, number, name = vote
        logger.info(f'Processing vote: {name}')
        if 'House' in name:
            vote_type = 'house_member_votes'
        else:
            vote_type = 'senate_member_votes'
        url, base_intercept_routes = helpers.get_url_intercept_routes(vote_type, logger) # noqa
        intercept_route = base_intercept_routes[0].format(**{'vote_id': id})
        vote_params.append((url, number, [intercept_route]))

    results = asyncio.run(main(vote_params, logger))
    logger.info('<<Ending fetching member votes>>')
    return results
