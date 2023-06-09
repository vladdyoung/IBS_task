import allure


class BasePage:
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.logger = browser.logger
        self.browser.implicitly_wait(10)

    @allure.step(f"Open url")
    def open(self):
        try:
            self.logger.info(f"Open url {self.base_url}")
            self.browser.get(self.base_url)
        except:
            self.logger.error(f"URL {self.base_url} is not found")
            raise AssertionError(f"URL {self.base_url} is not found")

    @allure.step('Find element on the page')
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            self.logger.info(f'Element ({what}) is present on the page')
            return True
        except:
            try:
                return False
            finally:
                self.logger.error(f'Element ({what}) is not found')
                raise AssertionError(f'Element ({what}) is not found')

    def click_btn(self, btn):
        with allure.step(f'Click on {btn}'):
            self.browser.find_element(*btn).click()



