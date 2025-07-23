import re
from playwright.sync_api import Page, expect

import config
from logger import logger

def test_license_plates_length(page: Page) -> None:

    logger.info("Ending parking with new user")
    page.goto(config.app_url)
    
    username_box = page.get_by_role("textbox", name="שם משתמש")
    password_box = page.get_by_role("textbox", name="סיסמה")
    slot = page.get_by_role("textbox", name="Slot")
    license_plate = page.get_by_role("textbox", name="Car Plate")
    login = page.get_by_role("button", name="כניסה")

    logger.info("Filling in credentials details")
    username_box.fill(config.username_1)
    password_box.fill(config.password_1)
    login.click()

    # List of valid plate numbers (5–8 digits)
    valid_plates = [
        config.eight_digit_lp,
        config.seven_digit_lp,
        config.six_digit_lp,
        config.five_digit_lp
    ]

    for plate in valid_plates:
        logger.info(f"Testing valid license plate: {plate}")
        license_plate.fill(plate)

        # Assert no error is shown
        expect(page.locator("#plate-error")).not_to_be_visible()
        logger.info(f"{plate} license plate tested successfully")
