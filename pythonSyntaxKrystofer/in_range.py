def in_range(nums, lowest, highest):

    for num in nums:
        if num >= lowest and num <= highest:
            print(f"{num} fits")


in_range([20, 30, 40, 50, 60, 70], 23, 64)            
