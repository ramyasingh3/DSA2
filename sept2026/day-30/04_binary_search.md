# Time Based Key-Value Store

## Problem
get(key, timestamp) ≤ timestamp value.

## Example
```
Input: [29, -3, -13, 5, -9]
Output: (compute according to problem statement)
```

## Constraints
- Reasonable input sizes for interview settings (`n` up to ~10^5 unless noted)
- Aim for better than naive O(n^2) when possible

## Hint
Map of key → binary-searchable list.

## Topic
Binary Search
