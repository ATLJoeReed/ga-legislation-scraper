#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import asyncio
import os

from playwright.async_api import async_playwright

from utils import helpers


async def get_member_voters(browser, params, logger):
    context = await browser.new_context()
    tasks = []
    for p in params:
        url, number, intercept_routes = p
        logger.info(f'Intercepting member votes {intercept_routes}')
        tasks.append(
            asyncio.ensure_future(
                helpers.intercept_api_call_with_click(
                    context,
                    url,
                    number,
                    intercept_routes
                )
            )
        )
    fetched_results = await asyncio.gather(*tasks)
    return fetched_results


async def main(params, logger):
    async with async_playwright() as playright:
        browser = await playright.chromium.launch()
        results = await get_member_voters(browser, params, logger)
        await browser.close()
    return results


def process(vote_params):
    logger = helpers.setup_logger_stdout(os.path.basename(__file__))
    logger.info('<<Starting to fetch member votes>>')
    params = []
    for v in vote_params:
        id, number, name = v
        logger.info(f'Processing vote id: {id}')
        if 'House' in name:
            vote_type = 'house_member_votes'
        else:
            vote_type = 'senate_member_votes'
        url, intercept_routes = helpers.get_url_intercept_routes(vote_type, logger) # noqa
        adjusted_routes = helpers.update_list_item(intercept_routes, {'vote_id': id}, logger) # noqa
        params.append((url, number, adjusted_routes))
    results = asyncio.run(main(params, logger))
    logger.info('<<Ending fetching member votes>>')
    return results
