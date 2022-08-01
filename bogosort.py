import random
import time


## #range(start, stop, step)
#Optional. An integer number specifying at which position to start. Default is 0
#Required. An integer number specifying at which position to stop (not included).
#Optional. An integer number specifying the incrementation. Default is 1
#print(random.randint(3, 9))
#The randint() method returns an integer number selected element from the specified range.
#random.randint(start, stop)
#start Required. An integer specifying at which position to start.
#stop Required. An integer specifying at which position to end.

class BogoSort:

    def __init__(self, nums):
        self.nums = nums


    #The randint() method returns an integer number selected element from the specified range.
    #start	Required. An integer specifying at which position to start.
    #stop	Required. An integer specifying at which position to end.

    def sort(self):
        while not self.is_sorted():
            print("shuffle again ...")
            self.shuffle()

    # fisher-yates  just randomly swap numbers and therfore its an in-place algorithm
    # we generate a new permutation in O(N)
    def shuffle(self):
        for i in range(len(self.nums)-2, -1 ,-1): # if we stop at 0 and if we have a small list that has 2 elements thent it wont work
            j = random.randint(0, i+1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]



    def is_sorted(self):
        for  i in range(len(self.nums)-1):
            if self.nums[i] > self.nums[i+1]:
                return  False

        return True


if __name__ == "__main__":

    # it has O(N) running tree
    start = time.time()
    alogrithm = BogoSort([1,-4,0,10,12,-5,1,2,-1,34])
    alogrithm.sort()
    print(alogrithm.nums)
    end = time.time()
    print("total time is", end-start)
