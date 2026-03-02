class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len == 0 or s_len == 1:
            return s_len

        left, right = 0, 1
        current = set(s[left])
        max_length = 1

        while right < s_len:
            c = s[right]

            if c not in current:
                current.add(c)
                right += 1

            else:
                # Slide
                while s[left] != s[right]:
                    current.remove(s[left])
                    left += 1
                current.remove(s[left])
                left += 1
                right += 1
                current.add(c)
            
            # Update max_length if needed
            new_length = len(current)
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