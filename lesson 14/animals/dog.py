from .animal import Animal


class Dog(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Bark-bark'
    ):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'meat', 'bone'}
        )
        self.animal_type = 'Dog'

    def treat(self, hours: int) -> str:
        """
        :param hours: how long outside
        :return: none or happiness
        """
        if hours > 2:
            print(f'You are walking with {self} for {hours} hours and you become happy')
            return 'happiness'
        print(f'You are walking with {self} for {hours} hours.')
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
