import pytest
from data.get_data import *
from data.post_data import CREATE_SCHEMA, NEW_USER_DATA, NEGATIVE_DATA
from data.put_data import *
from api.api_methods import *
from pages.main_page import MainPage
from pages.locators import MainPageLocators


@allure.feature("Test reqres.in")
@allure.story("Compare WEB and API")
@allure.title("Compare list users")
@allure.step("Checking WEB equal API")
@pytest.mark.web
@pytest.mark.compare
@pytest.mark.parametrize("btn", [MainPageLocators.GET_USERS_BTN])
def test_web_get_list_users(browser, base_url, logger, btn):
    """
    Compares status code/response body presenting on main page and status code/response body in api response

    """
    main_page = MainPage(browser=browser, base_url=base_url)
    main_page.open()
    main_page.click_btn(btn=btn)
    api_response = get_list_users(endpoint=base_url)
    main_page.should_be_equal_status_code(api_status_code=api_response)
    main_page.should_be_equal_response_body(api_response_body=api_response)
