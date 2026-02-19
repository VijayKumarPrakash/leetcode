import numpy as np
import math

class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        n = len(dist)
        dist = np.array(dist, dtype=float)
        speed = np.array(speed, dtype=float)

        time_to_city = dist / speed
        time_to_city.sort()

        for i in range(n):
            # Kill monster at position i - no need to update anything
            if math.ceil(time_to_city[i]) <= i:
                return i
        
        return n

# Example usage:
sol = Solution()
print(sol.eliminateMaximum([1, 3, 4], [1, 1, 1]))  # Output: 3
print(sol.eliminateMaximum([1, 1, 2], [1, 1, 1]))  # Output: 1
print(sol.eliminateMaximum([3, 2, 4], [5, 3, 2]))  # Output: 1