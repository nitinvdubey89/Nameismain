# keep comparing with the preceding item in the list
# then we swap if its greated
# keep comparing the all the lst

def insertionsort(nums):
    for i in range(len(nums)):

        j =  i
        #we have to check all the previous items( not always all of them)
        # in worst case we consider all previous items require swap unit j =0

        while j > 0  and nums[j-1] > nums[j]:
            # swap the items
            nums[j -1], nums[j] = nums[j], nums[j-1]
            j = j -1


if __name__  == "__main__":

    x = [1, -5, 10, 100, -4, 0, 3, 2, 1]
    insertionsort(x)
    print(x)




