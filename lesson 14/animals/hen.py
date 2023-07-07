from .animal import Animal
from random import randint


class Hen(Animal):
    """
    Ответственность класса может быть как под именем класса, так и в __init__
    Класс отвечает за симуляцию животного курица
    """
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Cluck-cluck'
    ):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'wheat', 'millet'}
        )
        self.animal_type = 'Hen'

    def treat(self, hours: int) -> str:
        """
        if hen is being treated well for specific time,
        we get 10 eggs, if less, we get 1 to 5 eggs
        :param hours: time treated
        :return: 1 to 10 eggs
        """
        if hours > 2:
            print(f'You are treating {self} for {hours} hours and are getting 10 eggs.')
            return 'Eggs received: 10'
        print(f'You are treating {self} for {hours} hours and are getting a few eggs.')
        return f'Eggs received: {randint(1, 5)}'

    def vet(self, minutes: int):
        """
        :param: hours at the vet
        :return:
        """
        if not self.sick:
            # animal feels good and does not need a vet
            return
        if self.sick:
            # animal is sick, so is at the vet
            print(f'{self} is being treated by a vet!!!')
            if minutes > 30:
                # the vet treats the animal for over half hour
                # so the animal is now healthy
                self.sick = False
                print(f'{self} is now feeling good!')

