"""
Given an integer array nums, return the third distinct maximum
number in this array. If the third maximum does not exist, return 
the maximum number. (Easy level)
"""
def thirdMax(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # form set from the given list of numbers to remove duplications
    # and change the set to list
    # sort in reverse order 
    # return third item @ index 2 if the length is  >=3
    # else return the first item @ index 0
    ls = list(set(nums))
    ls.sort(reverse=True)
    if len(ls) >= 3:
        return ls[2]
    else: return ls[0]