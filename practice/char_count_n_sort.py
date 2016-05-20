__author__ = 'Ryan Cabrera'


def main():
    raw_values = ['a', 'z', 'c', 'a']
    unique_values = set(raw_values)
    values_and_counts = list(tuple())
    for items in unique_values:
        values_and_counts.append((items, raw_values.count(items)))

    values_and_counts = sorted(values_and_counts, key=lambda x: x[1], reverse=True)

    for item in values_and_counts:
        print(item)

if __author__:
    main()