import datetime


class DateGenerator:
    formats = []
    dates_count = 10

    def __new__(cls, *args, **kwargs):
        cls.min_year = datetime.datetime.now().year
        cls.max_year = datetime.datetime.now().year + 1

        if kwargs.get('formats'):
            cls.formats = kwargs.get('formats')

    @classmethod
    def generate(cls):
        return []
