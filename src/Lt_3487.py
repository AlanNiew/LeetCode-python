from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_sort = sorted(nums)
        print(nums_sort)
        return len(nums)


def mutily(factory):
    def computer(x):
        return x * factory
    return computer
doub = mutily(2)
print(doub(10))
