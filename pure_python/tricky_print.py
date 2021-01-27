import dis

x = 0
y = 0


def f():
    x = 1
    y = 1

    class C:
        print(x, y)
        x = 2
        # y=2


f()
# 0 1

dis.dis(f)
