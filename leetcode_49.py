class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        freq = {}
        for i in range(len(strs)):
            tmp = list(strs[i].strip())
            tmp.sort()
            tmp = Counter(tmp)
            sear = ""
            for k, v in tmp.items():
                sear += (k + "," + str(v) + ",")
            if freq.get(sear, -1) == -1:
                freq[sear] = [strs[i]]
            else:
                freq[sear].append(strs[i])
        ans = []
        for k, v in freq.items():
            ans.append(v)
        return ans
