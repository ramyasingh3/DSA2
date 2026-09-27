# UTF-8 Validation

## Problem
Validate byte sequence as UTF-8.

## Example
```
Input: [32, 45, 16, 10, -3, -4, 47, 36, 11, -4, -11]
Output: (compute according to problem statement)
```

## Constraints
- Reasonable input sizes for interview settings (`n` up to ~10^5 unless noted)
- Aim for better than naive O(n^2) when possible

## Hint
Track remaining continuation bytes.

## Topic
Bit Manipulation
