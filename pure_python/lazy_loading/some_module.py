class ExapmleLoadingClass:
    """Example class for lay loading"""

    def __init__(self, number):
        self._number = number

    def __call__(self, *args, **kwargs):
        return self._number
