class TrappingRainWater:
    def trap(self, height: list[int]) -> int:
        """
        Calculate how much water can be trapped after raining.
        
        Args:
            height: List of integers representing the elevation map
            
        Returns:
            int: Total amount of water that can be trapped
        """
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        result = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1
                
        return result

def test_trapping_rain_water():
    # Test cases
    test_cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
        ([], 0),
        ([1], 0),
        ([1,0,1], 1),
        ([1,2,3,4,5], 0),
        ([5,4,3,2,1], 0),
        ([1,0,2,0,3,0,4], 6),
    ]
    
    solver = TrappingRainWater()
    
    for height, expected in test_cases:
        result = solver.trap(height)
        print(f"Input: height = {height}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_trapping_rain_water() 