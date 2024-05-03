import requests
import pytest

"""This file is to keep reusable methods along with data. Ideally data could be in separate file and will refactor 
later"""


class BaseTest:
    # Test data used to compare
    FILMS = "films"
    PLANETS = "planets"
    VEHICLES = "vehicles"
    STARSHIPS = "starships"
    SPECIES = "species"
    PEOPLE = "people"

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


    def __init__(self):
        # BaseTest = testdata.TestData()
        pass

    @staticmethod
    def get_people_homeworld(homeworld_url):
        response = requests.get(homeworld_url)
        return response.json().get("name")

    # Method to compare the expected output with actual output
    @staticmethod
    def compare_people_object(object_path):
        try:
            assert object_path["name"] == BaseTest.NAME
            assert object_path["height"] == BaseTest.HEIGHT
            assert object_path["mass"] == BaseTest.MASS
            assert object_path["hair_color"] == BaseTest.HAIR_COLOR
            assert object_path["skin_color"] == BaseTest.SKIN_COLOR
            assert object_path["eye_color"] == BaseTest.EYE_COLOR
            assert object_path["birth_year"] == BaseTest.BIRTH_YEAR
            assert object_path["gender"] == BaseTest.GENDER
            assert BaseTest.get_people_homeworld(object_path["homeworld"]) == BaseTest.HOMEWORLD
            assert len(object_path["films"]) == BaseTest.FILMS_COUNT
            assert len(object_path["starships"]) == BaseTest.STARSHIPS_COUNT
            assert len(object_path["vehicles"]) == BaseTest.VEHICLES_COUNT
            assert len(object_path["species"]) == BaseTest.SPECIES_COUNT
        except AssertionError as e:
            pytest.fail(f"Assertion failed: {e}")


# Fixture for parameters passing. It parametrized with three values
@pytest.fixture(params=["Han Solo", "p1", BaseTest.NAME])
def query_param_data(request):
    return request.param
