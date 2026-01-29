class Solution:
    def RLE(self, m: str) -> str:
        # Use a list which we merge in the end instead of a string becuase concatenations are expensive
        solution = []
        
        i = 0
        while i < len(m):
            j = i+1
            while j < len(m) and m[i] == m[j]:
                j += 1
            
            # j-i gives us the count
            solution.append(f"{j-i}{m[i]}")
            i = j
        
        return "".join(solution)

 
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        return self.RLE(self.countAndSay(n-1))
    
# Example usage:
sol = Solution()
print(sol.countAndSay(1))  # Output: "1"
print(sol.countAndSay(4))  # Output: "1211"
print(sol.countAndSay(5))  # Output: "111221"
print(sol.countAndSay(6))  # Output: "312211"