class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for s in strs:
            temp = []
            for char in s:
                new_char = chr(ord(char) + 1)
                temp.append(new_char)
            encoded_list.append("".join(temp))

        print(encoded_list)
        return encoded_list        
                
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        for word in s:
            temp = []
            for char in word:
                new_char = chr(ord(char) - 1)
                temp.append(new_char)
            decoded_list.append("".join(temp))
        print(decoded_list)
        return decoded_list