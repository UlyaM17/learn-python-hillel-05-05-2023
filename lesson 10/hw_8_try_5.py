def word_add(keyword_input) -> list:
    """
    :rtype: list
    """
    # my_list = []
    while True:
        user_input = input(f'{keyword_input}\n>>')
        if 'add' in user_input:
            user_list = user_input
            return [user_list]


def key_word_earliest(user_input: list) -> list:
    """
    :param user_input
    :return: list
    """
    if 'earliest' in user_input:
        user_list = user_input
        return [user_list.append(user_input)]


def key_word_latest(user_input: list) -> list:
    """
    :param user_input
    :return: list
    """
    if 'latest' in user_input:
        user_list = user_input
        return user_list.append(user_input)[::-1]


def key_word_shortest(user_input: list) -> list:
    """
    :param user_input
    :return: list
    """
    if 'shortest' in user_input:
        user_list = user_input
        return sorted(user_list, key=len)


def key_word_longest(user_input: list) -> list:
    """
    :param user_input
    :return: list
    """
    if 'longest' in user_input:
        user_list = user_input
        return sorted(user_list, key=len, reverse=True)


if __name__ == '__main__':
    while True:
        user_command = word_add(keyword_input='Please input a command: add, earliest, latest, shortest '
                                              'or '
                                              'longest \n>>')
        print(user_command)
        if user_command:
            earliest_entry = key_word_earliest(user_command)
            print(earliest_entry)
        if user_command:
            latest_entry = key_word_latest(user_command)
            print(latest_entry)
        if user_command:
            shortest_entry = key_word_shortest(user_command)
            print(shortest_entry)
        if user_command:
            longest_entry = key_word_longest(user_command)
            print(longest_entry)
