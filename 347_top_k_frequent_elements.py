from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dist = {}
        for num in nums:
            if num in freq_dist:
                freq_dist[num] += 1
            else:
                freq_dist[num] = 1
            
        result = []

        # Invert the dictionary
        inv_freq_dist = defaultdict(list)
        for key,v in freq_dist.items():
            inv_freq_dist[v].append(key)
        
        for key in sorted(list(inv_freq_dist.keys()), reverse=True):
            result.extend(inv_freq_dist[key])
            if len(result) == k:
                break

        return result
    
# Example usage:
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(sol.topKFrequent([1], 1))          # Output: [1]
print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))  # Output: [1, 2]