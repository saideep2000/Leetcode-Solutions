class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        strr = ""
        for each in strs:
            strr = strr + str(len(each)) + "#" + each
        return strr

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        final_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            str_len = int(s[i:j])
            i = j + 1  # Move past the '#'
            final_list.append(s[i:i + str_len])
            i += str_len

        return final_list
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))