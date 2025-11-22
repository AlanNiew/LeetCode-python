from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # 可以被三整除
        ans = 0
        arr = [num for num in range(50) if num % 3 == 0]
        for num in nums:
            if num in arr:
                continue
            else:
                ans += 1
        return ans


if __name__ == '__main__':
    print(Solution().minimumOperations([1, 2, 3, 4]))
