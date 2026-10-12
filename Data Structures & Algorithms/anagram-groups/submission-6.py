class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            # [0, 0, 0, 0, ...]

            for char in word:
                count[ord(char) - ord("a")] += 1
            
            # aac
            # [2, 0, 1, 0, ...]

            res[tuple(count)].append(word)
            # res[(2,0,1,0,0,..)].append("aac")]
        
        return list(res.values())
        # <class 'dict_values'>

