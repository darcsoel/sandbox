from factory.Audi import Audi
from factory.BMW import BMW


class CarFactory(object):
    @staticmethod
    def create(type):
        if type == 'Audi':
            return Audi('A8', 15000)
        if type == 'BMW':
            return BMW('750', 4000)

