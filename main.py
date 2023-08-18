class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def calculate_total_price(self):
        total_price = sum(product["price"] for product in self.cart_items)
        return total_price

    def display_cart(self):
        print("Contenu du panier :")
        for index, item in enumerate(self.cart_items):
            print(f"{index + 1}. {item['name']} - {item['price']} $")
        print(f"Pri total : {self.calculate_total_price()} $")


class Products:
    def __init__(self):
        self.products_list = []

    def load_products(self):
        self.products_list.append({"name": "Wob", "price": 10.0, "quantity": 5})
        self.products_list.append({"name": "tenis", "price": 20.0, "quantity": 10})
        self.products_list.append({"name": "Jip", "price": 30.0, "quantity": 20})
        self.products_list.append({"name": "sandal", "price": 700.0, "quantity": 50})
        self.products_list.append({"name": "pantalon", "price": 300.0, "quantity": 20})
        self.products_list.append({"name": "radyo", "price": 354.0, "quantity": 70})
        self.products_list.append({"name": "pafen", "price": 89.0, "quantity": 30})
        

         
        

    def display_products(self):
        print("Lis pwodui yo :")
        for index, product in enumerate(self.products_list):
            print(f"{index + 1}. {product['name']} - {product['price']} $")


def main():
    products = Products()
    products.load_products()

    cart = Cart()

    while True:
        print("Byenvini nan boutik anliy nou an !")
        print("1- Chaje youn ou plizye pwodui")
        print("2- we panye a ak tout pri li.")
        print("3- Femen")

        choice = input("Fe chwa ou : ")

        if choice == '1':
            products.display_products()
            product_choice = int(input("Chwazi nimewo pwodui ou vle ajoute nan panye an : "))
            if 1 <= product_choice <= len(products.products_list):
                selected_product = products.products_list[product_choice - 1]
                cart.add_to_cart(selected_product)
                print(f"{selected_product['name']} ou ajoute pwodui a ak sikse nan panye a.")
            else:
                print("Pwodui saa pa valid.")
        elif choice == '2':
            cart.display_cart()
        elif choice == '3':
            print("Mesi paske ou te fe chwa de boutik nou an !")
            break
        else:
            print("Chwa saa pa valid/ retounen eseye .")


if __name__ == "__main__":
    main()
