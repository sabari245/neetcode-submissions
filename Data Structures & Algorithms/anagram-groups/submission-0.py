class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for each in strs:
            key = "".join(sorted(each))
            if key in groups:
                groups[key].append(each)
            else:
                groups[key] = [each]
        return list(groups.values())

