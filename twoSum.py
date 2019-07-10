def twosum(nums, target):
    length = len(nums)

    for el in nums:
        compliment = target - el

        if compliment != el:
            if compliment in nums:
                x_index = nums.index(el)
                y_index = nums.index(compliment)
                return [x_index, y_index]
        elif compliment == el:
            if nums.count(el) == 2:
                x_index = nums.index(el)
                nums.remove(el)
                y_index = nums.index(el) + 1
                return [x_index, y_index]


nums = [2, 7, 11, 15]
target = 9
res = twosum(nums, target)
print(res)

nums = [-3, 4, 3, 90]
target = 0
res = twosum(nums, target)
print(res)

nums = [3, 2, 4]
target = 6
res = twosum(nums, target)
print(res)