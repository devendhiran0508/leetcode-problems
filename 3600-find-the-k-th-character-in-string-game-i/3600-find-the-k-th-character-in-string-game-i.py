class Solution:
    def kthCharacter(self, k: int) -> str:
        result=0
        while k!=1:
            x=k.bit_length()-1
            if(1<<x)==k:
                x-=1
            k-=1<<x
            result+=1
        return chr(ord("a")+result)
        