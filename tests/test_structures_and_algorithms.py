import pytest

from structures.models import Stack, Queue, SimpleLinkedList, TailedLinkedList
from structures.algorithms import (
    binary_search,
    binary_search_recursive,
    quicksort,
    quicksort_in_place,
    mergesort,
    factorial_recursive,
    fibonacci_recursive,
)


def test_stack():
    # Empty stack
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
    # Empty peek
    s = Stack()
    assert s.peek() is None
    # Normal operations
    s = Stack[int]()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert not s.is_empty()
    assert s.peek() == 2
    assert len(s) == 2
    assert s.pop() == 2
    assert s.pop() == 1
    with pytest.raises(IndexError):
        s.pop()

def test_queue():
    # Empty queue
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()
    # Empty peek
    q = Queue()
    assert q.peek() is None
    # Normal operations
    q = Queue[str]()
    assert q.is_empty()
    q.enqueue("a")
    q.enqueue("b")
    assert q.peek() == "a"
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    with pytest.raises(IndexError):
        q.dequeue()

def test_simple_linked():
    # Empty list
    ll = SimpleLinkedList[int]()
    assert len(ll) == 0
    assert ll.find(1) is None
    assert not ll.delete(1)
    # Insertions
    ll = SimpleLinkedList[int]()
    ll.insert_first(1)
    ll.insert_last(2)
    ll.insert_first(0)
    assert list(ll) == [0, 1, 2]
    # Find
    assert ll.find(1) is not None
    assert ll.find(5) is None
    # Deletions
    assert ll.delete(1) is True
    assert list(ll) == [0, 2]
    assert ll.delete(99) is False

def test_tailed_linked():
    # Empty list
    ll = TailedLinkedList[int]()
    assert len(ll) == 0
    assert ll.find(1) is None
    assert not ll.delete(1)
    # Insertions
    ll = TailedLinkedList[int]()
    ll.insert_first(1)
    ll.insert_last(2)
    ll.insert_first(0)
    assert list(ll) == [0, 1, 2]
    # Find
    assert ll.find(1) is not None
    assert ll.find(5) is None
    # Deletions
    assert ll.delete(1) is True
    assert list(ll) == [0, 2]
    assert ll.delete(99) is False

def test_binary_search():
    # Empty
    assert binary_search([], 1) == -1
    # Single
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1
    # Duplicates
    arr_dup = [1, 2, 2, 2, 3]
    assert binary_search(arr_dup, 2) in {1,2,3}
    # Negatives
    arr_neg = [-5, -2, 0, 3]
    assert binary_search(arr_neg, -2) == 1
    # Found and Not Found
    arr = [1, 3, 4, 7, 9, 10]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 2) == -1

def test_binary_search_recursive():
    # Empty
    assert binary_search_recursive([], 1) == -1
    # Single
    assert binary_search_recursive([1], 1) == 0
    assert binary_search_recursive([1], 2) == -1
    # Duplicates
    arr_dup = [1, 2, 2, 2, 3]
    assert binary_search_recursive(arr_dup, 2) in {1,2,3}
    # Negatives
    arr_neg = [-5, -2, 0, 3]
    assert binary_search_recursive(arr_neg, -2) == 1
    # Found and Not Found
    arr = [1, 3, 4, 7, 9, 10]
    assert binary_search_recursive(arr, 7) == 3
    assert binary_search_recursive(arr, 2) == -1

def test_quicksort():
    # Emtpy
    assert quicksort([]) == []
    # Single
    assert quicksort([1]) == [1]
    # Duplicates
    assert quicksort([2,2,2]) == [2,2,2]
    # Negatives
    assert quicksort([-1,0,1]) == [-1,0,1]
    # Sorted
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # Reverse
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    # Mixed
    unsorted = [5, 3, 8, 1, 2, 9, 5]
    assert quicksort(unsorted) == sorted(unsorted)
    # Invalid type
    with pytest.raises(TypeError):
        quicksort(None)

def test_quicksort_in_place():
    # Empty
    arr = []
    quicksort_in_place(arr)
    assert arr == []
    # Single
    arr = [1]
    quicksort_in_place(arr)
    assert arr == [1]
    # Duplicates
    arr = [2, 2, 2]
    quicksort_in_place(arr)
    assert arr == [2, 2, 2]
    # Negatives
    arr = [-1, 0, 1]
    quicksort_in_place(arr)
    assert arr == [-1, 0, 1]
    # Sorted
    arr = [1, 2, 3, 4, 5]
    quicksort_in_place(arr)
    assert arr == [1, 2, 3, 4, 5]
    # Reverse
    arr = [5, 4, 3, 2, 1]
    quicksort_in_place(arr)
    assert arr == [1, 2, 3, 4, 5]
    # Mixed
    arr = [5, 3, 8, 1, 2, 9, 5]
    quicksort_in_place(arr)
    assert arr == sorted([5, 3, 8, 1, 2, 9, 5])

def test_mergesort():
    # Empty
    assert mergesort([]) == []
    # Single
    assert mergesort([1]) == [1]
    # Duplicates
    assert mergesort([2,2,2]) == [2,2,2]
    # Negatives
    assert mergesort([-1,0,1]) == [-1,0,1]
    # Sorted
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # Reverse
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    # Mixed
    unsorted = [5, 3, 8, 1, 2, 9, 5]
    assert mergesort(unsorted) == sorted(unsorted)
    # Invalid type
    with pytest.raises(TypeError):
        mergesort(None)

def test_factorial_recursive():
    # Zero and One
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    # Positive
    assert factorial_recursive(5) == 120
    assert factorial_recursive(10) == 3628800
    # Negative
    with pytest.raises(ValueError):
        factorial_recursive(-1)
    # Invalid type
    with pytest.raises(TypeError):
        factorial_recursive('a')

def test_fibonacci_recursive():
    # Zero and One
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    # Positive
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(10) == 55
    # Negative
    with pytest.raises(ValueError):
        fibonacci_recursive(-2)
    # Invalid type
    with pytest.raises(TypeError):
        fibonacci_recursive('a')
