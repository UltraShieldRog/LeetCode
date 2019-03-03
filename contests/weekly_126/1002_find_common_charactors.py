class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        dic = {}
        for char in A[0]:
            if char in dic.keys():   
                dic[char] += 1
            else:
                dic[char] = 1
        # check every word based on the first word
        for word in A:
            check_dic = {}
            for char in word:
                if char in check_dic.keys():   
                    check_dic[char] += 1
                else:
                    check_dic[char] = 1
            to_be_remove = set([])
            for key in dic:
                if key not in check_dic:
                    to_be_remove.add(key)
                    continue
                if dic[key] > check_dic[key]:
                    dic[key] = check_dic[key]
            if len(to_be_remove) == 0:
                continue
            for i in to_be_remove:
                dic.pop(i)
        # construct the result list
        res = []
        for char in dic:
            times = dic[char]
            while times > 0:
                res.append(char)
                times -= 1
        return res
