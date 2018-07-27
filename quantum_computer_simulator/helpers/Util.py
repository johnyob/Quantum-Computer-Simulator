def decimal_to_binary(n, i):
    """
    Converts i to a binary list that contains n bits

    :param n: total number of bits (integer)
    :param i: number to convert (integer)
    :return: (list)
    """

    return list(map(int, list(format(i, "0{0}b".format(n)))))
