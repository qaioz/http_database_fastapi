from functools import lru_cache
from .config import Config
from .service import CollectionService


@lru_cache
def get_config():
    return Config()


@lru_cache
def get_service():
    return CollectionService(get_config().BASE_DIRECTORY)
