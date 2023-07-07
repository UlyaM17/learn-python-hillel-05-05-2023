from animals import Dog, Hen, Cow, Cat
from random import choices, choice, randint

if __name__ == '__main__':
    animals = [
        Dog('Jack', 3),
        Hen('Koko', 2),
        Cow('Milka', 5),
        Cat('Loki', 2)
    ]

    available_food = ['hay', 'grass', 'wheat', 'millet', "meat", 'bone', 'cake', "chicken", "salmon", "milk"]

    what_we_got = list()
    what_we_lost = list()
    for animal in animals:
        animal.say()
        for food in choices(available_food, k=3):
            what_we_lost.append(food)
            animal.eat(food)
        if animal.hungry:
            print(f'{animal} is hungry! Food is needed.')
        what_we_got.append(animal.treat(randint(0, 5)))
        if animal.sick:
            animal.vet(minutes=randint(1, 60))
            print(f'{animal} needs to see a vet!')
            print('=' * 20)

    print(f'Farm has spent today: {", ".join(what_we_lost)} and gained: {", ".join(what_we_got)}')
