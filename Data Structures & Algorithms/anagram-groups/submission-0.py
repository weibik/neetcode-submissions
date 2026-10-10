from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            hash_map[f"{sorted_word}"].append(word)
        
        new_list = []
        for key in hash_map.keys():
            temp = []
            for val in hash_map[key]:
                temp.append(val)
            new_list.append(temp)
        return new_list
