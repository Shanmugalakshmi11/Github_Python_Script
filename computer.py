class computer():
    typ = "Hardware"
    def __init__(self, Brand, Screen_size, colour, Hard_disk_size, CPU_model, RAM_memory, price):
        self.Brand = Brand
        self.Screen_size = Screen_size 
        self.colour = colour
        self.Hard_disk_size = Hard_disk_size
        self.CPU_model = CPU_model
        self.RAM_memory = RAM_memory 
        self.price = price

    def zeige_info(self):
        print(f"Computer Attributes: \n Brand: {self.Brand}\n Screen_size: {self.Screen_size}\n colour: {self.colour}\n Hard_disk_size: {self.Hard_disk_size}\n CPU_model: {self.CPU_model}\n RAM_memory: {self.RAM_memory}\n Price: {self.price}")

my_computer = computer("Lenovo", "15.6 Inches", "Black", "512 GB", "Celeron", "8 GB", "258€")
my_computer.zeige_info()
        
my_computer = computer("LG Electronics", "17 Inches", "Grey", "1 TB", "Intel Core i7", "8 GB", "689€")
my_computer.zeige_info()          