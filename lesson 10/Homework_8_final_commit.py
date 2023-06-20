# user command as constants- to match exactly
VALID_COMMANDS = ("add", "earliest", "latest", "longest", "shortest")


def get_input():
    # user commands
    # explanations for the user to match exact command key
    print("Please enter a command from the following list:")
    print("add:      to add a new note")
    print("earliest: to print from earliest to latest")
    print("latest:   to print from latest to earliest")
    print("longest:  to print from longest to shortest")
    print("shortest: to print from shortest to longest \n>>")

    command = input()
    if command in VALID_COMMANDS:
        return command
    else:
        # if user entered something else
        # stored command is not entered
        return None


def print_array(array):
    # to print each entry in new line
    # for better look
    for i in range(len(array)):
        print(array[i])


def add_note(notes, new_note):
    # adding new notes only
    notes.append(new_note)
    return notes


if __name__ == '__main__':
    notes = []
    while True:
        # to repeat
        command = get_input()
        if command:
            if command == "add":
                new_note = input("Please add note: \n>>")
                add_note(notes, new_note)
            else:
                # keys to corresponding output
                if command == "earliest":
                    sorted_notes = [notes]
                elif command == "latest":
                    sorted_notes = notes[::-1]
                elif command == "longest":
                    sorted_notes = sorted(notes, key=len, reverse=True)
                elif command == "shortest":
                    sorted_notes = sorted(notes, key=len)
                print_array(sorted_notes)
