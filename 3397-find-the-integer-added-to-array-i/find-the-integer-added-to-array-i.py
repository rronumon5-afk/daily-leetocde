class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        num1=[]
        for i in range(len(nums1)):
            for  j in range(i+1,len(nums1)):
                if nums1[i]>nums1[j]:
                    temp=nums1[i]
                    nums1[i]=nums1[j]
                    nums1[j]=temp
        nums2=sorted(nums2)

        for k in range(len(nums2)):
          x=nums2[k] - nums1[i]
        return x                
        