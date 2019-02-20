class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        true_group = []
        false_pair = []
        for equation in equations:
            var1 = equation[0]
            var2 = equation[3]
            if equation[1] == "=":
                done = False
                for group in true_group:
                    if var1 in group and var2 not in group:
                        group.append(var2)
                        done = True
                        break
                    elif var2 in group and var1 not in group:
                        group.append(var1)
                        done = True
                        break
                if not done:
                    true_group.append([var1, var2])
            else:
                if var1 == var2:
                    return False
                false_pair.append((var1, var2))
        for pair in false_pair:
            for group in true_group:
                if pair[0] in group and pair[1] in group:
                    return False
        return True
