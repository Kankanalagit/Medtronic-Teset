from environs import Env

env = Env()
env.read_env()

environments = {
    "local": {
        "host_url": "https://swapi.dev/api/",
    },
    "staging": {
        "host_url": "https://swapi.dev/api/",
    },
    "production": {
        "host_url": "https://swapi.dev/api/",
    },
}


def get_environment():
    """Retrieve environment variables"""
    app_env = environments.get(env("app_env", "local"))
    print(f"""Tests will be run against {app_env} environment""")
    return app_env