
'''
Task 1
Write a function called oops that explicitly raises an IndexError exception when called. Then write another function that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to raise KeyError instead of IndexError?
'''

def f():
    raise ZeroDivisionError

if __name__ == '__main__':
    f()
