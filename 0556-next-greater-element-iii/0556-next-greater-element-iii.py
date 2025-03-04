class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # if n >= 2147483486:
        #     return -1
        n = str(n)
        k = len(n)-2
        while k >= 0 and int(n[k]) >= int(n[k+1]):
            k = k - 1
        if k == -1:
            return -1
        i = k+1
        while i < len(n) and n[i]>n[k]:
            i = i + 1
        n = self.swap(n, k, i-1)
        n = self.placement(n, k+1)
        if int(n) > 2_147_483_647:
            return -1
        return int(n)
    def swap(self, n, index, index2):
        temp = n[:index] + n[index2] + n[index+1:index2] + n[index] + n[index2+1:]
        return temp.strip()
    def placement(self, n, index):
        start = index
        end = len(n) - 1
        while start < end:
            n = self.swap(n, start,end)
            start = start + 1
            end = end - 1
        return n