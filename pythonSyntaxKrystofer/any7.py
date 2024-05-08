def any7(nums):

    for num in nums:
        if num == 7:
            return True

    return False


print("should be true", any7([10, 3, 13, 18, 7]))
print("should be false", any7([1, 2, 3, 4]))