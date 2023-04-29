# given a list return a sorted list, if list is empty or None or not a list return an empty list

def solution(nums: list) -> list:
    if not nums:
        return []
    else:
        return sorted(nums)
