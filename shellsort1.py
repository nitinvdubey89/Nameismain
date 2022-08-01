# method sorts by comparing items far away from each other

def shellsort(nums):

    gap = len(nums) //2

    # 1 2 6 3 0 -2
    while gap > 0:
      # this is the same as insertion sort but here we have to consider items as far from each other as the value
      # of the gap 

        for i in range(gap, len(nums)):
            j = i

            while j >= gap and nums[j-gap] > nums[j]:
                nums[j], nums[j - gap] = nums[j - gap], nums[j]
                j = j - gap

        gap = gap // 2

if __name__ == "__main__":
    x = [10,-4,0,3,2,1,100,-8]
    shellsort(x)
    print(x)
