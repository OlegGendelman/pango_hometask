import re
from playwright.sync_api import Page, expect

import config
from logger import logger


def test_park_same_car(page: Page) -> None:
    """
    Test will verify that the parking system prevents duplicate parking for the same car with another user logged in.

    This test performs the following steps:
    1. Login with the first user and start parking by providing valid license plate and slot.
    2. Logout and login with second user credentials.
    3. Try to park the same car again in a different slot.
    4. Verifying the system blocks the second parking attempt with relevant information massage.
    5. Verifies that a "סיים" (Finish) button appears, and completes the parking session.
    """

    logger.info("Filling in credentials details")
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

    logger.info("Providing relevant details for the car")
    license_plate.click()
    license_plate.fill(config.eight_digit_lp)
    slot.click()
    slot.fill(config.parking_slot)

    logger.info("Starting the parking session")
    page.get_by_role("button", name="Start Parking").click()
    logger.info("Session started for {config.eight_digit_lp}")
    expect(page.get_by_role("alert")).to_contain_text(f"Parking started for {config.eight_digit_lp}")

    logger.info("Adding new user")
    page.get_by_role("link", name="Users").click()
    page.get_by_role("link", name="Add User").click()
    logger.info("Entering new user details")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(config.username_2)
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill(config.password_2)
    page.get_by_role("button", name="Save").click()
    logger.info("Verifying user added successfully")
    expect(page.locator("body")).to_contain_text(config.random_user)

    logger.info("Logging out and trying to park the same car again")
    page.get_by_role("link", name="Logout").click()

    logger.info("Filling in credentials details for second user")
    username_box.click()
    username_box.fill(config.username_2)
    password_box.click()
    password_box.fill(config.password_2)
    login.click()

    logger.info("Providing relevant details for the car")
    license_plate.click()
    license_plate.fill(config.eight_digit_lp)
    slot.click()
    slot.fill(config.parking_slot_2)

    logger.info("Trying to start the parking session for the same car again")
    page.get_by_role("button", name="Start Parking").click()
    logger.info("Duplicate parking attempt detected")
    expect(page.get_by_role("alert")).to_contain_text("Duplicate parking prevented: this car is already parked.")
    logger.info("Finishing the parking session")
    expect(page.locator("tbody")).to_contain_text("סיים")
    page.get_by_role("button", name="סיים").click()
    logger.info("Logging out")
    page.get_by_role("link", name="Logout").click()
