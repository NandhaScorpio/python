class laptop :
    def __init__(self):
        self.processor = ""
        self.ram = ""
        
    def display(self):
        print("RAM : ",self.ram)
        print("Processor : ",self.processor)

hp = laptop()
dell = laptop()

hp.processor = "i3"
hp.ram = "8gb"

dell.ram = "16gb"
dell.processor = "i7"

hp.display()
dell.display()

