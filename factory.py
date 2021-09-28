from typing import Dict, Type, Callable
from abstract.file_handler_base import Handler

class HandlerFactory:
    handlers: Dict[str, Type[Handler]] = {}

    @classmethod
    def make_handler(cls, version)-> Type[Handler]:
        try:
            retval = cls.handlers[version]
        except KeyError as err:
            raise NotImplementedError(f"{version=} doesn't exist") from err
        return retval

    @classmethod
    def register(cls, type_name) -> Callable[[Type[Handler]], Type[Handler]]:
        def deco(deco_cls)-> Type[Handler]:
            cls.handlers[type_name] = deco_cls
            return deco_cls
        return deco

