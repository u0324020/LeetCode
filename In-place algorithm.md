## In-place algorithm

In computer science, an in-place algorithm is an algorithm which transforms input using no auxiliary data structure. However, a small amount of extra storage space is allowed for auxiliary variables. The input is usually overwritten by the output as the algorithm executes. In-place algorithm updates input sequence only through replacement or swapping of elements. An algorithm which is not in-place is sometimes called not-in-place or out-of-place.

Usually, this space is O(log n), though sometimes anything in O(n) is allowed.

Quicksort operates in-place on the data to be sorted. However, quicksort requires O(log n) stack space pointers to keep track of the subarrays in its divide and conquer strategy.

python reverse
、class Solution:
	def reverseString(self, s: List[str]) -> None:
		s.reverse()、