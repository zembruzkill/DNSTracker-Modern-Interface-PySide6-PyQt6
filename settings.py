import os
import json

from datetime import timedelta


def get_env_var(config, settings, default=''):
    """Returns configuration value from settings loaded from file"""
    env_var = ''
    # checks if env variable is loaded,
    if config in settings:
        env_var = settings[config]
    elif config in os.environ:
        env_var = os.environ[config]
    else:
        env_var = default

    env_var = True if env_var == 'True' else False if env_var == 'False' else env_var
    return env_var

try:
    with open('settings.json') as f:
        SETTINGS = json.loads(f.read())
except FileNotFoundError:
    SETTINGS = {}


BASE_URL = get_env_var("base_url", SETTINGS)
JSON_HEADERS = {'Content-type': 'application/json'}
MULTIPART_HEADERS = {'Content-type': 'multipart/form-data'}
