import pytest
from data.get_data import *
from data.post_data import CREATE_SCHEMA, NEW_USER_DATA, NEGATIVE_DATA
from data.put_data import *
from api.api_methods import *


# Positive tests
@allure.feature("Test reqres.in")
@allure.story("GET methods")
@allure.title("Get list users")
@allure.step("Checking work get request")
@pytest.mark.positive
@pytest.mark.get_list_users
@pytest.mark.parametrize("expected_status_code, validate_schema, correct_schema", [
    (200,
     GET_VALIDATE_LIST_USERS,
     GET_LIST_USERS)]
    )
def test_get_list_users(logger, base_url, expected_status_code, validate_schema, correct_schema):
    """
    Check get list users

    """
    response = get_list_users(endpoint=base_url)
    should_be_correct_status_code(logger=logger, response=response, expected_status_code=expected_status_code)
    should_be_validate_response_body(response=response, schema=validate_schema)
    should_be_correct_response_body(response=response, schema=correct_schema)


@allure.feature("Test reqres.in")
@allure.story("POST methods")
@allure.title("Create new user")
@allure.step("Checking that new user is created")
@pytest.mark.positive
@pytest.mark.create_new_user
@pytest.mark.parametrize("data, expected_status_code, schema", [(NEW_USER_DATA, 201, CREATE_SCHEMA)])
def test_create_new_user(logger, base_url, data, expected_status_code, schema):
    """
    Check create new user

    """
    response = create_new_user(endpoint=base_url, data=data)
    should_be_correct_status_code(logger=logger, response=response, expected_status_code=expected_status_code)
    should_be_validate_response_body(response=response, schema=schema)


@allure.feature("Test reqres.in")
@allure.story("PUT methods")
@allure.title("Update user")
@allure.step("Checking that user is updated")
@pytest.mark.positive
@pytest.mark.update_new_user
@pytest.mark.parametrize("data, expected_status_code, validate_schema, correct_schema", [
    (NEW_USER_DATA,
     200,
     UPDATE_VALIDATE_SCHEMA,
     UPDATE_CORRECT_SCHEMA)]
    )
def test_create_new_user(logger, base_url, data, expected_status_code, validate_schema, correct_schema):
    """
    Check update user

    """
    response = create_update_user(endpoint=base_url, data=data)
    should_be_correct_status_code(logger=logger, response=response, expected_status_code=expected_status_code)
    should_be_validate_response_body(response=response, schema=validate_schema)
    should_be_correct_response_body(response=response, schema=correct_schema)


# Negative tests
@allure.feature("Test reqres.in")
@allure.story("POST methods")
@allure.title("Do not create new user")
@allure.step("Checking that new user is not created")
@pytest.mark.negative
@pytest.mark.parametrize("data, expected_status_code, schema", [(NEGATIVE_DATA, 201, CREATE_SCHEMA)])
def test_negative_create_new_user(logger, base_url, data, expected_status_code, schema):
    """
    Negative test create new user

    """
    response = create_new_user(endpoint=base_url, data=data)
    should_be_correct_status_code(logger=logger, response=response, expected_status_code=expected_status_code)
    should_be_validate_response_body(response=response, schema=schema)
