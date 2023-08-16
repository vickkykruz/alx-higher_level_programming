#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    arr_num = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    num = 0
    i = 0

    while i < len(roman_string):
        curr = roman_string[i]
        if i == len(roman_string) - 1:
            num += arr_num[curr]
            break
        nxt = roman_string[i + 1]

        if arr_num[curr] >= arr_num[nxt]:
            num += arr_num[curr]
        else:
            num += arr_num[nxt] - arr_num[curr]
            i += 1
        i += 1
    return num
