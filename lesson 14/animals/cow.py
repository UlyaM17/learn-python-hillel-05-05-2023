from .animal import Animal


class Cow(Animal):
    def __init__(self, name: str, age: int, say_word='Moooooo!'):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'grass', 'hey'}
        )
        self.animal_type = 'Cow'

    def treat(self, hours: int) -> str:
        """
        :param hours: time treated
        :return: milk or nothing
        """
        if hours > 1:
            print(f'You are treating {self} for {hours} hours and get a bucket of milk.')
            return 'A bucket of milk'
        print(f'You are treating {self} for {hours} hours.')
        return ''

    def vet(self, minutes: int):
        """
        :param: hours at the vet
        :return:
        """
        if not self.sick:
            return
        if self.sick:
            print(f'{self} is being treated by a vet!!!')
            if minutes > 30:
                self.sick = False
                print(f'{self} is now feeling good!')

