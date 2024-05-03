import requests
import json
import pytest
from tests.baseclass import BaseTest

URL = "https://swapi.dev/api/"

PEOPLE_COUNT = 82
FILMS_COUNT = 2
SPECIES_COUNT = 0
VEHICLES_COUNT = 0
STARSHIPS_COUNT = 0

NAME = "R4-P17"
HEIGHT = "96"
MASS = "unknown"
HAIR_COLOR = "none"
SKIN_COLOR = "silver, red"
EYE_COLOR = "red, blue"
BIRTH_YEAR = "unknown"
GENDER = "female"
HOMEWORLD = "unknown"


@pytest.mark.blocker
def test_get_all_people():
    # Assuming BASE_URL and PEOPLE are defined elsewhere
    response = requests.get(BaseTest.BASE_URL + BaseTest.PEOPLE)

    # # Check status code
    assert response.status_code == 200
    #
    # # Extract response JSON
    json_data = response.json()
    #
    # # Assuming PEOPLE_COUNT is defined elsewhere
    assert json_data["count"] == PEOPLE_COUNT


@pytest.mark.blocker
def test_get_one_person_by_path_param():
    response = requests.get(f"{BaseTest.BASE_URL}{BaseTest.PEOPLE}/75")

    assert response.status_code == 200

    json_data = response.json()

    compare_people_object(json_data)


@pytest.mark.blocker
@pytest.mark.parametrize("name", ["r4-p17", "p1", NAME])
def test_get_one_person_by_query_param(name):
    response = requests.get(BaseTest.BASE_URL + BaseTest.PEOPLE, params={"search": name})

    assert response.status_code == 200

    json_data = response.json()
    first_record = json_data.get("results", [])[0]
    compare_people_object(first_record)


def compare_people_object(object_path):
    try:
        assert object_path["name"] == NAME
        assert object_path["height"] == HEIGHT
        assert object_path["mass"] == MASS
        assert object_path["hair_color"] == HAIR_COLOR
        assert object_path["skin_color"] == SKIN_COLOR
        assert object_path["eye_color"] == EYE_COLOR
        assert object_path["birth_year"] == BIRTH_YEAR
        assert object_path["gender"] == GENDER
        assert get_people_homeworld(object_path["homeworld"]) == HOMEWORLD
        assert len(object_path["films"]) == FILMS_COUNT
        assert len(object_path["starships"]) == STARSHIPS_COUNT
        assert len(object_path["vehicles"]) == VEHICLES_COUNT
        assert len(object_path["species"]) == SPECIES_COUNT
    except AssertionError as e:
        pytest.fail(f"Assertion failed: {e}")


def get_people_homeworld(homeworld_url):
    response = requests.get(homeworld_url)
    return response.json().get("name")


@pytest.fixture(params=["r4-p17", "p1", NAME])
def query_param_data(request):
    return request.param
