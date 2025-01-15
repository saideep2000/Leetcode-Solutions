class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_b = str(bin(num1))
        num2_b = str(bin(num2))
        num1_c = num1_b.count("1")
        num2_c = num2_b.count("1")
        f = ""
        if num1_c == num2_c:
            return num1
        elif num1_c > num2_c:
            for i in str(num1_b):
                if i == "1":
                    if num2_c:
                        f = f + "1"
                        num2_c = num2_c - 1
                    else:
                        f = f + "0"
                else:
                    f = f + "0"
            return int(f, 2)
        else:
            print(num1_b)
            print(num2_b)
            num2_c = num2_c - num1_c
            for i in range(len(num1_b)-1,0,-1):
                if num1_b[i] != "1" and num2_c:
                    f = f + "1"
                    num2_c = num2_c - 1
                else:
                    f = f + num1_b[i]
            if num2_c:
                f = "1"*num2_c + f
            if f[-1] == "b":
                f = f[:-1]
            return int(f[::-1],2)
                


        