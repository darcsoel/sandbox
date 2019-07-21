class CustomIterator:
    def __init__(self, values_to_iter: (list, tuple, set, dict, str)):
        self.__values_to_iter = values_to_iter
        self.__current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index == len(self.__values_to_iter):
            raise StopIteration

        index = self.__current_index
        self.__current_index += 1
        return self.__values_to_iter[index]


values = [1, 2, 3, 4, 5, 6, 7]

iterator = CustomIterator(values)

print(iterator)
print(list(iterator))
