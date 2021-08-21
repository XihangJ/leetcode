'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
'''

class Solution:
    #method 1. BFS.
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000': return 0
        if '0000' in deadends: return -1
        deadends = set(deadends)
        directions = [1, -1]
        visited = set(['0000'])
        queue = collections.deque(['0000'])
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for i in range(4):
                    for direction in directions:
                        tmp_list = [slot for slot in curr]
                        tmp_list[i] = str((int(tmp_list[i]) + direction) % 10)
                        end = ''.join(tmp_list)
                        if end == target: 
                            return count
                        elif end not in visited and end not in deadends:
                            visited.add(end)
                            queue.append(end)
        return -1
