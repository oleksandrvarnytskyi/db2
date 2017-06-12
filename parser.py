# -*- coding: utf-8 -*-


def handle_string(value):
    """Function takes sentence as a parameter and count number of letters and
    digits"""
    text = unicode(value, 'utf - 8')
    letters = 0
    digits = 0

    for symbol in text:
        if symbol.isalpha():
            letters += 1
        elif symbol.isdigit():
            digits += 1

    print 'Result:\nLetters - {0}\nDigits - {1}'.format(letters, digits)


if __name__ == '__main__':
    handle_string('+++тттggg66888____""""@@   !!!')
