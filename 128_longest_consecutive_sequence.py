class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        longest = 0

        for i in numset:
            # Skip if i isn't the start of a sequence
            if i-1 in numset:
                continue

            # Keep going until sequence ends
            cur = i
            while cur+1 in numset:
                cur += 1
            
            longest = max(longest, cur-i+1)
            
        return longest

# Example usage:
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))  # Output: 4
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9
print(sol.longestConsecutive([]))  # Output: 0
print(sol.longestConsecutive([1,2,0,1]))  # Output: 3
print(sol.longestConsecutive([-7,-7,-7]))  # Output: 1