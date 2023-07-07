class Animal:
    def __init__(self, name: str, age: int, say_word: str, preferred_food: set):
        """
        :param name
        :param age
        :param say_word
        :param preferred_food
        """
        self.animal_type = '???'
        self.name = name
        self.age = age
        self.say_word = say_word
        self.preferred_food = preferred_food
        self.hungry = True
        self.sick = True

    def __str__(self):
        return f'{self.animal_type} {self.name}'

    def say(self):
        print(f'{self} says: {self.say_word}')

    def eat(self, food: str):
        """
        :param food
        """
        if not self.hungry:
            return
        if food in self.preferred_food:
            print(f'{self} eats {food}')
            self.hungry = False
        else:
            print(f'{self} does not eat: {food}')
            self.say()

    def treat(self, hours: int):
        """
        :param hours
        :return:
        """
        raise NotImplementedError

    def vet(self, minutes: int):
        """
        :param: minutes: at the vet, if more than 30- animal is now healthy
        :return:
        """
