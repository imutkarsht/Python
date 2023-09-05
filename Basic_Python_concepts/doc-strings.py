# docstring --> String literal that appear right after definition of func, methods, classs and module

def square(n):
    ''' Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

print(square.__doc__)    # To access doc string
                         # different from comment as interpreter recongises that
                         # should be put either just before a module or right after it                         