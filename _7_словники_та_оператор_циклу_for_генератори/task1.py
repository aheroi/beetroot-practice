"""
Make a program that has some sentence (a string) on input and returns a dict
containing all unique words as keys and the number of occurrences as values. 
"""

input_text = '''Remember that while Python list comprehensions get a lot of attention, 
    your intuition and ability to use data when it counts will help you write clean
    code that serves the task at hand. This, ultimately, is the key to making your code Pythonic!'''

dict_res = {ch: input_text.count(ch) for ch in input_text}
print(dict_res)

