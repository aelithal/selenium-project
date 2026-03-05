from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def click_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()