total = 0

while True:
    number = input('Please enter your number:\n>')
    if number == 'sum':
        print(total)
        break
    else:
        try:
            number = float(number)
            total += number
        except:
            print('Please enter a numeric value, I cannot count letters:)')

