import logging
from functools import partial


def log(func=None, prefix=''):
    if not func:
        return partial(log, prefix=prefix)

    def wrap_log(*args, **kwargs):
        name = f'{prefix} {func.__name__}'
        print(name)
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        fh = logging.FileHandler("%s.log" % name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Call function: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Result: %s" % result)
        return func

    return wrap_log


def extended_log(time):
    def wrapper(func):
        def inner_log(*args, **kwargs):
            name = func.__name__
            logger = logging.getLogger(name)
            logger.setLevel(logging.INFO)

            fh = logging.FileHandler("%s.log" % name)
            fmt = '%(asctime)s - %(name)s - %(levelname)s - ' \
                  '%(message)s - {0}'.format(time)
            formatter = logging.Formatter(fmt)
            fh.setFormatter(formatter)
            logger.addHandler(fh)

            logger.info("Call function: %s" % name)
            result = func(*args, **kwargs)
            logger.info("Result: %s" % result)

        return inner_log

    return wrapper


@log
def double_function(a):
    return a * 2


@log(prefix='**********')
def double_function_extended(a):
    return a * 2


@extended_log(23)
def tripple_function(a):
    return a * 3


if __name__ == "__main__":
    value = double_function(2)
    value1 = double_function_extended(2)
    value2 = tripple_function(2)
