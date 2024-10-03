class Product:
    def __init__(self, name, weight, category):
        self.name = name  # название продукта (строка)
        self.weight = weight  # общий вес товара (дробное число)
        self.category = category  # категория товара (строка)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')  # , encoding='utf-8'
        text = file.read()
        file.close()
        return text

    def add(self, *products):
        shop_products = self.get_products().split("\n")
        for index in range(len(products)):
            new_pt = str(products[index])
            if new_pt in shop_products:
                print(f"Продукт {new_pt} уже есть в магазине")
            else:
                shop_products.append(new_pt)
        text = "\n".join(shop_products)
        file = open(self.__file_name, 'w')  # , encoding='utf-8'
        file.write(text)
        file.close()


if __name__ == '__main__':
    magnet = Shop()
    magnet.get_products()

    # Пример работы программы:
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())

