# Challenge 4
* Worked with [Nathan Pillai](https://github.com/natepill/Graph-Theory/tree/master/Challenges)

## Part 1: Solve the Knapsack Problem using Dynamic Programming.

### Resources:
* https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

## Description
The knapsack problem or rucksack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.[wiki](https://en.wikipedia.org/wiki/Knapsack_problem)

### 5 Steps of Dynamic Programming for Knapsack:

* Step 1 - Identifying sub problems
In order to find which items we need to put in the bag, we can start with 1 item at a time, and check if it exeeds the limit or not.

* Step 2 - Guess the first choice
Adding any first item would be a choice since we dont really know how many items or which items we are going to put in. Just start with arbitrary item.

* Step 3 - Recursively define the value of an optimal solution
We call the function with 2 option either we put the item or dont put the item in the back pack and copmare the value and get the max of two cases. it looks like this in code:
```python
no_item = knapsack(capacity, items, n-1)
in_item = items[n-1][2] + knapsack((capacity - items[n-1][1]), items, n-1)
``` 

* Step 4 - Compute the optimal solution
From step 3 we pick the max out of two option
```python
return max(in_item, no_item)
```

* Step 5 - Solve the original problem.
For each iteration it returns fuction returns the optimal value and from step 3 and 4, then we build back up the recursion tree to get the solution for original problem.
```python
return max(in_item, no_item)
```


## Part 2: The Edit Distance Problem using Dynamic Programming.
Credit given to [GeeksforGeeks](https://www.geeksforgeeks.org/edit-distance-dp-5/)

### Description
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
* Step 1 - Identifying sub problems
Should we insert, remove, or replace current character to get closer to equating the two strings

* Step 2 - Guess the first choice
We can start traversing the two strings from either left or right.

* Step 3 - Recursively define the value of an optimal solution
We are taking the minimum number edits between inserting, removing, or replacing, current character

* Step 4 - Compute the optimal solution
Compute distance with memoization utilizing tabular reference table containing both string's values

* Step 5 - Solve the original problem.
Return the minimum between the three edit choices (insert, remove, or replace)

