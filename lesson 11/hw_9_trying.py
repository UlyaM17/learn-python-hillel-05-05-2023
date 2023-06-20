# to stop the program after "save"
from sys import exit as system_exit
# key command words to read from the user
VALID_COMMANDS = ("add", "earliest", "latest", "longest", "shortest", "save")


def get_input():
    # user commands
    # explanations for the user to match exact command key
    print("Please enter a command from the following list:")
    print("add:      add a new note")
    print("earliest: to print from earliest to latest")
    print("latest:   to print from latest to earliest")
    print("longest:  to print from longest to shortest")
    print("shortest: to print from shortest to longest")
    print("save:     to save and exit \n>>")

    command = input()
    if command in VALID_COMMANDS:
        return command
    else:
        # if user entered something else
        # stored command is not entered
        return None


def print_list(list):
    # to print each entry in new line
    # for better look
    for i in range(len(list)):
        print(list[i])


def add_note(existing_notes, new_note):
    # adding new note only
    existing_notes.append(new_note)
    return existing_notes


def save_notes(existing_notes):
    # writes to f
    # w= write something
    with open("notes_file", "w") as f:
        # join list lines
        f.write("\n".join(existing_notes))


def read_notes():
    # to read if notes file exists
    # r= read something
    # not sure about this one
    try:
        # to split
        with open("notes_file", "r") as f:
            existing_notes = f.read().splitlines()
    except Exception:
        # if no file/ empty
        existing_notes = []
    return existing_notes


if __name__ == '__main__':
    # get saved notes?
    # not sure about this one
    notes = read_notes()
    while True:
        # repeats
        command = get_input()
        if command:
            if command == "add":
                # add note
                new_note = input("Please add note: \n>>")
                add_note(notes, new_note)
            elif command == "save":
                # to save and exit
                save_notes(notes)
                # exit note to user:
                print("Goodbye!")
                # program exits
                system_exit()
            else:
                # other commands
                if command == "earliest":
                    sorted_notes = notes
                elif command == "latest":
                    sorted_notes = notes[::-1]
                elif command == "longest":
                    sorted_notes = sorted(notes, key=len, reverse=True)
                elif command == "shortest":
                    sorted_notes = sorted(notes, key=len)
                print_list(sorted_notes)
