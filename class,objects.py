class laptop:
    price = ""
    processor = ""
    ram = ""

hp = laptop()
dell = laptop()
lenovo = laptop()

hp.price = "$25"
hp.processor = "i3"
hp.ram = "8gb"

dell.price = "$30"
dell.processor = "i5"
dell.ram = "16gb"

lenovo.price = "$15"
lenovo.processor = "i3"
lenovo.ram = "4gb"

print("HP")
print(hp.price,hp.processor,hp.ram)

print("Dell")
print(dell.price,dell.processor,dell.ram)

print("Lenovo")
print( lenovo.price,lenovo.processor,lenovo.ram)
