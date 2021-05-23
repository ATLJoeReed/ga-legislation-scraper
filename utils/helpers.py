#!/usr/bin/python3.9
# -*- coding: utf-8 -*-


def intercept_api_calls(playwright, url, intercept_routes):
    intercepted_json = {}

    def extract_json(response):
        if any(route in response.url for route in intercept_routes):
            intercepted_json[response.url] = response.json()

    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.on("response", extract_json)
    page.goto(url, wait_until="networkidle")
    browser.close()
    return intercepted_json
