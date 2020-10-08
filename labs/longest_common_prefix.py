import sys
import typing as t


def prefix_search(strings: t.Union[list, tuple, set]):
    prefix = ''

    if not strings:
        return prefix

    for s in strings:
        if not isinstance(s, str):
            raise ValueError('Can not find prefix. '
                             'All iterable elements must be string')

        if not s == s.lower() or not s.isalpha():
            raise ValueError("Elements must contain only lowercase letters")

    strings.sort(key=len)

    for i in range(len(strings[0])):
        prefix_local = strings[0][:i]
        contain = []
        for s in strings:
            try:
                s.index(prefix_local)
                contain.append(True)
            except ValueError:
                contain.append(False)

        if all(contain):
            prefix = prefix_local
        else:
            break

    return prefix


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(prefix_search(strs))
    sys.exit()
