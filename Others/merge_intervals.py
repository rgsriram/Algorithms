class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        new_list = sorted(intervals, key=lambda x: x.start)

        for each in new_list:
            print(each.start)


Solution().merge(intervals)