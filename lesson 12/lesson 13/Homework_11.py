# cat breeds: siamese, british shorthair, persian, sphynx, scottish fold, etc.
from random import choices, randint, random


class Cat:
    # body
    # self
    def __init__(self, name: str, breed: str, preferred_food: set):
        """
        Class cat
        :param name: name
        :param breed:
        :param preferred_food: food this cat likes
        """
        self.name = name
        self.breed = breed
        self.preferred_food = preferred_food
        # is feeding needed?
        self.hungry = True
        # hours running outside, starting with 0
        self.hours_outdoors = 0

    def meow(self, count: int):
        if count > 0:
            meowing_str = '-'.join(["meow"] * count).capitalize()
            print(f"{self.name} meows: {meowing_str}!")

    def eat(self, food: str):
        if self.hungry:
            # if the food given is one cat likes
            if food in self.preferred_food:
                print(f"{self.name} eats {food}")
                # cat if fed, not hungry anymore
                self.hungry = False
            else:
                # if this can does not like given food
                print(f"{self.name} does not eat: {food}")
                self.meow(randint(1, 3))
        else:
            print(f"{self.name} is not hungry")

    def walk(self):
        """
        :param self:
        :return: if out for more than 2 hours= hungry
        """
        hours = randint(1, 4)
        print(f"{self.name} walks outside for {hours} hours")
        self.hours_outdoors += hours
        # after 2 hours of running outside, cat needs food
        if self.hours_outdoors > 2:
            self.hungry = True
        return f'{self.name} is hungry'


if __name__ == '__main__':
    a = Cat('Loki', "siamese", {'salmon'})
    b = Cat('Mimi', "british shorthair", {'salmon', 'chicken'})
    c = Cat('William', "persian", {'chicken', 'milk'})
    d = Cat('Cleo', "sphynx", {'pate', 'liver', 'salmon'})
    e = Cat("Max", "scottish fold", {'milk', 'liver'})
    f = Cat('Mia', 'sphynx', {'chicken', 'salmon', 'pate', 'liver'})
    cats = [a, b, c, d, e, f]

    print(a.name, b.name, c.name, d.name, e.name, f.name)

    # food choices for all cats
    potential_food = ['salmon', 'chicken', 'cookies', 'milk', 'pate', 'liver']
    print('-' * 30)
    for cat in cats:
        events_for_cat = randint(1, 7)
        for _ in range(events_for_cat):
            if random() > 0.5:
                print(f'Feeding {cat.name}')
                for random_food in choices(potential_food, k=3):
                    cat.eat(random_food)
            else:
                if random() > 0.5:
                    result = cat.walk()
                    print(f'Cat owner sees that: {result}')
        print(f'day has ended for: {cat.name}')
        print('=' * 30)
