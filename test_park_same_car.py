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
    page.get_by_role("textbox", name="Car Plate").click()
    page.get_by_role("textbox", name="Car Plate").fill(config.eight_digit_lp)
    page.get_by_role("textbox", name="Slot").click()
    page.get_by_role("textbox", name="Slot").fill(config.parking_slot)
    page.get_by_role("button", name="Start Parking").click()
    expect(page.get_by_role("alert")).to_contain_text(f"Parking started for {config.eight_digit_lp}")
    page.get_by_role("link", name="Logout").click()
    page.get_by_role("textbox", name="שם משתמש").click()
    page.get_by_role("textbox", name="שם משתמש").fill(config.username_2)
    page.get_by_role("textbox", name="סיסמה").click()
    page.get_by_role("textbox", name="סיסמה").fill(config.password_2)
    page.get_by_role("button", name="כניסה").click()
    page.get_by_role("textbox", name="Car Plate").click()
    page.get_by_role("textbox", name="Car Plate").fill(config.eight_digit_lp)
    page.get_by_role("textbox", name="Slot").click()
    page.get_by_role("textbox", name="Slot").fill(config.parking_slot_2)
    page.get_by_role("button", name="Start Parking").click()
    expect(page.get_by_role("alert")).to_contain_text("Duplicate parking prevented: this car is already parked.")
    expect(page.locator("tbody")).to_contain_text("סיים")
    page.get_by_role("button", name="סיים").click()

