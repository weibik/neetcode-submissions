class Solution:

    def encode(self, strs: list[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s

        return result


    def decode(self, s: str) -> list[str]:
        result, num_index = [], 0

        while num_index < len(s):
            hash_index = num_index
            while s[hash_index] != "#":
                hash_index += 1
            length = int(s[num_index:hash_index])
            print(s[num_index:hash_index])
            # length = int(s[num_index])
            result.append(s[hash_index + 1 : hash_index + 1 + length])
            num_index = hash_index + 1 + length

        return result

