def sort_list(nums, instructions):
    if instructions == 'asc':
        return sorted(nums)
    if instructions == 'desc':
        return sorted(nums, reverse=True)
    if instructions == 'none':
        return nums
    return nums

print(sort_list([1, 5, 4, 3, 2], 'asc'))