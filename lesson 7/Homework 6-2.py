
from cmath import sqrt


# adding square root import for the area function
# using cmath, to prevent error if square root of negative number


def read_user_number(user_prompt: float, lower_bound=0, upper_bound=9999999):
    while True:
        number = input(f'{user_prompt}\n>')
        try:
            # looking for a numeric value
            number = float(number)
            # making sure number is in given range
            if lower_bound < number < upper_bound:
                return number
            else:
                # if number is out of range
                print(f'Enter number: from {0} to {9999999}')
        except Exception:
            # if value entered is not a numeric value
            print(f'Could not get a number from: "{number}", please try again')


print(type(read_user_number), read_user_number)
a = read_user_number('Enter first side of a triangle a=')
b = read_user_number('Enter second side of a triangle b=')
c = read_user_number('Enter third side of a triangle c=')
p = (a + b + c)  # perimeter
half_p = (p / 2)  # half of perimeter for area function
area = sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))  # area function

if (a + b) > c and (b + c) > a and (c + a) > b:
    # if conditions are met, triangle exists
    print('Triangle is valid')
    # finding value of area via 'area' formula
    print('area:', area)
    # finding value of perimeter via 'p' formula
    print('perimeter:', p)
else:
    # are and perimeter are not found
    # because triangle is not valid
    print('Triangle is not valid')
