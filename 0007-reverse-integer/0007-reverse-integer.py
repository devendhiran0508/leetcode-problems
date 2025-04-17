class Solution:
    def reverse(self, x: int) -> int:
        int_min=-2**31
        int_max=2**31-1
        sign=-1 if x<0 else 1
        x=abs(x)
        rev=int(str(x)[::-1])*sign
        if rev<int_min or rev>int_max:
            return 0
        return rev        