from typing import Type, TypeVar
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

def serializer_to_dto(serializer, dto_class: Type[T]) -> T:
    data = serializer.validated_data
    return dto_class(**data)
