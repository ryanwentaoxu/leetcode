class Solution:
    def helper(self, candidates, target):
        ans = []
        i = 0
        while i < len(candidates):
            count = i
            while count < len(candidates) and candidates[count] == candidates[i]:
                count += 1
            count -= 1
            for j in range(i, count + 1):
                if (j - i + 1) * candidates[i] < target and count + 1 < len(candidates):
                    for n in self.helper(candidates[count + 1:], target - (j - i + 1) * candidates[i]):
                        ans.append((j - i + 1) * [candidates[i]] + n)
                if (j - i + 1) * candidates[i] == target:
                    ans.append((j - i + 1) * [candidates[i]])
            i = count + 1
        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.helper(candidates, target)
