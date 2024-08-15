from pydantic import field_validator
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """Configuration settings for the application.
    Base directory is the directory where the files are stored.
    The BASE_DIRECTORY_CREATE_TYPE defines how the base directory is created. If it is set to "update", the directory
    is updated with the new files. If it is set to "create", the directory is replaced with the new files every time
    the application starts.

    These settings are supposed to be provided as environment variables or in a .env file. Environment variables always
    override the values in the .env file(Because of how BaseSettings is implemented in pydantic_settings).
    """
    BASE_DIRECTORY: str
    BASE_DIRECTORY_CREATE_TYPE: str = "update"

    model_config = {
        "env_file": "HTTP_database/.env"
    }

    @classmethod
    @field_validator('BASE_DIRECTORY_CREATE_TYPE')
    def validate_create_type(cls, v):
        if v not in {'update', 'replace'}:
            raise ValueError('Invalid BASE_DIRECTORY_CREATE_TYPE')
        return v


