#/*The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well - so no additional memory can be used!

#For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]*/


T = [1,2,3,3,4,4,4,4,5,6]

def palindrome(s):

    if s == s[::-1]:
       return True
    return False

if __name__ == '__main__':
    print(palindrome("nitin"))