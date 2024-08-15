from pydantic import BaseModel, field_validator
from .exception import ValidationException


class CreateCollection(BaseModel):
    name: str

    class Config:
        json_schema_extra = {
            "example": {
                "name": "molecules"
            }
        }

    @classmethod
    @field_validator("name")
    def validate_name(cls, name):
        if not name:
            raise ValidationException("Name cannot be empty.")
        if not name.isalnum():
            raise ValidationException("Name can only contain alphanumeric characters.")
        if name == "collections":
            raise ValidationException("Name cannot be 'collections'.")
        return name


class CreateDocument(BaseModel):
    data: dict

    class Config:
        extra = "forbid"
        json_schema_extra = {
            "example": {
                "data": {
                    "name": "Methane",
                    "smiles": "C",
                    "description": "Simplest alkane"
                }
            }
        }
