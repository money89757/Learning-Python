class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        #设置一个存放字符串的字典
        start = maxLength = 0
        #start记录子字符串的起始位置，maxLength记录最长字符串的长度
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
                #如果检索到出现过的字符，则子字符串的其实位置从上次记录的字符
                #后开始，以保证新的子字符串没有重复字符
            else:
                maxLength = max(maxLength, i - start + 1)
            used[s[i]] = i
        print(maxLength)
        return maxLength



str = Solution()
str.lengthOfLongestSubstring("abcabcbb")
str.lengthOfLongestSubstring("bbbbb")
str.lengthOfLongestSubstring("pwwkew")
str.lengthOfLongestSubstring("aaaa")