import allure
import json
import pytest
from actions import base_actions
import requests


# method to get all people attribute
@allure.step("Get all data")
@pytest.mark.blocker
def get_all_data(client=requests, **kwargs):
    return base_actions.get(client, "people", **kwargs)


# method to get specific id for people
@allure.step("Get a single set")
def get_singleset_path_param(post_id, client=requests, **kwargs):
    return base_actions.get(client, "people/" + str(post_id))


@allure.step("Get a single set with query param")
def get_singleset_query_param(name, client=requests, **kwargs):
    return base_actions.get(client, "people/", params={"search": name})
