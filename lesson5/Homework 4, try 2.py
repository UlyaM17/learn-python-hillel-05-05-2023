# starting with a zero value, so if there is only one number entered,
# program will understand where to take the second value for 'sum'

total = 0

while True:
    # user enters anything as an answer
    number = input('Please enter your number:\n>')
    if number == 'sum':
        # if the word 'sum' is detected in user's answer,

        # the program adds previously entered number to starting value

        # if the word 'sum' is entered as the first answer,
        # the total would be zero (the starting value)
        print(total)
        break
    else:
        try:
            # checking if user's entry is a digit
            number = float(number)
            total += number
        except:
            # if user's entry is not a digit, error message pops up
            print('Please enter a numeric value, I cannot count letters:)')

