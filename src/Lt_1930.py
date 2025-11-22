class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # 对于每个字符，找出它在字符串中的第一次和最后一次出现位置
        # 然后统计在这两个位置之间有多少个不同的字符
        # 这些不同的字符就对应不同的回文子序列 (c, middle, c)
        print(f"输入: {s}")

        ans = 0

        # 对每个字母 'a' 到 'z'
        for c in 'abcdefghijklmnopqrstuvwxyz':
            # 找到字符c的第一次和最后一次出现位置
            left = s.find(c)
            right = s.rfind(c)

            # 如果字符出现过且不是相邻位置
            if left < right:
                # 统计left和right之间有多少个不同的字符
                middle_chars = set(s[left + 1:right])
                print(f"字符 {c} 的回文子序列: {middle_chars}")
                ans += len(middle_chars)

        return ans


if __name__ == '__main__':
    result = Solution().countPalindromicSubsequence("aabca")
