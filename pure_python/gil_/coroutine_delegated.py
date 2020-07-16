from sys import exit


def average():
    total = 0
    count = 0

    while True:
        age = yield

        if age is None:
            break

        total += age
        count += 1

    return total / count


def grouper(records, key):
    while True:
        records[key] = yield from average()


def main(data: dict):
    results = {}

    for key, records in data.items():
        group = grouper(results, key)
        next(group)

        for record in records:
            group.send(record)

        group.send(None)

    print(results)


if __name__ == '__main__':
    data = {'first_age_set': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'second_age_set': [2, 3, 7, 4, 5, 6, 7, 8, 9],
            'third_age_set': [9, 8, 6, 2, 5, 6, 7, 8, 9]}

    main(data)
    exit()
