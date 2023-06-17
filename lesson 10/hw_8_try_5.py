
def key_word_add(keyword_input) -> list:
    """
    :rtype: list
    """
    my_list = []
    while True:
        user_input = input(f'{keyword_input}\n>>')
        if 'add' in user_input:
            return [my_list.append(user_input)]


def key_word_earliest(user_input: list) -> list:
    """
    :param user_input
    :return: list
    """
    if 'earliest' in user_input:
        return [user_input.append(user_input)]


def key_word_latest(user_input: list) -> list:
    """
    :param user_input
    :return: list
    """
    if 'latest' in user_input:
        return user_input.append(user_input)[::-1]


def key_word_shortest(user_input: list) -> list:
    """
    :param user_input
    :return: list
    """
    if 'shortest' in user_input:
        return sorted(user_input, key=len)


def key_word_longest(user_input: list) -> list:
    """
    :param user_input
    :return: list
    """
    if 'longest' in user_input:
        return sorted(user_input, key=len, reverse=True)


if __name__ == '__main__':
    while True:
        user_command = key_word_add(keyword_input='Please add note or input command: add, earliest, latest, shortest '
                                                  'or'
                                                  'longest \n>>')
        print(user_command)
        earliest_entry = key_word_earliest(user_command)
        if earliest_entry:
            print(earliest_entry)
        latest_entry = key_word_latest(user_command)
        if latest_entry:
            print(latest_entry)
        shortest_entry = key_word_shortest(user_command)
        if shortest_entry:
            print(shortest_entry)
        longest_entry = key_word_longest(user_command)
        if longest_entry:
            print(longest_entry)

