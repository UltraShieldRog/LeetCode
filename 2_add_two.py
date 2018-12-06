def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    def convert(node):
        if node.next is None:
            return node.val
        return node.val + 10 * convert(node.next)

    def set_digit(node, digit_counter):
        if digit_counter == 0:
            return
        digit_counter -= 1
        node.next = ListNode(int(str(new_num)[digit_counter]))
        set_digit(node.next, digit_counter)

    new_num = convert(l1) + convert(l2)

    digit_counter = len(str(new_num))-1
    result = ListNode(int(str(new_num)[digit_counter]))

    set_digit(result, digit_counter)
    return result
