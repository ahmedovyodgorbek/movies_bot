import logging
from typing import Callable

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='logs.log'
)


def logger(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        try:
            func_res = func(*args, **kwargs)
            message = (f"Func: {func.__name__} Result: {func_res}"
                       f"ARGS: {args} KWARGS:{kwargs}")
            logging.info(message)
            return func_res
        except Exception as e:
            message = (f"Func: {func.__name__} Error: {e}"
                       f"ARGS: {args} KWARGS: {kwargs}")
            logging.error(message)

    return wrapper
