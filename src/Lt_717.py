from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        #         前缀匹配
        size = len(bits)
        bit1 = [0]
        bit2 = [10, 11]
        ans = [0 for _ in range(size)]
        # 成对匹配
        index = 0
        while index < size:
            if bits[index] in bit1:
                ans[index] = 1
                index += 1
                continue
            if bits[index] * 10 + bits[index + 1] in bit2:
                ans[index] = 2
                index += 2
                continue
        print(ans)
        return ans[size - 1] == 1


if __name__ == '__main__':
    print(Solution().isOneBitCharacter([1, 0, 0]))
