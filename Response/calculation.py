import math

def check_int(result):
    if result == int(result):
        return int(result)
    return result

def wrong_arguments():
    print('Sorry the arguments are not valid')


def add(arg_list):
    result = 0
    for element in  arg_list:
        result += element
    return check_int(result)


def subtract(arg_list):
    if len(arg_list) > 2:
        wrong_arguments()
    result = arg_list[0] - arg_list[1]
    return check_int(result)


def multiply(arg_list):
    result = 1
    for arg in arg_list:
        result *= arg
    return check_int(result)


def divide(arg_list):
    if len(arg_list) > 2:
        wrong_arguments()
    result = arg_list[0] / arg_list[1]
    return check_int(result)
