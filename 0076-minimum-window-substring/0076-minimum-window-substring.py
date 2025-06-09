class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ori_dict = defaultdict(int)
        build_dict = defaultdict(int)
        for i in t:
            ori_dict[i] = ori_dict[i] + 1
        ori_count = len(ori_dict.keys())
        build_count = 0
        final_str = ""
        
        start = 0
        for end in range(0,len(s)):
            # add a char to make the build and ori count same
            if s[end] in ori_dict:
                build_dict[s[end]] = build_dict[s[end]] + 1
                if build_dict[s[end]] == ori_dict[s[end]]:
                    build_count = build_count + 1
                    
            # pop the intial characters to minimize the len
            while build_count == ori_count:
                if final_str == "" or (len(final_str) >= (end - start + 1)):
                    final_str = s[start:end+1]

                if s[start] in ori_dict:
                    build_dict[s[start]] = build_dict[s[start]] - 1
                    if build_dict[s[start]] < ori_dict[s[start]]:
                        build_count = build_count - 1
                start = start + 1
            
            
        
        return final_str

            


        
        return ""