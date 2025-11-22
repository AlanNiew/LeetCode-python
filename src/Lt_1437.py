from itertools import count, pairwise
from lzma import compress
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        size = len(nums)
        start = 0
        # 找起始位置
        for start in range(size):
            if nums[start] == 1:
                break
            start+=1
        fast = start+1
        slow = start
        while fast < size:
            while fast < size and nums[fast] != 1 :
                fast+=1
            if fast >= size:
                break
            n = fast - slow - 1
            if n < k:
                return False
            slow = fast
            fast+=1
        return True
if __name__ == '__main__':
    nums = [1,0,0,0,1,0,0,1]
    for i,num in enumerate(nums):
        if num == 1:
            print(i,num)
    # indices = [i for i, num in enumerate(nums) if num == 1]
