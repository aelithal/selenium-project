import pytest, time

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_button()
    page.click_button()
    page.solve_quiz_and_get_code()
    time.sleep(30)

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
