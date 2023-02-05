# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        sum_result = function(args[0], args[1], args[2])
        inputs = ''
        for arg in args:
            inputs += f'{arg},'
        inputs = inputs[:len(inputs)-1]
        print(f'You called {function.__name__}({inputs})')
        print(f'IT returned: {sum_result}')
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(*args):
    sum_result = 0
    for arg in args:
        sum_result += arg
    return sum_result


a_function(1, 2, 4)
