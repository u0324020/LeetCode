# LeetCode
演算法是解決一問題的有限步驟，程式的效率一般是利用Big-O做評估，
A LeetCode a day keep bugs away

2^X = N -> logN = X
在N夠大的前提下:
1 < logn < n^1/2 < n < nlogn < n^2 < 2^n < N!

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
 
 # 6) Heap Sort : 
 Binary Heap可以分為Min Heap與Max Heap兩種<br>
 特徵一：Binary Heap之結構可以視作Complete Binary Tree<br>
 特徵二：若將位於index(i)之node視為subtree之root，那麼，可將此Binary Heap分為max, min heap<br>
 作法(Max-heap)：<br>
 1. 先從Array建立Binary Tree<br>
 2. Binary Tree root開始跟nodes比較將大的交換<br>
 3. 遍歷後最大Node就會跑到root<br>
 4. 再把root跟最尾端的node交換<br>
 5. 把最尾端的node(max)提出到heap sort array中<br>
 再重複2 to 5直到Tree空了為止，heap sort array就是max-heap sort<br>
 Worst Time: O(nlogn)<br>
 Avg Time: O(nlogn)<br>
 Best Time: O(nlogn)<br>
 Space: O(1)<br>
 
 # 7) Binary Search Tree(BST)->Time O(logn), Space O(n): 
     1. Ordered, or sorted, binary trees.
     2. Nodes can have 2 subtrees.
     3. Items to the left of a given node are smaller.
     4. Items to the right of a given node are larger.
     - red-black tree(RB-Tree)
     1. A node is either red or black
     2. T root and leaves(NIL) are black.
     3. If a node is red, the its children are black.
     4. All paths from a node to its NIL descendants contain the same number of black nodes.
     Ps. 1. Nodes require one storage bit to keep track of color.
         2. The longest path(root to farthest NIL) is no more than twice the length of the shortest path(root to nearest NIL).
     Binary Search Tree operations:
     1. Search
     2. Insert -> require rotation
     3. Remove -> require rotation
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
         
# Array in Python
一維串列: A = [None]* 20
二維串列: A = [[None]* 10 for rows in range(20)]
三維串列: A = [[[None for z in range(10)]for x in range(20)]for y in range(30)]

# Python
1. https://blog.kdchang.cc/2017/08/15/learning-programming-and-coding-with-python-list-tuple-dict-set/
2. Dict https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-533b8d8d96f3

# 三種 Interative Binary Tree Traversal 的方法 (In-Order, Pre-Order and Post-Order)
pre-, in-, post-是指parent node相對於child node的順序<br>
preorder: 中->左->右<br>
inorder: 左->中->右<br>
postorder: 左->右->中<br>


