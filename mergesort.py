import sys


def merge_count(left, right):
    """
    Merge two sorted lists into a single sorted list, counting
    the number of cross-inversions (split inversions).

    A cross-inversion occurs when an element from the right list
    is smaller than an element from the left list. When we pick
    an element from right, every remaining element in left is
    inverted with it, so we add len(left) - i to the count.

    Args:
        left: A sorted list of integers
        right: A sorted list of integers

    Returns:
        A tuple (merged_list, inversion_count)
    """
    result = []
    inversions = 0
    i = 0  # pointer into left
    j = 0  # pointer into right

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inversions += len(left) - i
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, inversions


def sort_count(lst):
    """
    Sort a list and count the total number of inversions using
    a modified Mergesort (divide and conquer).

    An inversion is a pair (i, j) where i < j but lst[i] > lst[j].

    Args:
        lst: A list of integers

    Returns:
        A tuple (sorted_list, inversion_count)
    """
    # Base case: a list of length 0 or 1 has no inversions
    if len(lst) <= 1:
        return lst, 0

    mid = len(lst) // 2

    # Recursive case: count inversions in each half, then count
    # cross-inversions during merge
    left, left_inversions = sort_count(lst[:mid])
    right, right_inversions = sort_count(lst[mid:])
    merged, split_inversions = merge_count(left, right)

    return merged, left_inversions + right_inversions + split_inversions


def main():
    line = sys.stdin.read().strip()
    elements = [int(x) for x in line.split(',')]

    _, count = sort_count(elements)
    print(count)


if __name__ == "__main__":
    main()
