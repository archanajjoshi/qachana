import requests
from pytest_bdd import scenario, given, when, then, parsers
from src import app

@scenario("dog_code.feature", "Dog Code")
def test_dog_code():
    pass

@given("I can access dog api")
def access_dog_api():
    response = requests.get(app.API_URL)
    return response

@when(parsers.parse("I do a GET request on dog api with status code {code}"))
def get_dog_api(code, response_data):
    response = requests.get(f"{app.API_URL}/{code}.json")
    response_data["response"] = response

@then(parsers.parse("I should get a success response with status code {response_code}"))
def verify_success_response(response_code, response_data):
    data = response_data["response"].json()
    assert data["status_code"] == int(response_code)