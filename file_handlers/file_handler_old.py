from factory import HandlerFactory
from abstract.file_handler_base import Handler


@HandlerFactory.register('old')
class FileHandler(Handler):

    def download(self, path: str):
        pass

    def upload(self, data, path: str):
        pass

