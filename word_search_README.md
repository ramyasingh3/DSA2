# Word Search

## Problem Description
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Examples
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Explanation: The word "ABCCED" can be found by starting at the top-left corner and moving right, down, right, down, right.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Explanation: The word "SEE" can be found by starting at the bottom-left corner and moving right, up, right.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
Explanation: The word "ABCB" cannot be found in the grid.
```

## Constraints
- m == board.length
- n == board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consist of only lowercase and uppercase English letters

## Approach 1: DFS with Visited Set
1. For each cell in the grid:
   - Start DFS from that cell
   - Keep track of visited cells using a set
   - Try all four directions (up, right, down, left)
2. DFS function:
   - Base case: if we've matched all characters, return true
   - Check boundaries and if current cell matches
   - Mark current cell as visited
   - Try all four directions
   - Backtrack by unmarking current cell
3. Return false if no path is found

## Approach 2: Optimized DFS (In-place)
1. Similar to Approach 1, but instead of using a visited set:
   - Mark visited cells by changing their value to a special character (e.g., '#')
   - Restore the original value when backtracking
2. This approach:
   - Reduces space complexity
   - Avoids creating a new set for each search
   - Is more memory efficient

## Time and Space Complexity
### Both Approaches
- Time Complexity: O(m * n * 4^L)
  - m, n: dimensions of the board
  - L: length of the word
  - 4^L: maximum number of paths to explore
- Space Complexity: O(L) for recursion stack

## Key Points
- This is a classic backtracking problem
- We need to try all possible paths
- We can't reuse the same cell
- The optimized version is more space-efficient
- Both approaches handle edge cases (empty board, empty word)

## Common Applications
- Word games (like Boggle)
- Pattern matching
- Text search
- Image processing
- Path finding
- Game development

## Example Walkthrough
For board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED":

### DFS with Visited Set:
1. Start at (0,0) with 'A'
2. Mark (0,0) as visited
3. Move right to (0,1) with 'B'
4. Move right to (0,2) with 'C'
5. Move down to (1,2) with 'C'
6. Move down to (2,2) with 'E'
7. Move right to (2,3) with 'D'
8. Word found!

### Optimized DFS:
1. Start at (0,0) with 'A'
2. Change (0,0) to '#'
3. Move right to (0,1) with 'B'
4. Change (0,1) to '#'
5. Continue until word is found
6. Restore cells during backtracking 