from factory import HandlerFactory
from abstract.file_handler_base import Handler


@HandlerFactory.register('s3')
class S3FileHandler(Handler):

    def download(self, path: str):
        pass

    def upload(self, data: bytes, path: str):
        pass