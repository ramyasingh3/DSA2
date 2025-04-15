# Trapping Rain Water

## Problem Description
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

### Examples
1. Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
   Output: 6
   Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

2. Input: height = [4,2,0,3,2,5]
   Output: 9
   Explanation: The elevation map traps 9 units of rain water.

## Approach
The solution uses a two-pointer technique:
1. Initialize two pointers, one at the start (left) and one at the end (right) of the array.
2. Keep track of the maximum height from left (left_max) and right (right_max).
3. For each position, the amount of water that can be trapped is:
   min(left_max, right_max) - height[current]
4. Move the pointer pointing to the smaller maximum height inward.
5. Update the maximum heights as we move the pointers.

## Time Complexity
- O(n) where n is the length of the array
- We only need to traverse the array once with two pointers
- Each element is visited exactly once

## Space Complexity
- O(1)
- We only use a constant amount of extra space for variables
- No additional data structures are required 