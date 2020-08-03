from sys import exit


def some_func(list_=[]):
    list_.append(1) # mutate list parameter
    return list_


def param_muting(list_):
    #list_ = list_ + [1] #works fine
    list_[0] = 3 # mutate first element
    return list_


if __name__ == '__main__':
    first_list = [1, 2]
    first_result = some_func(first_list)
    second_result = some_func(first_list)

    second_list = [1, 2]
    third_result = param_muting(second_list)
    exit()
