from .animal import Animal


class Cat(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Meow-Meow!!!'
    ):
        """
        this class imitates the cat
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'chicken', 'salmon', 'milk'}
        )
        self.animal_type = 'Cat'

    def treat(self, hours: int) -> str:
        """
        :param hours: hours outside
        :return: none, or happiness
        """
        if hours > 2:
            # if outside for over 2 hours: happy animal and owner
            print(f'You are walking {self} for {hours} hours and you are feeling happy.')
            return 'happiness!'
        print(f'You are walking {self} for {hours} hours.')
        return ''

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
