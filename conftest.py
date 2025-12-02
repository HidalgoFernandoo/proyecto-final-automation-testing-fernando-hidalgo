import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login_in_driver(driver, usuario, password):
    LoginPage(driver).abrir_pagina().login_completo(usuario, password)
    return driver


@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"


@pytest.fixture
def header_request():
    # API key required for Reqres requests (use x-api-key header per dashboard examples)
    return {"x-api-key": "reqres_e4e7d67af63040e78370f76ebb9b15a4"}


def _get_driver_from_item(item):
    """Return the WebDriver instance used by the test, if any."""
    for fixture_name in ("driver", "login_in_driver"):
        if fixture_name in item.funcargs:
            return item.funcargs[fixture_name]
    return None


def _capture_failure_screenshot(driver, item):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    screenshot_dir = Path(__file__).resolve().parent / "assets" / "screenshots"
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{timestamp}_{item.name}.png"
    destination = screenshot_dir / filename
    driver.save_screenshot(str(destination))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture an automatic screenshot when a Selenium test fails or is expected to fail."""
    outcome = yield
    report = outcome.get_result()

    should_capture = report.when == "call" and (
        report.failed or getattr(report, "wasxfail", False)
    )

    if should_capture:
        driver = _get_driver_from_item(item)
        if driver:
            _capture_failure_screenshot(driver, item)
