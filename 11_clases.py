## CLass

class Person:
    def __init__(self, name, username):
        self.__name = name
        self.username = username
        self.fullname = f"{name} {username}"
    
    def get_Name(self):
        return self.__name

    def walk(self):
        print(f"{self.fullname} esta caminando")
        

my_person = Person("Ezequiel", "Ramirez")
print(my_person.get_Name())
my_person.walk()