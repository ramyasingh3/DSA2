def exist(board, word):
    """
    Check if the word exists in the board.
    Time Complexity: O(m * n * 4^L) where m,n are board dimensions and L is word length
    Space Complexity: O(L) for recursion stack
    """
    if not board or not board[0] or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, word_index, visited):
        # Base case: found the word
        if word_index == len(word):
            return True
        
        # Check boundaries and if current cell matches
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or board[r][c] != word[word_index]):
            return False
        
        # Mark current cell as visited
        visited.add((r, c))
        
        # Try all four directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            if dfs(r + dr, c + dc, word_index + 1, visited):
                return True
        
        # Backtrack: unmark current cell
        visited.remove((r, c))
        return False
    
    # Try starting from each cell
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0, set()):
                return True
    
    return False

def exist_optimized(board, word):
    """
    Optimized version that modifies the board instead of using a visited set.
    Time Complexity: O(m * n * 4^L)
    Space Complexity: O(L) for recursion stack
    """
    if not board or not board[0] or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, word_index):
        # Base case: found the word
        if word_index == len(word):
            return True
        
        # Check boundaries and if current cell matches
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            board[r][c] != word[word_index]):
            return False
        
        # Mark current cell as visited by changing it to '#'
        temp = board[r][c]
        board[r][c] = '#'
        
        # Try all four directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            if dfs(r + dr, c + dc, word_index + 1):
                return True
        
        # Backtrack: restore the cell
        board[r][c] = temp
        return False
    
    # Try starting from each cell
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    
    return False

def main():
    # Test cases
    test_cases = [
        # Test case 1
        ([
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], "ABCCED"),  # Expected: True
        
        # Test case 2
        ([
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], "SEE"),  # Expected: True
        
        # Test case 3
        ([
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], "ABCB"),  # Expected: False
        
        # Test case 4
        ([
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ], ""),  # Expected: False
        
        # Test case 5
        ([], "ABC"),  # Expected: False
        
        # Test case 6
        ([['A']], "A"),  # Expected: True
        
        # Test case 7
        ([['A', 'A']], "AAA"),  # Expected: False
    ]
    
    print("Testing DFS with visited set:")
    for board, word in test_cases:
        result = exist(board, word)
        print(f"Board: {board}")
        print(f"Word: {word}")
        print(f"Exists: {result}")
        print()
    
    print("\nTesting Optimized DFS:")
    for board, word in test_cases:
        # Create a deep copy of the board for the optimized version
        board_copy = [row[:] for row in board]
        result = exist_optimized(board_copy, word)
        print(f"Board: {board}")
        print(f"Word: {word}")
        print(f"Exists: {result}")
        print()

if __name__ == "__main__":
    main() 