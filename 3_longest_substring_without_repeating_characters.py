class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len == 0 or s_len == 1:
            return s_len

        left, right = 0, 0
        tracker = {}
        max_length = 0

        while right < s_len:
            c = s[right]

            if c not in tracker:
                tracker[c] = right

            else:
                # Slide, but only slide left if the duplicate is within the current window
                if tracker[c] >= left:
                    left = tracker[c] + 1
            
            tracker[c] = right
            right += 1

            # Update max_length if needed
            new_length = right - left
            max_length = max(max_length, new_length)


        return max_length

# Example usage:
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))   # Output: 3
print(sol.lengthOfLongestSubstring("bbbbb"))      # Output: 1
print(sol.lengthOfLongestSubstring("pwwkew"))     # Output: 3
print(sol.lengthOfLongestSubstring(""))           # Output: 0
print(sol.lengthOfLongestSubstring("a"))          # Output: 1
print(sol.lengthOfLongestSubstring("au"))         # Output: 2
print(sol.lengthOfLongestSubstring("bbbbkkkk"))   # Output: 2