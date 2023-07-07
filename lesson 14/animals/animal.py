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
        # each animal has their own sound
        print(f'{self} says: {self.say_word}')

    def eat(self, food: str):
        """
        :param food
        """
        # if animal is not hungry
        if not self.hungry:
            return
        # if animal is hungry
        if food in self.preferred_food:
            print(f'{self} eats {food}')
            # after eating, animal is now not hungry
            self.hungry = False
        else:
            # if preferred food was not given to specific animal
            print(f'{self} does not eat: {food}')
            # animal "says" that this food is not what it likes
            self.say()

    def treat(self, hours: int):
        """
        :param hours
        :return:
        """
        # hours the owner spends with the animal
        raise NotImplementedError

    def vet(self, minutes: int):
        """
        :param: minutes: # at the vet, if more than 30- animal is now healthy
        :return:
        """
