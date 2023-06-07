def read_user_number(user_prompt):
    """
            function checks if the number is numeric and whole
            :param user_prompt: user entry
            :return: yes, not
            """
    while True:
        try:
            user_input = input(f'{user_prompt}\n>> ')
            # is a whole number
            if user_input == int(user_input):
                return user_input
        except Exception:
            # if decimal/ negative number entered
            print(f'\nPlease enter a whole numeric value')


def convert_user_number(user_prompt) -> dict:
    """
            :param: number
            :return: dictionary
            """
    d = dict()
    if d:
        d = {'seconds': {user_prompt},
             'minutes': divmod(user_prompt, 60),
             'hours': divmod(user_prompt, (60 * 60)),
             'days': divmod(user_prompt, (24 * 60 * 60))
             }
        return d
    else:
        print(f'\nCould not calculate')


if __name__ == '__main__':
    while True:
        seconds_entry = read_user_number(user_prompt='Enter number of seconds\n>> ')
        seconds_converted = convert_user_number(seconds_entry)
        print(seconds_converted)

