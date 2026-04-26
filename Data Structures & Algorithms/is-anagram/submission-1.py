class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        for a, b in zip(s,t):
            count[a] = count.get(a, 0) + 1
            count[b] = count.get(b, 0) - 1
        
        values = set(count.values())
        last = values.pop() 
        return last == 0 and len(values) == 0