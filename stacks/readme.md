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

| Feature/Aspect         | Linked List                                                     | Lists                                    | Deque                                                                              |
|------------------------|-----------------------------------------------------------------|------------------------------------------|------------------------------------------------------------------------------------|
| **Insertion at End**   | O(1) with tail pointer                                          | O(1)                                     | O(1)                                                                               |
| **Deletion at End**    | O(1) with tail pointer                                          | O(1)                                     | O(1)                                                                               |
| **Insertion at Start** | O(1)                                                            | O(n)                                     | O(1)                                                                               |
| **Deletion at Start**  | O(1)                                                            | O(n)                                     | O(1)                                                                               |
| **Memory Overhead**    | Higher due to extra pointers                                    | Minimal                                  | Moderate due to double-ended nature                                                |
| **Use Case**           | When you need constant-time insertions/deletions from both ends | When you mostly deal with end operations | When you need operations from both ends but don't want the overhead of linked list |


