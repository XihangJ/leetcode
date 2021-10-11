'''
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
'''
class Solution:
    #method 1. 2 pointers + hashmap. O(n), S(1)
    #Ex. fruits = [3,3,3,1,2,1,1,2,3,3,4]
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n <= 2: return n
        left, right = 0, 1
        d = {fruits[left]: 0}
        max_pick = 0
        while right < n:
            fruit = fruits[right]
            if fruit in d:
                #update fruit's end position
                d[fruit] = right
                max_pick = max(max_pick, right - left + 1)
            #if only 1 kind of fruit in baskets
            elif fruit not in d and len(d) < 2:
                d[fruit] = right
                max_pick = max(max_pick, right - left + 1)
            else:
                #replace one kind of fruit
                container, index = [[], []], 0
                for f in d:
                    container[index] = (f, d[f])
                    index += 1
                if container[0][1] < container[1][1]: 
                    throw = container[0][0]
                else: 
                    throw = container[1][0]
                left = d[throw] + 1
                d.pop(throw)
                d[fruit] = right
                max_pick = max(max_pick, right - left + 1)
            right += 1
        return max_pick
