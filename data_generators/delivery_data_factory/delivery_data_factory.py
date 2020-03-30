import re

from faker import Faker


class GeneratorAbstractFactory:
    prefix_data_count = 10
    main_data_count = 10
    delivery_points = 1
    postfix_data_count = 10
    locales = ['en-US', 'en_US']

    def __init__(self):
        self._faker = Faker(self.locales)
        self._features = []
        self._labels = []

        self._strip_pattern = r'\s'
        self._strip_replace_pattern = ' '

    def _generate_prefix(self):
        raise NotImplementedError

    def _generate_main_part(self):
        raise NotImplementedError

    def _generate_postfix(self):
        raise NotImplementedError

    def _clear_address_data(self, address):
        return re.sub(self._strip_pattern, self._strip_replace_pattern, address)

    def add_feature_and_label(self, feature, label):
        self._features.append(feature)
        self._labels.append(label)
        return self

    def generate(self) -> (list, list):
        """Generate test/train data. Return feature list and label list"""

        self._generate_prefix()
        return self._features, self._labels


class SimpleDataFactory(GeneratorAbstractFactory):
    prefix_data_count = 5
    postfix_data_count = 5

    def _generate_main_part(self):
        return self

    def _generate_prefix(self):
        address = self._faker.address()
        address = self._clear_address_data(address)

        company = self._faker.company()
        date = self._faker.date()

        return self

    def _generate_postfix(self):
        return self
