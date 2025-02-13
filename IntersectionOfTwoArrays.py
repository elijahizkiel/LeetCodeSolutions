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
    ls = set(nums1).intersection(set(nums2))
    return list(ls) #return ls as list containing intersection