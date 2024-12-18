# : Create the logging_decorator() function 👇
def logging_decorator(function):
    def inner(*args, **kwargs):
        print(f"you called {function.__name__}{args}")
        result = function()
        print(f"It returned: {result}")

    return inner


# : Use the decorator 👇


@logging_decorator
def a_function(*args):
    result = sum(args)
    print(result)
    return result


a_function(1, 2, 3)
