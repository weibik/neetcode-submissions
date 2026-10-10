class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count: dict[str, int] = {}
        
        for val in s:
            count[val] = count.get(val, 0) + 1
        
        for val in t:
            count[val] = count.get(val, 0) - 1

            if count[val] < 0:
                return False
        return True
        # hash_map_s = {}
        # hash_map_t = {}
        # for val in s:
        #     if val in hash_map_s:
        #         hash_map_s[val] += 1
        #     else:
        #         hash_map_s[val] = 1
        # for val in t:
        #     if val in hash_map_t:
        #         hash_map_t[val] += 1
        #     else:
        #         hash_map_t[val] = 1
        # return hash_map_s == hash_map_t