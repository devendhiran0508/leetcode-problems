class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        res=0
        while k!=1:
            x=k.bit_length()-1
            if(1<<x)==k:
                x-=1
            k-=1<<x
            if operations[x]:
                res+=1
        return chr(ord("a")+(res%26))