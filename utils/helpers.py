#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import logging
import sys

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


def get_committees(context, params, logger):
    url, intercept_routes = get_url_intercept_routes('committees', logger)
    adjusted_routes = update_list_item(intercept_routes, params, logger)
    logger.info('Intercepting committee route')
    results = intercept_api_calls(context, url, adjusted_routes)
    return extract_first_item(results, 'committees', logger)


def get_current_session(context, logger):
    url, intercept_routes = get_url_intercept_routes('sessions', logger)
    logger.info('Intercepting session route')
    results = intercept_api_calls(context, url, intercept_routes)
    return extract_current_sessions(results, logger)


def get_legislation_details(context, params, logger):
    url, intercept_routes = get_url_intercept_routes('legislation_details', logger) # noqa
    adjusted_url = update_item(url, params, logger)
    adjusted_routes = update_list_item(intercept_routes, params, logger)
    logger.info('Intercepting legislation details route')
    results = intercept_api_calls(context, adjusted_url, adjusted_routes)
    return results


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


def intercept_api_calls(context, url, intercept_routes):
    intercepted_json = {}

    def extract_json(response):
        if any(route in response.url for route in intercept_routes):
            intercepted_json[response.url] = response.json()

    page = context.new_page()
    page.on("response", extract_json)
    page.goto(url, wait_until="networkidle")
    context.close()
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
