
# in this algo , we compare every element with the other and swap the greater with smaller

def selectionsort(nums):
    #print(nums)
    for i in range(len(nums)-1):
        index = i

        # N-1 * O(N) there it is O(N2)
        ## this is the linear search
        for j in range(i, len(nums)):
            if nums[j] > nums[index]:
                index = j

        # we have to swap min with left most item
        if index != i:
            nums[index], nums[i] = nums[i], nums[index]
    print(nums)

if __name__ == "__main__":

      n = [45,100,0,1,-5,10,4,5,6,13]
      selectionsort(n)
