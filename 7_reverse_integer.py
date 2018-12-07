def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    x = str(x)
    res = ''
    nega = 0
    if x[0] == '-':
        x = x[1:]
        nega = 1

    for e in x:
        res = e + res

    if nega:
        res = '-' + res

    res = int(res)
    if res > 2 ** 31 - 1 or res < - 2 ** 31:
        return 0
    return res
