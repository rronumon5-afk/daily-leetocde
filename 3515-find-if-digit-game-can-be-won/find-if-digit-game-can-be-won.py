class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single=0
        double=0
        for i in nums:
            if i<10:
             single=single+i
            else:
             double=double+i
        if single>double:
            return True
        elif single<double:
            return True
        elif single==double:
            return False  
        