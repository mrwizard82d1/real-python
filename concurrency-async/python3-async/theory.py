def odds(start, stop):
    """
    Produces a sequence of odd numbers between start and stop, inclusive.

    :param start: The first value of the sequence
    :param stop: The last value of the sequence
    :return: A generated sequence
    """

    for odd in range(start, stop + 1, 2):
        # `yield` will return a value and "pause>
        yield odd


def main():
    odd_values = [odd for odd in odds(3, 15)]
    print(odd_values)
    odds2 = tuple(odds(21, 29))
    print(odds2)


if __name__ == '__main__':
    main()
