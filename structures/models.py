from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """Simple LIFO stack."""

    def __init__(self) -> None:
        self._data: list[T] = []

    def push(self, item: T) -> None:
        """Push item onto the stack. O(1)."""
        self._data.append(item)

    def pop(self) -> T:
        """Remove and return the top item. Raises IndexError if empty. O(1)"""
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[T]:
        """Return top item without removing it, or None if empty. O(1)"""
        if not self._data:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:  # convenience
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        # Iterate from top to bottom
        return reversed(self._data).__iter__()


class Queue(Generic[T]):
    """Simple FIFO queue using collections.deque for O(1) enqueue/dequeue."""

    def __init__(self) -> None:
        self._data: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """Add item to the end of the queue. O(1)."""
        self._data.append(item)

    def dequeue(self) -> T:
        """Remove and return the front item. Raises IndexError if empty. O(1)"""
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Optional[T]:
        """Return front item without removing it, or None if empty. O(1)"""
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)


class LinkedListNode(Generic[T]):
    def __init__(self, value: T, next: Optional["LinkedListNode[T]"] = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"LinkedListNode({self.value!r})"


class PreviousAndCurrent(Generic[T]):
    def __init__(self,
                 previous: Optional[LinkedListNode[T]],
                 current: Optional[LinkedListNode[T]]) -> None:
        self.previous = previous
        self.current = current

    def __iter__(self):
        yield self.previous
        yield self.current

    def __getitem__(self, index: int) -> Optional[LinkedListNode[T]]:
        if index == 0:
            return self.previous
        elif index == 1:
            return self.current
        else:
            raise IndexError("Index out of range for PreviousAndCurrent")


class LinkedList(ABC, Generic[T]):
    """Singly linked list base class."""

    def __init__(self) -> None:
        self.head: Optional[LinkedListNode[T]] = None
        self.tail: Optional[LinkedListNode[T]] = None
        self._size = 0

    @abstractmethod
    def insert_first(self, value: T) -> None:
        """Insert value at the beginning of the list."""
        pass
    
    @abstractmethod
    def get_first(self) -> Optional[LinkedListNode[T]]:
        """Returns the first node in the list."""
        pass

    @abstractmethod
    def insert_last(self, value: T) -> None:
        """Insert value at the end of the list.."""
        pass

    @abstractmethod
    def get_last_node(self) -> Optional[LinkedListNode[T]]:
        """Traverses to and returns the last node in the list."""
        pass

    @abstractmethod
    def pop(self) -> Optional[LinkedListNode[T]]:
        """Remove and return the first node, or None if empty."""
        pass

    @abstractmethod
    def pop_left(self) -> Optional[LinkedListNode[T]]:
        """Remove and return the last node, or None if empty."""
        pass

    @abstractmethod
    def insert(self, index: int) -> Optional[LinkedListNode[T]]:
        """Insert value at the given index, or at the end if index >= size."""
        pass

    def _find_node_and_prev(
            self,
            value: T) -> PreviousAndCurrent[T]:
        """
        Traverses the list, returning the (previous node, current node)
        when the value is found, or (None, None) otherwise. O(n).
        """
        prev = None
        cur = self.head
        while cur:
            if cur.value == value:
                return PreviousAndCurrent(prev, cur)
            
            prev = cur
            cur = cur.next
        
        return PreviousAndCurrent(None, None)

    def find(self, value: T) -> Optional[LinkedListNode[T]]:
        """Return the first node with the given value, or None if not found. O(n)."""
        _, cur = self._find_node_and_prev(value)
        return cur

    def delete(self, value: T) -> bool:
        """Delete the first node with the given value. O(n)."""
        prev, cur = self._find_node_and_prev(value)

        if cur is None:
            return False

        if prev is None:
            # deleting head
            self.head = cur.next
        else:
            prev.next = cur.next

        self._size -= 1
        return True

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __repr__(self) -> str:
        return "LinkedList([" + ", ".join(repr(x) for x in self) + "])"


class SimpleLinkedList(LinkedList[T]):
    """Singly linked list with head."""

    def insert_first(self, value: T) -> None:
        """Insert value at the beginning of the list. O(1)."""
        node = LinkedListNode(value, self.head)
        self.head = node
        self._size += 1
    
    def get_first(self) -> Optional[LinkedListNode[T]]:
        """Returns the first node in the list. O(1)."""
        return self.head

    def get_last_node(self) -> Optional[LinkedListNode[T]]:
        """Traverses to and returns the last node in the list. O(n)."""
        if not self.head:
            return None
        
        cur = self.head
        while cur.next:
            cur = cur.next
        return cur

    def insert_last(self, value: T) -> None:
        """Insert value at the end of the list. O(n)."""
        node = LinkedListNode(value)
        cur = self.get_last_node()
        if not cur:
            self.head = node
        else:
            cur.next = node
        self._size += 1

    def pop(self) -> Optional[LinkedListNode[T]]:
        """Remove and return the first node, or None if empty. O(1)"""
        if self.head is None:
            return None
        else:
            node = self.head
            self.head = self.head.next
            self._size -= 1
            return node
    
    def pop_left(self) -> Optional[LinkedListNode[T]]:
        """Remove and return the last node, or None if empty. O(n)"""
        if self.head is None:
            return None
        if self.head.next is None:
            node = self.head
            self.head = None
            self._size = 0
            return node

        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        node_to_pop = cur.next
        cur.next = None
        self._size -= 1
        return node_to_pop



class TailedLinkedList(LinkedList[T]):
    """Singly linked list with head and tail."""

    def insert_first(self, value: T) -> None:
        """Insert value at the beginning of the list. O(1)."""
        node = LinkedListNode(value, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1
    
    def get_first(self) -> Optional[LinkedListNode[T]]:
        """Returns the first node in the list. O(1)."""
        return self.head

    def get_last_node(self) -> Optional[LinkedListNode[T]]:
        """Traverses to and returns the last node in the list. O(1)."""
        return self.tail

    def insert_last(self, value: T) -> None:
        """Insert value at the end of the list. O(1)."""
        node = LinkedListNode(value, self.head)
        if self.head is None:
            self.insert_first(value)
        else:
            self.tail.next = node
            self.tail = node
            self._size += 1

    def pop(self) -> Optional[LinkedListNode[T]]:
        """Remove and return the first node, or None if empty. O(1)"""
        if self.head is None:
            return None
        elif self.head.next is None:
            node = self.head
            self.head = None
            self.tail = None
            self._size = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self._size -= 1
            return node

    def pop_left(self) -> Optional[LinkedListNode[T]]:
        """Remove and return the last node, or None if empty. O(n)"""
        if self.head is None:
            return None
        if self.head.next is None:
            node = self.head
            self.head = None
            self.tail = None
            self._size = 0
            return node

        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        node_to_pop = self.tail
        cur.next = None
        self.tail = cur
        self._size -= 1
        return node_to_pop
