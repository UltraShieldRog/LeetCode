def isPalindrome(x):
    """
    :type x: int
    :rtype: bool

    Optional: use an approach without converting the int to sr
    """
    if x < 0:
        return False
    # reverse it 
    rev = 0
    temp = x
    while temp != 0:
        rev *= 10
        rev += temp%10
        temp//= 10

    return rev == x
