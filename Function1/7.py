def has_33(nums):
    if 3 in nums:
        ind = nums.index(3)
        if ind + 1 < len(nums) and nums[ind + 1] == 3:
            print(True)
        elif ind - 1 >= 0 and nums[ind - 1] == 3:
            print(True)
        else:
            print(False)
L = [3, 2, 3]
has_33(L)