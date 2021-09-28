from abc import ABC, abstractmethod
from typing import Protocol

class Handler(Protocol):

    def download(self, path: str) -> bytes:
        pass

    def upload(self, data: bytes, path: str):
        pass

