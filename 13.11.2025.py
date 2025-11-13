
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name: {self.name}\n"
              f"age: {self.age}\n")

    def age_group(self):
        if self.age >= 14:
            print("малой")
        else:
            print("пушистая")


if __name__ == '__main__':
    person1 = Person("Oleg", 27)
    person2 = Person("Ilya", 22)
    person3 = Person("Aleksandr", 30)

   person1.age_group()






