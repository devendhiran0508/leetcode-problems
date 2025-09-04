class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz=abs(x-z)
        yz=abs(y-z)
        if xz<yz:
            return 1
        elif yz<xz:
            return 2
        else:
            return 0
        