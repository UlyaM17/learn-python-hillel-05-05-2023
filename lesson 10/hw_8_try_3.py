my_list = []


def notes_list(user_entry) -> list:
    while True:
        user_entry = input(f"{user_entry}\n>>")
        try:
            # all work, but add key word as well to the list
            d = {'add': my_list.append(user_entry),
                 'earliest': my_list,
                 'latest': my_list[::-1],
                 'shortest': sorted(my_list, key=len),
                 'longest': sorted(my_list, key=len, reverse=True)
                 }
            if 'add' in user_entry:
                # returns 'None"
                print(d['add'])
            if 'earliest' in user_entry:
                print(d['earliest'])
            if 'latest' in user_entry:
                print(d['latest'])
            if 'shortest' in user_entry:
                print(d['shortest'])
            if 'longest' in user_entry:
                print(d['longest'])
        except Exception:
            # does not work
            print('Please continue')


if __name__ == '__main__':
    while True:
        notes_completed = notes_list(user_entry='Please add note or input command: add, earliest, latest, shortest or '
                                                'longest \n>>')
        print(notes_completed)
