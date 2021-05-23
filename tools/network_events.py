#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright


def show_api_requests(requests):
    if 'legis.ga.gov/api' in requests.url:
        print(">>", requests.method, requests.url)


def show_api_reponses(response):
    if 'legis.ga.gov/api' in response.url:
        print(">>", response.status, response.url)


def watch_all_network_events(playwright, url, only_api):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    if only_api:
        page.on("request", show_api_requests)
        page.on("response", show_api_reponses)
    else:
        page.on("request", lambda request: print(">>", request.method, request.url)) # noqa
        page.on("response", lambda response: print("<<", response.status, response.url)) # noqa
    page.goto(url, wait_until="networkidle")
    browser.close()


url = 'https://www.legis.ga.gov'
with sync_playwright() as playwright:
    watch_all_network_events(playwright, url, only_api=True)
