from collections import defaultdict 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_a = defaultdict(lambda: 0)
        hash_map_b = defaultdict(lambda: 0)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hash_map_a[s[i]] += 1
            hash_map_b[t[i]] += 1

        if hash_map_a == hash_map_b:
            return True

        return False