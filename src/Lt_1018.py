from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        prefix = 0
        # 每次左移一位，相当于乘以2
        for num in nums:
            prefix = (prefix * 2 + num) % 5
            result.append(prefix == 0)
        return result


if __name__ == '__main__':
    print(Solution().prefixesDivBy5([1, 0, 1]))
