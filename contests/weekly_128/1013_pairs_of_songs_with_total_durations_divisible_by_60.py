from math import factorial as f 
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time_simp = list(map(lambda x: x % 60, time))
        time_simp.sort()
        dic = {}
        for i in time_simp:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        counter = 0
        for i in range(1,30):
            if i not in dic.keys() or (60-i) not in dic.keys():
                continue
            counter += dic[i] * dic[60-i]
        if 0 in dic.keys():
            num = dic[0]
            if num >= 2:
                counter += f(num)//(f(num-2)*f(2)) # n choose 2
        if 30 in dic.keys():
            num = dic[30]
            if num >= 2:
                counter += f(num)//(f(num-2)*f(2)) # n choose 2
        return counter
