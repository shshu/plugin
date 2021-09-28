from abstract.file_handler_base import Handler
from factory import HandlerFactory
from pathlib import Path

import importlib
import os

def load_python_modules_from_folder(folder: str):
    modules = [module for module in os.listdir(folder)]
    for m in modules:
        module, _ = os.path.splitext(m)
        importlib.import_module(f'{folder}.{module}')

def main() -> None:
    handler: Handler = HandlerFactory

    # load handlers
    load_python_modules_from_folder('file_handlers')

    # load plugin
    load_python_modules_from_folder('plugin')

    print(handler.handlers)

if __name__ == '__main__':
    main()
