## max function
# two stacks    i.e. main stack and max stack
# insert 10 and insert in the maxstack as well
# insert new item and see if its larger than other items in main stack
# if yes then copy it to the max stack

class Maxstack:


    def __int__(self):
        self.main_stack = []  # use this to queue the data
        self.max_stack = [] # use this to dequeue the data

    def push(self,data):

        # push the main item onto the stack
       self.main_stack.append(data)

       if(len(self.main_stack))==1):
           self.max_stack.append(data)
            return

    def pop(self, data):
        for i in self.main_stack:
            if self.main_stack[-1] > max(self.main_stack[i-1])
        self.main_stack[0] = self.main_stack[-1]