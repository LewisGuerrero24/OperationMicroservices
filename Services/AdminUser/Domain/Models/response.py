from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class GenericResponse(Generic[T]):
    def __init__(self, value: Optional[T] = None, message: str = '', is_correct: bool = True):
        self.value = value
        self.message = message
        self.is_correct = is_correct

    def to_dict(self):
        return {
            'value': self.value,
            'message': self.message,
            'is_correct': self.is_correct
        }