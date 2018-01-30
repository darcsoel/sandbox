class BMW(object):
    def __init__(self, model, price):
        self.price = price
        self.model = model
        self.name = 'BMW'

    def __str__(self):
        return '{0} {1} ({2})'.format(self.name, self.model, self.price)

