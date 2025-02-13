"""
Given two integer arrays nums1 and nums2, return an array of their 
intersection. Each element in the result must be unique and you may 
return the result in any order. (Easy level)
"""
def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    ls = []
    # convert nums1 and nums2 to set to remove duplication
    num1 = set(nums1) 
    num2 = set(nums2)
    # loop num1 set and append the item i to ls if it exists in num2
    for i in num1:
        if i in num2:
            ls.append(i)
    return ls #return ls containing intersection