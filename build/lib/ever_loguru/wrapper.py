from loguru import logger
from logging import PlaceHolder


class LoggingLoguruWrapper(PlaceHolder):
    def __init__(self, __placeholder: str = None, _depth=0):
        self._depth = _depth
        pass

    def __getattr__(self, item):
        return getattr(logger.opt(depth=self._depth), item)


class AsyncLoggingLoguruWrapper(PlaceHolder):
    def __init__(self, __placeholder: str = None, _depth=2):
        self._depth = _depth

    @staticmethod
    def _async_wrapper(func):
        async def __logger_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return __logger_wrapper

    def __getattr__(self, item):
        return self._async_wrapper(getattr(logger.opt(depth=self._depth), item))