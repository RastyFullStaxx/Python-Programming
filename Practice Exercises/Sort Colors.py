def sort_colors(nums):
    left, current, right = 0, 0, len(nums) - 1
    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1
        elif nums[current] == 2:
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1
        else:
            current += 1

colors = [2, 0, 2, 1, 1, 0]
sort_colors(colors)
print(colors)
