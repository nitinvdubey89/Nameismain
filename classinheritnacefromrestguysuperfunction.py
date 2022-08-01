class Device:
    def __init__(self,name,connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name} ({self.connected})"


    def disconnect(self):
        self.connected = False
        print("Disconnected.")

class Printer(Device):
    def __init__(self, name,connected_by,capacity):
        #self.name = name
        #self.connected_by = connected_by
        #self.connected = True
        # in python 3 we have a super funciton that can call the parent class __init__
        super().__init__(name,connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()}({self.remaining_pages} pages reamining)"

    def print(self,pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(20)
printer.disconnect()
printer.print(20)