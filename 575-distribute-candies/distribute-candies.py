class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        num=len(candyType)//2
        candies=set(candyType)
        type=len(set(candyType))
        if type>num:
            return num
        else:
            return type

        

        