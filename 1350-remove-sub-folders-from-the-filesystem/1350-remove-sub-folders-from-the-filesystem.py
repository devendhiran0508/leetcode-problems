class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res=[folder[0]]
        for i in folder[1:]:
            if not i.startswith(res[-1] + "/"):
                res.append(i)
        return res
        