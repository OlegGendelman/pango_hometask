import re
from playwright.sync_api import Page, expect

import config


def test_example(page: Page) -> None:
    page.goto(config.app_url)
    username_box = page.get_by_role("textbox", name="שם משתמש")
    password_box = page.get_by_role("textbox", name="סיסמה")
    slot = page.get_by_role("textbox", name="Slot")
    license_plate = page.get_by_role("textbox", name="Car Plate")
    login = page.get_by_role("button", name="כניסה")
    
    username_box.click()
    username_box.fill(config.username_1)
    password_box.click()
    password_box.fill(config.password_1)
    login.click()
    license_plate.click()
    license_plate.fill(config.eight_digit_lp)
    slot.click()
    slot.fill(config.parking_slot)
    page.get_by_role("button", name="Start Parking").click()
    expect(page.get_by_role("alert")).to_contain_text(f"Parking started for {config.eight_digit_lp}")
    page.get_by_role("link", name="Logout").click()
    username_box.click()
    username_box.fill(config.username_2)
    password_box.click()
    password_box.fill(config.password_2)
    login.click()
    license_plate.click()
    license_plate.fill(config.eight_digit_lp)
    slot.click()
    slot.fill(config.parking_slot_2)
    page.get_by_role("button", name="Start Parking").click()
    expect(page.get_by_role("alert")).to_contain_text("Duplicate parking prevented: this car is already parked.")
    expect(page.locator("tbody")).to_contain_text("סיים")
    page.get_by_role("button", name="סיים").click()

