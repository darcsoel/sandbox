def digit_counts(k, n):
    letters = ''.join(str(x) for x in range(n))
    return letters.count(str(k))


k = 1
n = 11

print(digit_counts(k, n))
