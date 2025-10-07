class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res=[1]*len(rains)
        s=SortedList()
        mp={}
        for i, rain in enumerate(rains):
            if rain==0:
                s.add(i)
            else:
                res[i]=-1
                if rain in mp:
                    it=s.bisect(mp[rain])
                    if it==len(s):
                        return []
                    res[s[it]]=rain
                    s.discard(s[it])
                mp[rain]=i
        return res