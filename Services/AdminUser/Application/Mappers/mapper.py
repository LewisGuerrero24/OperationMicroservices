from django.forms.models import model_to_dict
from typing import Type, TypeVar
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

def model_to_dto(model_instance, dto_class: Type[T]) -> T:
    data = model_to_dict(model_instance)
    return dto_class(**data)

def dto_to_model(dto_instance: BaseModel, model_class):
    return model_class(**dto_instance.dict())