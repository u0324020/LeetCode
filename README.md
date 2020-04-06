# LeetCode
A LeetCode a day keep bugs away


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
 
 # Big O of book
 1. 並排的for迴圈不管多少都是 = O(n)
 2. 巢狀迴圈 兩層for = O(n^2)
 3. for i in range(5):
       for j in range(i+1,5):
         do...
    inner for loog 起始值與前一個相關就要分析: 1. Counting the Iterations 2. What It Means 3. Visualizing What It Does 4. Average Work
   結果皆為O(n^2)
 4. 3個loop迴圈 其中一個是無關緊要的判斷 for i in range(10000)
    O(n^2)
 5. 遞迴(Recursive Patten)
    O(branches^depth) , branches = 一次分幾個遞迴
 6. return n * function(n-1) ->從n, n-1, n-2...., 1-> O(n)  
 7. Fibonacci -> O(branches^depth)-> O(2^n):
    def fibonacci(n):
       if n<=0 :
         return 0
       elif n==1 :
         return 1
       else:
         return fibonacci(n-1) + fibonacci(n-2)

