from __future__ import annotations

from typing import List, Sequence, Optional


def binary_search(sorted_list: Sequence[int], target: int) -> int:
    """
    Perform binary search on a sorted sequence of integers.
    Returns the index of target, or -1 if not found.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    lo = 0
    hi = len(sorted_list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = sorted_list[mid]
        if val == target:
            return mid
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_recursive(
        sorted_list: Sequence[int],
        target: int,
        lo: int = 0,
        hi: Optional[int] = None) -> int:
    """
    Perform binary search recursively on a sorted sequence of integers.
    Returns the index of target, or -1 if not found.
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """
    if hi is None:
        hi = len(sorted_list) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    val = sorted_list[mid]
    if val == target:
        return mid
    elif val < target:
        return binary_search_recursive(sorted_list, target, mid + 1, hi)
    else:
        return binary_search_recursive(sorted_list, target, lo, mid - 1)


def quicksort(unsorted_list: Sequence[int]) -> List[int]:
    """
    Return a new sorted list using quicksort.
    Time Complexity: Average O(n log n), Worst-case O(n²)
    Space Complexity: Average O(log n), Worst-case (this) O(n)
    """
    list_lenght = len(unsorted_list)
    if list_lenght <= 1:
        return list(unsorted_list)
    pivot = unsorted_list[list_lenght // 2]
    left = [x for x in unsorted_list if x < pivot]
    middle = [x for x in unsorted_list if x == pivot]
    right = [x for x in unsorted_list if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def mergesort(unsorted_list: Sequence[int]) -> List[int]:
    """
    Return a new sorted list using mergesort.
    Time Complexity: Average O(n log n)
    Space Complexity: O(n)
    """
    list_lenght = len(unsorted_list)
    if list_lenght <= 1:
        return list(unsorted_list)

    mid = list_lenght // 2
    left = mergesort(unsorted_list[:mid])
    right = mergesort(unsorted_list[mid:])

    # merge
    i = j = 0
    merged: List[int] = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged


def factorial_recursive(n: int) -> int:
    """
    Compute factorial recursively. Raises ValueError for negative inputs.
    Space Complexity: O(n)
    Complexity: O(n)
    """
    if n < 0:
        raise ValueError("factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n: int) -> int:
    """
    Compute nth Fibonacci number recursively.
    Space Complexity: O(2^n)
    Complexity: O(n)
    """
    if n < 0:
        raise ValueError("fibonacci not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
