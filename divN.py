class DivisionByZeroException(Exception):
    pass


def handle_numbers(number1, number2, number3):
    """Function returns the count of integers that are divisible by
    number3 in range [number1, number2]"""
    if number3 == 0:
        raise DivisionByZeroException('Impossible to do division by 0!')

    divider = number3
    if number3 < 0:
        divider = abs(number3)

    min_num = number1
    max_num = number2

    if number1 > number2:
        min_num = number2
        max_num = number1

    multiple = min_num - min_num % divider

    if multiple < min_num:
        multiple += divider

    divisible_numbers = []
    count = 0

    while multiple <= max_num:
        divisible_numbers.append(multiple)
        multiple += divider
        count += 1

    if divisible_numbers:
        print 'Result:\n{0} because {1} {2} divisible by {3}'.format(
            count,
            ', '.join(str(num) for num in divisible_numbers),
            'are' if len(divisible_numbers) > 1 else 'is',
            number3)
    else:
        print 'Result:\n{0} because there are no numbers divisible by {1} in' \
              ' range [{2}, {3}]'.format(count, number3, number1, number2)

if __name__ == '__main__':
    print
    handle_numbers(-20, -5, -6)
