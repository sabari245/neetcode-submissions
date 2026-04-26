class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        for a, b in zip(s,t):
            # handling the a case
            if a in count:
                count[a] += 1
            else:
                count[a] = 1
            
            #handling the b case
            if b in count:
                count[b] -= 1
            else: 
                count [b] = -1
        
        values = set(count.values())
        last = values.pop() 
        return last == 0 and len(values) == 0