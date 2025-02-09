def suma(*args):
    s = 0

    for arg in args :
        s +=arg
    return s
suma (1, 3, 4, 2)

def suma(*args):
     return sum(args)