def filter_pos(nums):
    l = []
    for num in nums:
        if num > 0:
            l.append(num)
    return l
