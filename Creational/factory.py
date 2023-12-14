class Product:
    def describe(self):
        pass


class Factory:
    product = "Product"
    def create(self):
        print(f"{self.product} created.")
        

class CPU(Product):
    def describe(self):
        print("I'm a CPU.")
        
    def __str__(self):
        return "CPU"
        
        
class RAM(Product):
    def describe(self):
        print("I'm a RAM")

    def __str__(self):
        return "RAM"
        

class CPUFactory(Factory):
    product = CPU()

    def create(self):
        super().create()
        return self.product
    

class RAMFactory(Factory):
    product = RAM()

    def create(self):
        super().create()
        return self.product
    

products = []

# Creates Factories for creating products
cpu_factory = CPUFactory()
ram_factory = RAMFactory()

# Create products using their factories and add an product array
products.append(cpu_factory.create())
products.append(ram_factory.create())

# Change Factory's product and create on product
ram_factory.product = cpu_factory.product
products.append(ram_factory.create())

# Use describe methods of product's which in the products array
for pr in products:
    pr.describe()