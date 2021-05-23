from playwright.sync_api import sync_playwright

def show_api_requests(requests):
    if 'legis.ga.gov/api' in requests.url:
        print(requests.url)

def return_token(response):
    if 'egis.ga.gov/api/authentication' in response.url:
        print('TOKEN: ', response.json())

playwright = sync_playwright().start()

browser = playwright.chromium.launch()
page = browser.new_page()
page.on("request", show_api_requests)
page.on("response", return_token)

page.goto("https://www.legis.ga.gov/legislation/all", wait_until="networkidle")
browser.close()
playwright.stop()
