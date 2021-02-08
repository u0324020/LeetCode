'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

#in-place problem 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

'''
class Soultion:
	def reverseString(self, s: List[str])-> None:
		def helper(left, right):
			s[left], s[right] = s[right], s[left]
			helper(left+1, right-1)
		helper(0, len(s)-1)

	def reverseString_Python(self, s: List[str])-> None:
		s.reverses()