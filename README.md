
# Data Structures and Algorithms Challenge

This project implements classic data structures and fundamental algorithms in Python, with a focus on internal workings, complexity, and best coding practices.

## Data Structures

### Stack
- **Operations:** `push`, `pop`, `peek`, `is_empty`
- **How it works:** Follows Last-In-First-Out (LIFO) principle. Items are added and removed from the top.
- **Complexity:**
	- `push`, `pop`, `peek`, `is_empty`: O(1) time, O(n) space (n = number of elements)

### Queue
- **Operations:** `enqueue`, `dequeue`, `peek`, `is_empty`
- **How it works:** Follows First-In-First-Out (FIFO) principle. Items are added at the rear and removed from the front.
- **Complexity:**
	- `enqueue`, `dequeue`, `peek`, `is_empty`: O(1) time, O(n) space

### Singly Linked List

### SimpleLinkedList
- **Operations:** `insert_first`, `insert_last`, `find`, `delete`
- **How it works:** Each node points to the next. Insertions at the head are O(1); insertions at the tail require traversal (O(n)).
- **Complexity:**
	- `insert_first`: O(1) time
	- `insert_last`: O(n) time
	- `find`, `delete`: O(n) time
	- Space: O(n)

### TailedLinkedList
- **Operations:** `insert_first`, `insert_last`, `find`, `delete`
- **How it works:** Like SimpleLinkedList, but maintains a tail pointer for efficient insertions at the end.
- **Complexity:**
	- `insert_first`: O(1) time
	- `insert_last`: O(1) time
	- `find`, `delete`: O(n) time
	- Space: O(n)

## Algorithms

### Binary Search
- **How it works:** Searches for a target in a sorted list by repeatedly dividing the search interval in half.
- **Time Complexity:** O(logn)
The time is logarithmic because the algorithm eliminates half of the search space in every iteration. The number of steps required to complete the search is proportional to the base-2 logarithm of n (log n). This makes binary search extremely efficient for large input lists.
- **Space Complexity:** O(1)
The space is constant because the function only uses a fixed number of variables (lo, hi, mid, val) regardless of the input list's size n. No new data structures are allocated that would grow with n.

### Binary Search Recursive
- **How it works:** Searches for a target in a sorted list by repeatedly dividing the search interval in half.
- **Time Complexity:** O(logn)
The time is logarithmic because the function discards half of the search space in every recursive call. The number of operations required is proportional to the logarithm of n (logn), resulting in highly efficient performance.
- **Space Complexity:** O(logn)
The space is logarithmic because of the recursion depth. Since the problem size is halved in each step, the function performs O(logn) nested recursive calls. Each of these calls consumes a small amount of memory on the call stack, making the total auxiliary space proportional to O(logn).

### Quicksort in Place
- **How it works:** Recursively partitions the list around a pivot, sorting sublists.
- **Time Complexity:** O(nlogn) to O(n^2)
Average Case (O(nlogn)): When the pivot splits the list roughly in half, the work is O(n) per level across O(logn) levels, resulting in O(nlogn).
Worst Case (O(n^2)): Occurs when the pivot is consistently the smallest or largest element, leading to highly unequal partitions. This forces the algorithm through O(n) levels of recursion, with O(n) work at each level, resulting in O(n^2).
- **Space Complexity:** O(n)
This implementation uses O(n) extra space because it creates new lists (left, middle, right) in every recursive call to hold the partitioned elements. This temporary storage dominates the space required, even though a more efficient "in-place" version would only require O(logn) for the recursion stack.

### Quicksort
- **How it works:** It sorts the array in-place by repeatedly partitioning sub-arrays around a pivot and managing the sub-array boundaries using an explicit stack instead of recursion
- **Time Complexity:** O(nlogn) to O(n^2)
The time complexity is the same as recursive Quicksort:
    - Average Case (O(nlogn)): Achieved when balanced partitioning is performed O(logn) times, with O(n) work at each level.
    - Worst Case (O(n^2)): Occurs with poor pivot selection (e.g., always the smallest/largest element), leading to O(n) partitioning levels.
- **Space Complexity:** O(logn)
The space is logarithmic (O(logn)) because this iterative version uses an explicit stack to store sub-array boundaries. By design, the maximum stack size (the depth of the recursion tree) is typically optimized to be O(logn), making it more memory-efficient than a standard recursive Quicksort, which can hit O(n) space in the worst case.

### Mergesort
- **How it works:** Recursively splits the list, sorts, and merges sublists.
- **Time Complexity:** O(nlogn)
The time complexity is O(nlogn) across the best, average, and worst cases, making it highly stable. This comes from two factors:
    - Recursion Depth (O(logn)): The list is consistently split in half, creating a recursion tree with logn levels.
    - Work Per Level (O(n)): At every level of the tree, the merge step compares and combines all n elements, requiring O(n) total operations.
- **Space Complexity:** O(n)
The extra space is linear (O(n)). This is because the provided implementation is not "in-place" and requires a new temporary array (merged) to store n elements during the combine step. While the recursion stack only adds O(logn) space, the O(n) requirement for temporary storage dominates the total space complexity.

### Recursive Factorial
- **How it works:** Computes n! by multiplying n by factorial(n-1).
- **Time Complexity:** O(n)
The time is linear because the function executes a constant amount of work (a comparison and a multiplication) for each of the $n$ times it recursively calls itself. The total number of operations is directly proportional to the input $n$.
- **Space Complexity:** $O(n)$
The space is also linear because the function's depth of recursion is $n$. Since each of the $n$ recursive calls is stored on the call stack until it resolves, the memory usage for the stack grows linearly with the input $n$.

### Recursive Fibonacci
- **How it works:** Computes nth Fibonacci number by summing results of previous two numbers recursively.
- **Time Complexity:** O(2^n)
The time is exponential due to redundant calculations. The function repeatedly computes the same smaller Fibonacci numbers, causing the total number of operations to grow like 2^n. This makes the naive recursive approach highly inefficient.
- **Space Complexity:** O(n) 💾
The extra space is linear (O(n)) because it's determined by the recursion depth on the call stack. The longest chain of recursive calls, n→n−1→⋯→1, means the stack size grows linearly with the input n.
--