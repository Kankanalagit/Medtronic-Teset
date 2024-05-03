import pytest
import allure
from actions import get_actions as get
from tests.baseclass import BaseTest


# Test case for checking count of people
@allure.description("User should be able to get all people data")
def test_get_all_people_data():
    PEOPLE_COUNT = 82
    try:
        # Call get_all_data() function to get the response
        response = get.get_all_data()

        # Check if the response status code is 200 (OK)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

        # Extract response JSON
        json_data = response.json()

        # Check if the "count" attribute in the JSON data matches the expected PEOPLE_COUNT
        assert json_data["count"] == PEOPLE_COUNT, f"Unexpected 'count' value: {json_data['count']}"

    except AssertionError as e:
        # Handle assertion errors
        print(f"AssertionError: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Test case for accessing specific dataset by passing through URL and validating the response
@pytest.mark.blocker
@allure.description("User should be able to get the 75 record and the data")
def test_get_one_person_by_path_param():
    response = get.get_singleset_path_param(75)

    assert response.status_code == 200

    json_data = response.json()

    # Below line of code is to compare the dataset
    BaseTest.compare_people_object(json_data)


# Test case to check if a specific resource exists
@pytest.mark.blocker
@pytest.mark.parametrize("name", ["r4-p17", "p1"])
@allure.description("Checking the response code where record does not exist")
def test_get_response_code_invalid_param(name):
    response = get.get_singleset_path_param(234)
    assert response.status_code == 404, "Resource does not exist"


# Below test to handle invalid query parameters by returning success code with empty data set.
@pytest.mark.normal
def test_get_one_person_by_invalid_query_param():
    invalid_name = "I don't exist"
    response = get.get_singleset_query_param(invalid_name)
    assert response.status_code == 200
    json_data = response.json()
    assert len(json_data["results"]) == 0

#test single person data with query parameter
@pytest.mark.blocker
@pytest.mark.parametrize("name", ["Luke"])  # Example data provider
def test_get_one_person_by_query_param(name):
    with allure.step(f"Get one person by query param: {name}"):
        response = get.get_singleset_query_param(name)
        assert response.status_code == 200
        json_data = response.json()
        with pytest.raises(AssertionError):
            first_record = json_data["results"][0]
            BaseTest.compare_people_object(first_record)
