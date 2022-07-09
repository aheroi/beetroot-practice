# def repeat(s, exclaim):
#     """
#     Returns the string 's' repeated 3 times.
#     If exclaim is true, add exclamation marks.
#     """
#
#     result = s + s + s  # can also use "s * 3" which is faster (Why?)
#     if exclaim:
#         result = str(result) + '!!!'
#     print(result)
#
# a = repeat(s=10, exclaim="!")


# def main(name):
#     if name == 'Guido':
#         print(repeeeet(name) + '!!!')
#     else:
#         print(repeat(name))
#
# if __name__ == '__main__':
#     a = main('Al')

import sys

for path in sys.path:
    print(path)
