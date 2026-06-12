class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        added = {}
        for s in strs:
            sublist = []
            sort_key = ''.join(sorted(s))
            if sort_key in added:
                added[sort_key].append(s)
                continue
            added[sort_key] = [s]
        for x, y in added.items():
            final_list.append(y)
        return final_list
