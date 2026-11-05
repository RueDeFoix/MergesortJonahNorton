# Counting Inversions with Mergesort

## Assignment Instructions

Your task is to complete the `mergesort.py` file by filling in the missing code in two functions: `merge_count` and `sort_count`.

## Problem Description

An **inversion** in a list is a pair of indices $(i, j)$ where $i < j$ but $a_i > a_j$ — in other words, a pair of elements that are "out of order."

For example, the list `[2, 4, 1, 3, 5]` has **3 inversions:** $(2,1)$, $(4,1)$, and $(4,3)$.

Counting inversions is useful for measuring how far a list is from sorted. A sorted list has 0 inversions; a reverse-sorted list of $n$ elements has $\binom{n}{2} = n(n-1)/2$ inversions (the maximum).

**Applications:**
- **Recommendation systems:** If two users rank $n$ movies, the number of inversions between their rankings measures how different their preferences are (this is related to the Kendall tau distance)
- **Computational biology:** Measuring similarity between gene orderings across species

### The naive approach

Check all $\binom{n}{2}$ pairs — this takes $O(n^2)$ time.

### The divide and conquer approach

We can count inversions in $O(n \log n)$ by modifying Mergesort. The key insight is that inversions come in three types:

1. **Left inversions:** both elements are in the left half
2. **Right inversions:** both elements are in the right half
3. **Split inversions:** one element in the left half, one in the right

The recursive calls handle types 1 and 2. The merge step handles type 3: when we pick an element from the right list (because it's smaller), every remaining element in the left list forms an inversion with it.

## Your Task

Complete the `mergesort.py` file by replacing the comments `# your code goes here` with the correct code. There are two gaps to fill:

1. **In `merge_count`:** When an element from the right list is smaller than the current element from the left list, count the inversions and advance the right pointer. The number of inversions contributed is the number of remaining elements in the left list.

2. **In `sort_count`:** Write the recursive case. You have `mid` already computed. Recursively sort and count each half, then merge-count, and return the combined result.

**Note:** The template uses `pass` statements as placeholders. Delete `pass` and write your own code in its place.

## Input/Output Format

### Input Format
A single line containing integers separated by commas (no spaces):

```
2,4,1,3,5
```

### Output Format
A single integer: the total number of inversions.

```
3
```

## Testing Your Solution

```bash
echo "2,4,1,3,5" | python3 mergesort.py
```

Expected output:
```
3
```

Another test — a reverse-sorted list of 5 elements has $\binom{5}{2} = 10$ inversions:

```bash
echo "5,4,3,2,1" | python3 mergesort.py
```

Expected output:
```
10
```

A sorted list has 0 inversions:

```bash
echo "1,2,3,4,5" | python3 mergesort.py
```

Expected output:
```
0
```

## Submission

Submit your completed `mergesort.py` file. The auto-grader will test your solution by running the file and checking the output.

## How to Submit

For complete instructions on submitting assignments with GitHub Classroom (including how to use Codespaces), see: [Submission Instructions](https://github.com/michaelsoltys/IAA/blob/main/Assignments/instructions.md)
