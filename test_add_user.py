import re
from playwright.sync_api import Page, expect

import config

def test_example(page: Page) -> None:
    page.goto(config.app_url)
    
    username_box = page.get_by_role("textbox", name="שם משתמש")
    password_box = page.get_by_role("textbox", name="סיסמה")
    login = page.get_by_role("button", name="כניסה")
    

    username_box.click()
    username_box.fill(config.username_1)
    password_box.click()
    password_box.fill(config.password_1)
    login.click()
    page.get_by_role("link", name="Users").click()
    page.get_by_role("link", name="Add User").click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(config.username_2)
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill(config.password_2)
    page.get_by_role("button", name="Save").click()
    expect(page.locator("body")).to_contain_text(config.username_2)
    page.get_by_role("link", name="Logout").click()
    expect(login).to_be_visible()
    username_box.click()
    username_box.fill(config.username_2)
    username_box.press("Tab")
    password_box.fill(config.password_2)
    password_box.press("Enter")
    login.click()
    expect(page.get_by_role("alert")).to_contain_text("User created")

    page.get_by_role("link", name="Users").click()
    page.get_by_role("row", name="user2 Delete").get_by_role("button").click()
