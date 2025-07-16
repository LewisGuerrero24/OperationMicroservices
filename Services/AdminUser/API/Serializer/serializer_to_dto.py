# Sin restricción de pydantic
from typing import Type, TypeVar

T = TypeVar('T')

def serializer_to_dto(serializer, dto_class: Type[T]) -> T:
    data = serializer.validated_data
    return dto_class(**data)
