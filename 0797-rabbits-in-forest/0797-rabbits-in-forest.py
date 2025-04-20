class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        total=0
        for x,freq in count.items():
            groupSize=x+1
            groups=math.ceil(freq/groupSize)
            total+=groups*groupSize
        return total

        