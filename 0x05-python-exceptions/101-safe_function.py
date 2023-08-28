#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        res = fct(*args)
    except (ZeroDivisionError, Exception) as err:
        sys.stderr.write("Exception: {}\n".format(err.args[0]))
        res = None

    return res
