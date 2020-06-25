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


l = [1, 2, 3]
test_func2(l)
print(l)


def test_func3(list_par2):
    list_par2 = copy(list_par2)
    list_par2.append(1)
    print(list_par2)


l2 = [1, 2, 3]
test_func3(l2)
print(l2)
