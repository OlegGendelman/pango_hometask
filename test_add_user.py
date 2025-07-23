from playwright.sync_api import Page, expect

import config
from logger import logger


def test_add_user(page: Page) -> None:
    """
    Test adding a new user to the system.
    And verifying user is logged and working with the new user.
    """

    logger.info(f"Open tested application: {config.app_url}")
    page.goto(config.app_url)
    
    username_box = page.get_by_role("textbox", name="שם משתמש")
    password_box = page.get_by_role("textbox", name="סיסמה")
    slot = page.get_by_role("textbox", name="Slot")
    license_plate = page.get_by_role("textbox", name="Car Plate")
    login = page.get_by_role("button", name="כניסה")
    
    logger.info("Filling in credentials details")
    username_box.click()
    username_box.fill(config.username_1)
    password_box.click()
    password_box.fill(config.password_1)
    login.click()
    logger.info("Adding new user")
    page.get_by_role("link", name="Users").click()
    page.get_by_role("link", name="Add User").click()
    logger.info("Entering new user details")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(config.random_user)
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill(config.random_password)
    page.get_by_role("button", name="Save").click()
    logger.info("Verifying user added successfully")
    expect(page.locator("body")).to_contain_text(config.random_user)
    logger.info("Logging out and logging in again with the new user details")
    page.get_by_role("link", name="Logout").click()
    logger.info("Filling in new user credentials")
    username_box.click()
    username_box.fill(config.random_user)
    username_box.press("Tab")
    password_box.fill(config.random_password)
    login.click()
    logger.info("Starting parking with new user")
    license_plate.click()
    license_plate.fill(config.eight_digit_lp)
    slot.click()
    slot.fill(config.parking_slot)
    page.get_by_role("button", name="Start Parking").click()
    expect(page.get_by_role("alert")).to_contain_text(f"Parking started for {config.eight_digit_lp}")
    expect(page.locator("tbody")).to_contain_text("סיים")
    logger.info("Ending parking with new user")
    page.get_by_role("button", name="סיים").click()

