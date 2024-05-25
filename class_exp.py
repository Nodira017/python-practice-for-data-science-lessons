class Computer:
    def __init__(self, ram, processor, price):
        self.ram = ram
        self.processor = processor
        self.price = price

    def info(self):
        print(f'RAM: {self.ram}, Processor: {self.processor}, Price: {self.price}')


macbook = Computer('32GB', 'M1', '$4000')
macbook.info()
