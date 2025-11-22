from itertools import pairwise
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        prev = [-1, -1]
        ans = 0
        for interval in intervals:
            for a, b in pairwise(interval):
                # 包含前一个区间
                if a <= prev[0] and b >= prev[1]:
                    continue
                elif a <= prev[1]:
                    ans += 1
                else:
                    ans += 2
                prev = [a, b]
        return ans


if __name__ == '__main__':
    # [[1,3],[3,7],[8,9]]
    print(Solution().intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]))
