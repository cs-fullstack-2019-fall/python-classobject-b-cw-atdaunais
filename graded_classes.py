# main function to call all the code that will show up in the terminal
def main():
    newDog = Dog("Spot", "Chihuahua", "White", "Male")
    newDog.printAttributes()
    quit_func()
    newProduct = Product("Gum", 1, 60)
    # prints the values assigned from a new instance of Product in an f-string
    print(f"The product name is {newProduct.name}, it costs ${newProduct.price}, and we currently hold {newProduct.quantity} of them.")


class Dog:
    def __init__(self, name, breed, color, gender):
        self.name = name
        self.breed = breed
        self.color = color
        self.gender = gender

    # prints the values assigned to a Dog object in an f-string template
    def printAttributes(self):
        print(f"Your dog's name is {self.name}.\nThey are a {self.breed}, their color is {self.color}, and they are {self.gender}.")


# quits a while loop if the user enters an = sign
def quit_func():
    userInput = ""
    while userInput != "=":
        userInput = input("Enter anything at all or press '=' to quit the function: ")


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # each of these methods tell the current value of the name, price, or quantity then allows user to input a new value that is saved into the paramter
    def changeName(self):
        self.name = input(f"The product name is currently {self.name}. What would you like to change the name to?\n")
        print(f"The name is now {self.name}.")

    def changeNamePrice(self):
        self.name = input(f"The product name is currently {self.name}. What would you like to change the name to?\n")
        self.price = input(f"The product price is currently ${self.price}. What would you like to change the price to?\n")
        print(f"The name is now {self.name}, and the updated price is ${self.price}.")

    def changeNamePriceQuantity(self):
        self.name = input(f"The product name is currently {self.name}. What would you like to change the name to?\n")
        self.price = input(f"The product price is currently ${self.price}. What would you like to change the price to?\n")
        self.quantity = input(f"We have {self.quantity} of this product. What would you like to change the quantity to?\n")
        print(f"The name is now {self.name}, it costs ${self.price} and we hold {self.quantity} of them.")


# calls the main function which contains the answers for each problem
main()
