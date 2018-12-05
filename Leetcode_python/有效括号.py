class Solution:
    def isValid(self,s):
        """
        :type s: str
        :return: bool
        """
        str = []
        for i in s:
            if i in '([{':
                str.append(i)
            elif i in ')]}':
                if len(str) < 1:
                    return False
                tmp = str.pop()
                if (tmp == '(' and i == ')') or (tmp == '[' and i == ']') or (tmp == '{' and i == '}'):
                    pass
                else:
                    return False
        if len(str) > 0:
            return False
        return True

solution = Solution()
solution.isValid('{]')