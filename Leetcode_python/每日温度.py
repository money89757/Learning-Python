 class Solution:
 	def dailyTemperatures(self,T):

 		n = len(T)
 		tmp = []
 		stack = [0 for i in range(n)]
 		for i in range(n):
 			while len(tmp) != 0 and T[i] > T[stack[-1]]:
 				res[tmp[-1]] = i - tmp[-1]
 				del tmp[-1]
 			tmp.append(i)

 		return res

 temp = Solution()
 T = [73, 74, 75, 71, 69, 72 76, 73]
 temp.dailyTemperatures(T)
