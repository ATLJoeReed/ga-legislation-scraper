#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import json
import logging
import re
import sys
from unicodedata import normalize

from bs4 import BeautifulSoup
from utils import constants


def extract_current_sessions(results, logger):
    results_values = list(results.values())
    if len(results_values) != 1:
        logger.warning('Sessions JSON objects needs inspecting')
    sessions = results_values[0]
    for session in sessions:
        if session.get('isCurrent'):
            return session.get('id')


def extract_first_item(results, type, logger):
    results_values = list(results.values())
    if len(results_values) != 1:
        logger.warning(f'{type} JSON objects needs inspecting')
    return results_values[0]


def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    # cleanup some of the unicode characters...
    step_1 = normalize('NFKD', text)
    # removes the line numbers...
    step_2 = re.sub('\\n([1-9][0-9]*)', ' ', step_1)
    # removes multiple spaces...
    step_3 = re.sub(' +', ' ', step_2)
    # final bit of code cleanup...
    step_4 = "".join(i for i in step_3 if 31 < ord(i) < 127)
    return step_4.strip()


def get_legistative_members(context, params, type, logger):
    url, intercept_routes = get_url_intercept_routes(type, logger)
    adjusted_routes = update_list_item(intercept_routes, params, logger)
    logger.info(f'Intercepting {type} route')
    results = intercept_api_calls(context, url, adjusted_routes)
    return extract_first_item(results, type, logger)


def get_url_intercept_routes(legislative_route, logger):
    logger.info(f'Getting {legislative_route} url and intercept routes')
    url = constants.GA_LEGISLATION_ROUTES.get(legislative_route).get('url')
    intercept_routes = constants.GA_LEGISLATION_ROUTES.get(legislative_route).get('intercept_routes') # noqa
    return (url, intercept_routes)


async def intercept_api_calls(context, url, intercept_routes):
    intercepted_json = {}

    async def extract_json(response):
        if any(route in response.url for route in intercept_routes):
            intercepted_json[response.url] = await response.json()

    page = await context.new_page()
    page.on("response", extract_json)
    await page.goto(url, wait_until="networkidle")
    await page.close()
    return intercepted_json


def setup_logger_stdout(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def update_item(item, params, logger):
    updated_item = item.format(**params)
    logger.info(f'Updated item: {item} --> {updated_item}')
    return updated_item


def update_list_item(list_object, params, logger):
    updated_items = []
    for item in list_object:
        updated_items.append(update_item(item, params, logger))
    return updated_items


def write_json_file(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)
