from cmath import sqrt


# adding square root import for the area function
# using cmath, to prevent error if square root of negative number


def read_user_number(user_prompt, lower_bound=0, upper_bound=9999999):
    # first function reads the values entered
    # determines if the values are numeric
    while True:
        number = input(f'\n{user_prompt}\n> ')
        try:
            # looking for a numeric value
            number = float(number)
            return number
        except Exception:
            # if value entered is not a numeric value
            print(f'\nPlease enter a numeric value')


def if_triangle_exist():
    # second function determines if triangle is possible
    # with values entered by user
    if (a + b) > c and (b + c) > a and (c + a) > b:
        # if conditions are met, triangle exists
        print('Triangle is valid')
        return True
    else:
        # are and perimeter are not found
        # because triangle is not valid
        print('Triangle is not valid')
        return False


def calculating():
    # third function stores all calculation methods needed
    p = (a + b + c)  # perimeter
    half_p = (p / 2)  # half of perimeter for area function
    area = sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))  # area function
    # finding value of area via 'area' formula
    print(f'\tarea: {area} cm²')
    # finding value of perimeter via 'p' formula
    print(f'\tperimeter: {p} cm')


if __name__ == "__main__":
    # code outside function
    # combines all previous functions into one
    print(type(read_user_number), read_user_number)
    while True:
        a = read_user_number('Enter first side of a triangle a cm')
        b = read_user_number('Enter second side of a triangle b cm')
        c = read_user_number('Enter third side of a triangle c cm')
        if if_triangle_exist() is True:
            calculating()

