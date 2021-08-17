import json
import logging
from logging.config import dictConfig

with open('./logging.json') as file:
    config_dict = json.load(file)
    dictConfig(config_dict)

log = logging.getLogger(__name__)


def app():
    log.info("Hello world")
