# Algorithm-course
## week1-p1-3
Given a set S of n integers, and another number M, we want to determine
whether or not there exist 2 numbers in S whose sum is exactly M. The algorithm
of testing all possible 2 numbers in S will take O(n
2
) time and it is unacceptable.

a) Design a more efficient algorithm for solving this problem. Analyze the time
complexity of your algorithm.

b) Extend your algorithm for the following case: determine whether or not there
exist 3 numbers in S whose sum is exactly M.

> Use ```HashTable``` to finish
## week2-p3
How to implement merge-sort such that the extra space used is about n/2 where n
is the number of input elements?
> Use ```list.append``` to finish
> ![example week2](/week2/merge_sort_revisespace.png =718x1279)
## week3-p1
Given a sorted array A[1...n] of n distinct integers, you want to find out the index
i for which A[i] = i if it exists. Please design a Divide-and-Conquer algorithm that
runs in time O(lgn). (Analyze your algorithm and show it is correct.)
## week4-p4
**Inversions**

Let A[1....n] be an array of n distinct numbers. If i<j and A[i] > A[j], then the
pair (i,j) is called an ```inversion``` of A.

a) List the five inversions of the array 〈3,8,6,1,
42〉.

b) What array with elements from the set ｛1,2 . . . . ,n｝has the most inversions?
How many does it have?

c) What is the relationship between the running time of insertion sort and the
number of inversions in the input array? Justify your answer.

d) Give an algorithm that determines the number of inversions in any permutation
on n elements in θ(nlogn) worst-case time. (Hint: Modify merge sort.)
## week4-p8
Directly solve the origin stock buying problem in θ(n) time. 