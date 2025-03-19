import pytest
from playwright.sync_api import sync_playwright
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            # Create screenshots directory
            screenshots_dir = os.path.join("results", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            
            # Capture screenshot
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            test_name = report.nodeid.split("::")[-1]
            screenshot_name = f"{test_name}-{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_name)
            
            page.screenshot(path=screenshot_path)
            
            # Add to HTML report
            html = f'<div><img src="{screenshot_path}" style="width:60%"/></div>'
            report.extra = [("Screenshot", html)]

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                "--disable-web-security",
                "--no-sandbox",
                "--disable-setuid-sandbox",
  #              "--start-maximized",
                "--disable-infobars",
                "--disable-dev-shm-usage",
                "--disable-gpu"
            ]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            viewport={"width": 1500, "height": 700},
            java_script_enabled=True
        )
        context.set_default_timeout(10000) # 10 seconds
        yield context
        context.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()