import requests
from pages.base_page import *
from jsonschema import validate


@allure.step(f"Get list users with GET")
def get_list_users(endpoint):
    return requests.get(f"{endpoint}/api/users?page=2")


@allure.step(f"Create new user with POST")
def create_new_user(endpoint, data):
    return requests.post(f"{endpoint}/api/users", data=data)


@allure.step(f"Update user with PUT")
def create_update_user(endpoint, data):
    return requests.put(f"{endpoint}/api/users/2", data=data)


@allure.step(f"Check status code")
def should_be_correct_status_code(logger, response, expected_status_code):
    assert response.status_code == expected_status_code, \
        (f"Response status code is not {expected_status_code}",
         logger.error(f"Response status code is not {expected_status_code}"))[0]
    logger.info(f'OK! Response status code is {expected_status_code}')


@allure.step(f"Check validate response body")
def should_be_validate_response_body(response, schema):
    validate(instance=response.json(), schema=schema)


@allure.step(f"Check correct response body")
def should_be_correct_response_body(response, schema):
    for key, value in schema.items():
        assert value in response.json().values()
