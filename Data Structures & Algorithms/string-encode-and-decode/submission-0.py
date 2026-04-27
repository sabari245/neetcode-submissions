class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "#" + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        flag = 0 # 0 none, 1 count
        count = ""
        while i < len(s):
            if s[i] == "#" and flag == 0:
                flag = 1
            elif s[i] == "#" and flag == 1:
                flag = 0
                count = int(count)
                res.append(s[i+1: i+1+count])
                i += count
                count = ""
            else:
                count += s[i]
            i += 1

        return res