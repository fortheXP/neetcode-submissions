class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sort_key = ''.join(sorted(s))
            res[sort_key].append(s)
        return list(res.values())
