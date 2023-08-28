#!/usr/bin/python3
def magic_calculation(a, b):

    counter = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too Far")
            else:
                counter += (a ** b) / i
        except Exception:
            counter = b + a
            break

    return counter
