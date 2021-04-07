import datetime as dt
from calculation_functions import *
from interactive_functions import *

time = dt.datetime.now()
time_str = time.strftime('%H%M%S')


def greet():
    time_right_now = int(time_str[:4])

    if (time_right_now >= 5) and (time_right_now <= 1159):
        print('HELLO! "Good Morning" What can I do for you ?')
    elif (time_right_now >= 12) and (time_right_now <= 459):
        print('HELLO! "Good Afternoon" What can I do for you ?')
    else:
        print('HELLO! "Good Evening" What can I do for you ?')


greet()


def filter_arg(msg):
    msg_list = msg.split()
    arg = []
    for element in msg_list:
        try:
            arg.append(float(element))
        except ValueError:
            pass
    return arg


def identify_operations_and_find_result(msg, arg_list):
    if len(arg_list) > 1:
        operations = {
            'add': add,
            'addition': add,
            'sum': add,
            '+': add,
            'plus': add,
            'difference': subtract,
            'differences': subtract,
            'subtract': subtract,
            'minus': subtract,
            '-': subtract,
            'multiply': multiply,
            'product': multiply,
            '*': multiply,
            'times': multiply,
            'divide': divide,
            'break': divide,
            '/': divide,
            '//': divide
        }
        for element in msg.split():
            try:
                return operations[element.lower()](arg_list)
            except KeyError:
                pass
    else:
        interactive_words = {
            'name': name,
            'who': created,
            'do': do,
            'feel': feel,
            'how': how,
            'amazing': amazing,
            'great': amazing,
            'oops': oops,
            'whats': whatsup,
            'quit': end_program,
            'close': end_program,
            'exit': end_program,
            'end': end_program,
            'kill': end_program,
            'age': age
        }
        for element in msg.split():
            try:
                return interactive_words[element.lower()]()
            except KeyError:
                pass
        else:
            return forbidden()


start = True
while start:
    msg = input()
    arg_list = filter_arg(msg)
    result = identify_operations_and_find_result(msg, arg_list)
    if result is not None:
        print(result)

