# Class creation
class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof")

    def sit(self):
        print(f"{self.name} Sit Down!")


# Object creation
lily = dog("Lily", "Maltes");
ruby = dog("Ruby", "Police dog")

#Object calling
lily.bark()
ruby.sit()