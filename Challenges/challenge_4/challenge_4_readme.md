# Challenge 4
* Worked with [Nathan Pillai](https://github.com/natepill/Graph-Theory/tree/master/Challenges)

## Part 1: Solve the Knapsack Problem using Dynamic Programming.

### Resources:
* https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/



### 5 Steps of Dynamic Programming for Knapsack:

* 

## Part 2: The Edit Distance Problem using Dynamic Programming.
Credit given to [GeeksforGeeks](https://www.geeksforgeeks.org/edit-distance-dp-5/)

Problem is called 'edit distance', it determines how many changes needed to make two string exactly the same. using following operations:
1. Replace
2. Insert
3. Delete

### Example
```
Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a
```
### 5 Steps of Dynamic Programming for Edit Distance
* Should we insert, remove, or replace current character to get closer to equating the two strings

* We can start traversing the two strings from either left or right.

* We are taking the minimum number edits between inserting, removing, or replacing, current character

* Compute distance with memoization utilizing tabular reference table containing both string's values

* Return the minimum between the three edit choices (insert, remove, or replace)

