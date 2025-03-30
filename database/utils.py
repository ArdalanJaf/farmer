from typing import Type, TypeVar
from pydantic import BaseModel, ValidationError


T = TypeVar("T", bound=BaseModel)

def validate_json(data: dict, schema_class: Type[T]) -> dict:
    """
    Validates data against a Pydantic schema class.
    Returns the validated dict or raises ValueError.
    """
    try:
        validated = schema_class(**data)
    except ValidationError as e:
        raise ValueError(f"Invalid data for {schema_class.__name__}: {e}")
    return validated.model_dump()