class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiou"
        vowel_list = [c for c in s if c.lower() in vowels]
        print(vowel_list)
        vowel_list.sort(reverse=True)
        res = ""
        for c in s:
            if c.lower() in vowels:
                res += vowel_list.pop()
            else:
                res += c
        return res

if __name__ == '__main__':
    s = "lEetcode"
    print(Solution().sortVowels(s))