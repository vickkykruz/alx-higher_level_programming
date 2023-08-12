#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght == 0:
        first_ch = None
    else:
        first_ch = sentence[0]

    new_tuple = lenght, first_ch
    return new_tuple
