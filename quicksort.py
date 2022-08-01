class QuickSort:

    def __init__(self,data):
        self.data = data

    def sort(self):
        self.quick_sort(0,len(self.data)-1)

    # low is the index of the first item
    # high is the index of the last item

    def quick_sort(self, low, high):
        #[1,2,3,4]
        #[1,2] [3,4]
      if low >= high:
          return
      pivot_index = self.partition(low, high)
      print(f"pivot_index is the return value from partiotion function i.e. {pivot_index}")
        # call the function recursively on the left array
        # we make( if the pivot selection is working fine) log2 function calls
        # MASTER THEOREM T(n) = 2*log + O(N) = 0(NlogN)
      print(f"now we are calling quicksort low to pivot -1 i.e. {low} and {pivot_index - 1}")
      self.quick_sort(low, pivot_index-1)
        # call the function recursively on the righr array
      print(f"now we are calling quicksort low to pivot +1 i.e. {low} and {pivot_index + 1}")
      self.quick_sort(pivot_index+1, high)


# this is where the magic happens
    # in O(N) linear running time complexity
    def partition(self, low, high):
         '''pivot = random(low, hihg)
         let us use middle item as the pivot'''
         pivot_index = (low + high) // 2
         print(f"the updated pivot-index/low/high is {pivot_index}/{low}/{high} from x = [21, -4, 0, 10, 5, 4, 3, 100] is {x[pivot_index]}")
         print(f"here we are performing swap between {self.data[pivot_index]} and {self.data[high]} as pivot_index is {pivot_index} and x is {x}")
         self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]
         print(f"now the new x ready  is {x}")

         # consider all the items and compare them with the pivot

         for j in range(low,high):
            if  self.data[j] <= self.data[high]: # here pivot is self.data[high]
                #print(self.data[j] , end=' ')
                #x = [1, -4, 0, 10, 5, 4, 3, 100]
                print(f"{low} is low  and {j} is j are the values")
                print(f"swapping inside the loop between {self.data[low]} and {self.data[j]} ,  as low is {low} and j is {j} and x is {x}")
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low = low + 1
            # we have considered all the items , now we have to swap the pivot and index low
            #else: if else is not written then its like else pass.
              #  pass

         print(f"here we are performing swap between {self.data[low]} and {self.data[high]} as low is {low} and x is {x}")
         self.data[low], self.data[high] = self.data[high], self.data[low]


         # return the index of the pivot
         print(f"final value of low is {low} in this iteration {j}")
         return low

if __name__ == "__main__":
    x =[21,-4,0,10,5,4,3,100]
    algorithm = QuickSort(x)
    algorithm.sort()
    print(x)
 