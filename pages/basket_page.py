from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text == \
               "Your basket is empty. Continue shopping", "Basket is not empty"
