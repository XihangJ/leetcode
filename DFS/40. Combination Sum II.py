'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''

class Solution:
  
    # O(N * 2**N), S(N)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        visited = [False for _ in range(len(candidates))]
        def backtrack(start, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return
            elif curr_sum > target: return
            
            for i in range(start, len(candidates)):
                if i > 0 and candidates[i-1] == candidates[i] and visited[i-1] == False:
                    continue
                curr_sum += candidates[i]
                curr.append(candidates[i])
                visited[i] = True
                backtrack(i + 1, curr, curr_sum)
                visited[i] = False
                curr.pop()
                curr_sum -= candidates[i]
            
        res = []
        candidates.sort()
        backtrack(0, [], 0)
        return res
