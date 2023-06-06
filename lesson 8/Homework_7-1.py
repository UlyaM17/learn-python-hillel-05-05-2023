

def read_entry(user_prompt):
    """
        function checks if the number is numeric and whole
        :param user_prompt: user entry
        :return: yes, not
        """
    while True:
        user_input = input(f'{user_prompt}\n>> ')
        try:
            # is a whole number
            user_input = int(user_input)
            if user_input != float(user_input):
                return True
            else:
                return False
        except Exception:
            # if decimal/ negative number entered
            print(f'\nPlease enter a whole number')


def converting(number):
    """
        :param: number
        :return: dictionary
        """
    while True:
        seconds = input(f'{number}\n>> ')
        minutes, seconds = divmod(number, 60)
        hours, minutes = divmod(minutes, 60)
        print(f"{number}s is {hours}h {minutes}m {seconds}s")


if __name__ == '__main__':
    while True:
        if read_entry(user_prompt='Enter number of seconds\n>> '):
            converting()
        else:
            print('\n\tYour entry could not be converted')
