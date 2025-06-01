class Solution:
    def intToRoman(self, num: int) -> str:
        value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        i=0
        rom=""
        while num>0:
            for _ in range(num//value[i]):
                rom+=roman[i]
                num-=value[i]
            i+=1
        return rom