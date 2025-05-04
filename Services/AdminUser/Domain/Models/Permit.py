from datetime import datetime
from typing import Optional
from Domain.Models import Module, Spaces


class Permit:
    def __init__(
        self, spaces: Spaces, module: Module, name: str,
        description: Optional[str] = None, is_custom: bool = False,
        system_defined: bool = False, logical_route: Optional[str] = None,
        status: bool = True, creation_date: Optional[datetime] = None,
        update_date: Optional[datetime] = None
    ):
        self.spaces = spaces
        self.module = module
        self.name = name
        self.description = description
        self.is_custom = is_custom
        self.system_defined = system_defined
        self.logical_route = logical_route
        self.status = status
        self.creation_date = creation_date
        self.update_date = update_date