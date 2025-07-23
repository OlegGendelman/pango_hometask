import re
from playwright.sync_api import Page, expect

import config

def test_example(page: Page) -> None:
    page.goto(config.app_url)
    page.get_by_role("textbox", name="שם משתמש").click()
    page.get_by_role("textbox", name="שם משתמש").fill(config.username_1)
    page.get_by_role("textbox", name="סיסמה").click()
    page.get_by_role("textbox", name="סיסמה").fill(config.password_1)
    page.get_by_role("button", name="כניסה").click()
    page.get_by_role("textbox", name="Car Plate").fill(config.seven_digit_lp)
    expect(page.locator("#plate-error")).not_to_be_visible()
