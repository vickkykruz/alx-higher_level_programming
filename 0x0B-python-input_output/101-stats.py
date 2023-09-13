#!/usr/bin/python3
"""
    This is a ``log_parsing module that reads stdin line by line and computes
    matrics
"""


import sys


class Magic:
    """ This is a class Magic that generate instance
    """

    def __init__(self):
        """ This is a method that initizaed the objects """
        self.size = 0
        self.dict = {}

    def init_dict(self):
        """ In this method we are initizating the dict """
        self.dict['200'] = 0
        self.dict['301'] = 0
        self.dict['400'] = 0
        self.dict['401'] = 0
        self.dict['403'] = 0
        self.dict['404'] = 0
        self.dict['405'] = 0
        self.dict['500'] = 0

    def add_status_code(self, status):
        """ This is a method that repeate number to the status code """

        if status in self.dict:
            self.dict[status] += 1

    def print_info(self, sig=0, frame=0):
        """ This is a method that print the status code """
        print("File size: {:d}".format(self.size))
        for key in sorted(self.dict.keys()):
            if self.dict[key] != 0:
                print("{}: {:d}".format(key, self.dict[key]))


if __name__ == "__main__":
    magic = Magic()
    magic.init_dict()
    lines = 0

    try:
        for line in sys.stdin:
            if lines % 10 == 0 and lines != 0:
                magic.print_info()

            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                magic.add_status_code(list_line[-2])
                magic.size += int(list_line[-1].strip("\n"))
            except Exception:
                pass
            lines += 1
    except KeyboardInterrupt:
        magic.print_info()
        raise
    magic.print_info()
