import time

class Bubblesort:

    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-i-1):
                if self.nums[j] > self.nums[j+1]: # incase we need descending order then we change the symbol to >
                    self.swap(j, j+1)


    def swap(self, i , j ):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


if __name__ == "__main__":
    n = [1, -5, 0,2, -1, 10, 9, 100, 56, -34]
    start = time.time()
    sort = Bubblesort(n)
    sort.sort()
    print(sort.nums)
    end = time.time()
    print("total time is", end - start)