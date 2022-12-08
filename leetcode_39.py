class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                ans.append([candidates[i]])
            elif candidates[i] < target:
                count = 1
                while count * candidates[i] < target:
                    for n in self.combinationSum(candidates[i+1:], target - count * candidates[i]):
                        ans.append([candidates[i]] * count + n)
                    count += 1
                if target % candidates[i] == 0:
                    ans.append([candidates[i]] * int(target / candidates[i]))
        return ans
