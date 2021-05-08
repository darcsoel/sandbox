from copy import copy


def test_func(par):
    par += 1
    print(par)


x = 1
test_func(x)
print(x)


def test_func2(list_par):
    list_par.append(1)
    print(list_par)


list_ = [1, 2, 3]
test_func2(list_)
print(list_)


def test_func3(list_par2):
    list_par2 = copy(list_par2)
    list_par2.append(1)
    print(list_par2)


l2 = [1, 2, 3]
test_func3(l2)
print(l2)


def some_foo_func(a, b, first=None, second=None):
    return True


some_foo_func(1, 2, 3, 4)
some_foo_func(a=1, b=2, first=3, second=4)
