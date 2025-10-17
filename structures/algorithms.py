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



def quicksort_in_place(arr: List[int]) -> None:
    """
    In-place, non-recursive quicksort implementation.
    Sorts the list in place.
    Time Complexity: Average O(n log n), Worst-case O(n²)
    Space Complexity: O(log n)
    """
    if len(arr) <= 1:
        return
    stack = [(0, len(arr) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        stack.append((lo, i - 1))
        stack.append((i + 1, hi))


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


def mergesort_in_place(arr: List[int]) -> None:
    """
    In-place, non-recursive mergesort implementation.
    Sorts the list in place.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    n = len(arr)
    if n <= 1:
        return
    size = 1
    temp = [0] * n
    while size < n:
        for left_start in range(0, n, 2 * size):
            mid = min(left_start + size, n)
            right_end = min(left_start + 2 * size, n)
            i, j, k = left_start, mid, left_start
            while i < mid and j < right_end:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1
            while i < mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j < right_end:
                temp[k] = arr[j]
                j += 1
                k += 1
        arr[:n] = temp[:n]
        size *= 2


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


def factorial_iterative(n: int) -> int:
    """
    Compute factorial iterating. Raises ValueError for negative inputs.
    Space Complexity: O(1)
    Time Complexity: O(n)
    """
    if n < 0:
        raise ValueError("factorial not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


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


def fibonacci_iterative(n: int) -> int:
    """
    Compute nth Fibonacci number iteratively.
    Space Complexity: O(1)
    Time Complexity: O(n)
    """
    if n < 0:
        raise ValueError("fibonacci not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
