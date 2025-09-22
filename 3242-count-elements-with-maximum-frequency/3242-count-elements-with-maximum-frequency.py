class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqmap=Counter(nums)
        maxfreq=max(freqmap.values())
        return sum(freq for freq in freqmap.values() if freq==maxfreq)