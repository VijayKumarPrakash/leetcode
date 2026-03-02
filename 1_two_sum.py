class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dt = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dt:
                return [i, dt[complement]]
            dt[num] = i

# Example usage:
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(sol.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(sol.twoSum([3, 3], 6))          # Output: [0, 1]