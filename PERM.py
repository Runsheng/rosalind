#!/usr/bin/env python
'''
Rosalind ID: PERM
Problem Title: Enumerating Gene Orders
URL: http://rosalind.info/problems/perm/
2016/05/08, runsheng
'''


def perm(nums):
    """
    :param nums: a list of range(n), like [1,2,3]
    :return:The total number of permutations of length n,
            followed by a list of all such permutations (in any order).
    """
    if nums is None:
        return [[]]
    elif len(nums) <= 1: # to the end
        return [nums]

    # main code
    result = []
    for i, item in enumerate(nums):
        for p in perm(nums[:i] + nums[i+1:]):  # recursion
            result.append(p + [item])
    return result

if __name__=="__main__":
    nums=range(1,5+1)
    print len(perm(nums))
    for i in perm(nums):
        for n in i:
            print n,
        print

