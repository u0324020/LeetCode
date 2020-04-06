# LeetCode
A LeetCode a day keep bugs away

2^X = N -> logN = X

logn < n < n^1/2 <nlogn < n^2 < 2^n < N!

# 1) Bubble Sort : 
依照序列順序，一次比較兩個元素，順序錯誤就將其交換<br>
 Worst Time: O(n^2)<br>
 Avg Time: O(n^2)<br>
 Best Time: O(n^2)<br>
 Space: O(1)<br>

# 2) Selection Sort : 
是將未排序的序列中選擇最小值放到已排序的序列中，依序將尚未排序的序列加入。<br>
 Worst Time: O(n^2)<br>
 Avg Time: O(n^2)<br>
 Best Time: O(n^2)<br>
 Space: O(1)<br>

# 3) Insert Sort : 
是依序在未排序的序列中將元素插入已排序的序列適當的位置。<br>
 Worst Time: O(n^2)<br>
 Avg Time: O(n^2)<br>
 Best Time: O(n^2)<br>
 Space: O(1)<br>

# 4) Merge Sort : 
屬於Divide and Conquer演算法，把問題先拆解(divide)成子問題，並在逐一處理子問題後，將子問題的結果合併(conquer)，如此便解決了原先的問題。<br>
 Worst Time: O(nlogn)<br>
 Avg Time: O(nlogn)<br>
 Best Time: O(nlogn)<br>
 Space: O(1)<br>

# 5) Quick Sort : 
會先隨機找一個基準元素，將小於該數之元素放在前面，大於該數之元素放在後面。再分別對兩類的序列做遞迴。<br>
 Worst Time: O(n^2)<br>
 Avg Time: O(nlogn)<br>
 Best Time: O(nlogn)<br>
 Space: O(1)<br>
 
 # 6) Binary Search Tree(BST)->Time O(logn), Space O(n): 
     1. Ordered, or sorted, binary trees.<br>
     2. Nodes can have 2 subtrees.<br>
     3. Items to the left of a given node are smaller.<br>
     4. Items to the right of a given node are larger.<br>
     - red-black tree(RB-Tree)<br>
     1. A node is either red or black<br>
     2. T root and leaves(NIL) are black.<br>
     3. If a node is red, the its children are black.<br>
     4. All paths from a node to its NIL descendants contain the same number of black nodes.<br>
     Ps. 1. Nodes require one storage bit to keep track of color.<br>
         2. The longest path(root to farthest NIL) is no more than twice the length of the shortest path(root to nearest NIL).<br>
     Binary Search Tree operations:<br>
     1. Search<br>
     2. Insert -> require rotation<br>
     3. Remove -> require rotation<br>
 # Big O of book
 1. 並排的for迴圈不管多少都是 = O(n)
 2. 巢狀迴圈 兩層for = O(n^2)
 3. for i in range(5):<br>
       for j in range(i+1,5):<br>
         do...<br>
    inner for loog 起始值與前一個相關就要分析: 1. Counting the Iterations 2. What It Means 3. Visualizing What It Does 4. Average Work<br>
   結果皆為O(n^2)
 4. 3個loop迴圈 其中一個是無關緊要的判斷 for i in range(10000)<br>
    O(n^2)
 5. 遞迴(Recursive Patten)<br>
    O(branches^depth) , branches = 一次分幾個遞迴
 6. return n * function(n-1) ->從n, n-1, n-2...., 1-> O(n)  
 7. Fibonacci -> O(branches^depth)-> O(2^n):<br>
    def fibonacci(n):<br>
       if n<=0 :<br>
         return 0<br>
       elif n==1 :<br>
         return 1<br>
       else:<br>
         return fibonacci(n-1) + fibonacci(n-2)

