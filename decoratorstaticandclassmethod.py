class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self})

    @classmethod
    def class_method(cls):
        print(f"Called a class method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")




test = ClassTest()
print(test.instance_method())

ClassTest.class_method() # python will pass it like this ClassTest.class_method(ClassTest)

ClassTest.static_method()