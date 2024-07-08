from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}\n'


class Shop(Product):
    __file_name = 'products.txt'

    def __init__(self):
        pass

    def get_products(self):
        self.file = open(self.__file_name, 'r')
        pprint(self.file.read())
        self.file.close()
        return

    def add(self, *products):
        self.products = products
        self.get_products()
        for self.name in self.file:
            if self.name not in self.file:
                self.file = open(self.__file_name, 'a')
                self.file.write(products)
                self.file.close()
            else:
                print(f'Продукт {self.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2, p1, p3)

s1.get_products()
s1.add(p1)
