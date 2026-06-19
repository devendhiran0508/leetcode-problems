class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curAlt = 0
        highPoint = curAlt
        for alt_gain in gain:
            curAlt += alt_gain
            highPoint = max(highPoint, curAlt)
        return highPoint