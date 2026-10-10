class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # if len(s) != len(t):
        #     return False
        # count: dict[str, int] = {}
        
        # for val in s:
        #     count[val] = count.get(val, 0) + 1
        
        # for val in t:
        #     count[val] = count.get(val, 0) - 1

        #     if count[val] < 0:
        #         return False
        # return True