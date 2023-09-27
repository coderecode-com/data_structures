# Stack

## Introduction

- LIFO
- Stack of plates
- Stack of books

## Real Life Usage

- Phone call history
- Browser History
- Undo Redo
- Call stacks
- Parenthesis matching

## Common methods

```Python
push()
pop()

peek()
size()
is_empty()
```

## Implementation in Python

- `list`
- `deque`

## Using Lists

### Advantages

- Native to Python
- dynamic resizing
- O(1) average time complexity for append and pop operations.

### Disadvantages

- Overhead of dynamic resizing can sometimes cause performance issues for very large lists or frequent resizing.
- `pop()` incurs `O(n)` memory cost

### Suitable for

Smaller stacks

## Using Collections.deque

### Advantages

- Implemented as a doubly-linked list
- fast O(1) appends and pops from both ends

### Disadvantages

- Slightly more overhead than a simple list for typical stack operations

### Suitable for

larger stacks

## Summary of differences

| Feature/Aspect         | Lists   | Deque                               |
|------------------------|---------|-------------------------------------|
| **Insertion at End**   | O(1)    | O(1)                                |
| **Deletion at End**    | O(1)    | O(1)                                |
| **Insertion at Start** | O(n)    | O(1)                                |
| **Deletion at Start**  | O(n)    | O(1)                                |
| **Memory Overhead**    | Minimal | Moderate due to double-ended nature |

## When to use `list` or `deque`

### Use Lists

- For small-sized stacks where performance differences are negligible.
- When you're only using the list for basic stack operations and don't need the additional functionalities of deque.

**Advantages**

- built-in part of Python and don't require an additional import.

**Disadvantages**

- Popping or appending elements in the middle of a list is O(n). However, if you're using it as a stack (with `append()`
  and `pop()` at the end), it's
  O(1) on average.

### Use Deque

- For larger datasets where the efficiency of operations matters more.

**Advantages**

- deque is optimized for fast appends and pops from both ends, providing consistent O(1) time for these operations.

**Disadvantages**

- Might be a bit of an overkill if you only require simple stack operations.