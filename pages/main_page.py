""" Maine page of reqres.in """
import json

from pages.base_page import *

from pages.locators import MainPageLocators


class MainPage(BasePage):
    def get_status_code_of_methods(self):
        self.is_element_present(*MainPageLocators.STATUS_CODE_OF_METHODS)
        return self.browser.find_element(*MainPageLocators.STATUS_CODE_OF_METHODS)

    def should_be_equal_status_code(self, api_status_code):
        with allure.step('Equal status codes'):
            self.is_element_present(*MainPageLocators.STATUS_CODE_OF_METHODS)
            status_code_of_methods = int((self.browser.find_element(*MainPageLocators.STATUS_CODE_OF_METHODS).text.
                                          replace('Response', '')).replace('\n', ''))
            assert status_code_of_methods == api_status_code.status_code, ('Status codes is not equal',
                                                               self.logger.error('Status codes is not equal'))[0]

    def should_be_equal_response_body(self, api_response_body):
        with allure.step('Equal response body'):
            self.is_element_present(*MainPageLocators.RESPONSE_BODY_OF_METHODS)
            k = api_response_body.json()
            response_body_of_methods = json.loads(self.browser.find_element(*MainPageLocators.RESPONSE_BODY_OF_METHODS).text)
            assert response_body_of_methods == api_response_body.json(), ('Response body is not equal',
                                                                 self.logger.error('Response body is not equal'))[0]
