import sys

file_path = 'output_of_mergesort.txt'
sys.stdout = open(file_path, "w")

def merge_sort(nums):

    # define the base case: that we keep splitting the list until the sublist have just one item
    if len(nums) == 1:
        print("here the left merge sort is over and right  merge sort starts")
        return

    # DIVIDE PHASE
    middle_index = len(nums) // 2
    print(f"nums is {nums}")
    print(f"middle_index is {middle_index} and", end =' next is left half \n')
    left_half = nums[:middle_index]
    print(left_half, end=' next is right half \n ')
    right_half = nums[middle_index:]
    print(right_half)
    print("###################################")

    print("next is merge sort left_half")
    merge_sort(left_half)
    print("next is merge sort right_half")
    merge_sort(right_half)

    # CONQUER PHASE
    # I AND J FOR LEFT AND RIGHT SUBARRAY
    # INDEX K FOR MERGE ARRAY
    i = 0
    j = 0
    k = 0

    while i<len(left_half) and j<len(right_half):
        print("#######here we enter the while loop###################")
        print(f"len(left_half)  len(right_half)  is {len(left_half)} and {len(right_half)} respectively value of i is {i} and j is {j}")
        print(f"if left_half[i] < right_half[j] {left_half[i]} and {right_half[j]}")
        if left_half[i] < right_half[j]:
            print("#######here we enter the while loop if statement###################")
            print(f"if left_half[i] < right_half[j] {left_half[i]} and {right_half[j]}")

            nums[k] = left_half[i]
            i = i + 1
        else:
            nums[k] = right_half[j]
            print("#######here we enter the while loop else statement###################")
            print(f"here we are entering the  else statemet  j is {j} and right_half[j] {right_half[j]} and we do j+1")
            j = j + 1

        k = k + 1

    # after that there may be additional items in the left or right subarray
    while i < len(left_half):
        nums[k] = left_half[i]
        i = i + 1
        k = k + 1

    while j < len(right_half):
        nums[k] = right_half[j]
        j  = j + 1
        k =  k + 1

if __name__ == "__main__":

    l = [1,5,-2,0,10,100,55,12,10,2,-10,-3]
    merge_sort(l)
    #print(l)
