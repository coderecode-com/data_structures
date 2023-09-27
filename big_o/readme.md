# Big O Notation Overview

## Introduction

- Represents the **upper limit** or **worst case** of an algorithm's runtime.
- Used to gauge **efficiency** as input size grows.

## Time Complexity vs Space Complexity

- Time complexity answers how long does it take
- Space complexity answers how much memory does it need

## Common Big O Notations

- **O(1)**: Constant Time
    - Independent of input size.

- **O(log n)**: Logarithmic Time
    - Divides problem size each step.
- **O(n)**: Linear Time
    - Directly proportional to input size.
- **O(n log n)**: Linear Logarithmic Time
    - Common in optimized sorting algorithms.
- **O(n^2)**: Quadratic Time
    - Often seen with nested loops.

## Importance

- Helps in **choosing algorithms** for tasks.
- Understand **performance limits**.
- Vital for large datasets.

## Cheatsheet

![big_o_cheatsheet.png](img%2Fbig_o_cheatsheet.png)
Source: https://www.bigocheatsheet.com/

## Conclusion

- Big O offers a lens to **compare algorithms**.
- A foundational tool in **software development**.

## Quiz

1. What's the Big O for an algorithm that runs in constant time?
2. Two loops inside each other is O(_).
3. What is the big O for the following code?

```
def four_times_linear_time(arr):
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0

    for num in arr:
        total1 += num

    for num in arr:
        total2 += num

    for num in arr:
        total3 += num

    for num in arr:
        total4 += num

    return total1 + total2 + total3 + total4
```

### Answers

1. O(1)
2. O(n^2)
3. O(n).

**Explanation**
The function iterates over the list once, 
hence it has a time complexity of O (4n). 
However, the constants are omitted
and thus the final answer is O (n).