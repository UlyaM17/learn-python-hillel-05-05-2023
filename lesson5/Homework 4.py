
EXIT_COMMAND = 'sum'

while True:
    print('Please enter your number')
    number = input()
    try:
        number = int(number)
        print('Your number is', number, 'please enter your next number or sum')
    except:
        print('Please indicate a numeric value or sum')
        break

numbern = input()
a = (number, numbern)
while True:
    numbern = input()
    try:
        numbern = int(numbern)
        print('Your number is', numbern, 'please enter your next number')
    except:
        if 'sum' in input():
            print(sum(a))





