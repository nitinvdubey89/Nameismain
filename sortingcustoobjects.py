class Person:

    # we have 2 instance variables - name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # we have to define the 'less than' function to let Python know how to interpret the < and > operators
    # when we use < then Python calls this function to decide what object is smaller and what is greater
    def __lt__(self, other):
        return self.age < other.age

    # string representation of the object (when we use the print() function then this function is called)
    def __repr__(self):
        return str(self.name)


# we can use the exact same insertion sort algorithm we have implemented
def insertion_sort(people):
    for i in range(len(people)):

        j = i

        while j > 0 and people[j - 1] > people[j]:
            people[j], people[j - 1] = people[j - 1], people[j]
            j = j - 1


if __name__ == '__main__':
    n = [Person('Adam', 23), Person('Ana', 17), Person('Kevin', 32), Person('Daniel', 37)]
    insertion_sort(n)
    print(n)
