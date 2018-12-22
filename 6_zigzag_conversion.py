def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    dict_columns = {}
    n = 0
    while s != "":
        if n%(numRows-1) == 0:
            temp = [''] * numRows
            for i in range(numRows):
                if s == "":
                    break
                temp[i] = s[0]
                s = s[1:]
        else:
            temp = [''] * numRows
            temp[-n%(numRows-1)] = s[0]
            s = s[1:]
        dict_columns[n] = temp
        n += 1
    res = ""
    for i in range(numRows):
        for e in range(len(dict_columns)):
            res += dict_columns[e][i]
    return res

print(convert("PAYPALISHIRING",3))