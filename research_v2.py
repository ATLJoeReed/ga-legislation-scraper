from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    def get_token(route, request):
        print(request.response())
        route.continue_()

    def log_and_continue_request(route, request):
        print(request.url)
        route.continue_()

    # Log and continue all network requests
    # page.route("https://www.legis.ga.gov/api/*", log_and_continue_request)

    page.route("https://www.legis.ga.gov/api/authentication/*", get_token)

    page.goto("https://www.legis.ga.gov/legislation/58786", wait_until="networkidle")
    browser.close()