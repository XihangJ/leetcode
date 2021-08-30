'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
'''

class Solution:
    #method 1. sort. O(nlogn), S(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1: return 1
        begin = []
        end = []
        for interval in intervals:
            begin.append(interval[0])
            end.append(interval[1])
        begin.sort()
        end.sort()
        
        i_begin, i_end, rooms, curr_rooms = 0, 0, 0, 0
        while i_begin < len(intervals) and i_end < len(intervals):
            if begin[i_begin] < end[i_end]:
                curr_rooms += 1
                rooms = max(curr_rooms, rooms)
                i_begin += 1
            else:
                curr_rooms -= 1
                rooms = max(curr_rooms, rooms)
                i_end += 1
        return rooms
