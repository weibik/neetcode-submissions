class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        for val in s:
            if val in hash_map_s:
                hash_map_s[val] += 1
            else:
                hash_map_s[val] = 1
        for val in t:
            if val in hash_map_t:
                hash_map_t[val] += 1
            else:
                hash_map_t[val] = 1
        return hash_map_s == hash_map_t