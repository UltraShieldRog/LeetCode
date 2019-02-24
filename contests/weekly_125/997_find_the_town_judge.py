class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        dic = {} # be trusted by somebody
        dic2 = {} # trust somebody
        for i in range(1,N+1):
            dic[i] = []
            dic2[i] = []
        for relation in trust:
            dic[relation[1]].append(relation[0])
            dic2[relation[0]].append(relation[1])
        # print(dic)
        # print(dic2)
        res = []
        for i in dic.items():
            if len(i[1]) == N-1:
                res.append(i[0])
        new_res = []
        for candidate in res:
            # print(candidate)
            if len(dic2[candidate]) == 0:
                new_res.append(candidate)
        if len(new_res) != 1:
            return -1
        else:
            return new_res[0]
