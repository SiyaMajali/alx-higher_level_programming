#!/usr/bin/python3

"""Write a function that finds peak of list of unsorted numbers"""


def find_peak(li):
    """caller function"""
    if li is None or li == []:
        return None

    return peak_helper(li, 0, len(li) - 1)


def peak_helper(li, start, end):
    """helper function"""
    x = int((end - start)/2 + start)

    if x + 1 >= len(li) or li[x + 1] <= li[x]:
        if x - 1 < 0 or li[x - 1] <= li[x]:
            return li[x]
        else:
            return peak_helper(li, 0, x)
    else:
        return peak_helper(li, x + 1, end)
