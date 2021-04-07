import math
from Exceptions import singleton_error
from Exceptions import bad_args


class Calculate:
    """Calculate result from arg_list
    """
    __instance = None

    def __init__(self):
        if Calculate.__instance != None:
            raise singleton_error.SingletonClassException()
        else:
            Calculate.__instance = self

    @staticmethod
    def get_instance():
        """return instance of Calculate
        """
        if Calculate.__instance == None:
            Calculate()
        return Calculate.__instance

    def convert_int(self, result):
        """return int if result is int else float
        """
        if result == int(result):
            return int(result)
        return result

    def add(self, arg_list):
        """return sum of all args in args_list
        """
        result = 0
        for element in arg_list:
            result += element
        return self.convert_int(result)

    def subtract(self, arg_list):
        """return difference between two numbers
        """
        if len(arg_list) > 2:
            raise bad_args

        result = arg_list[0] - arg_list[1]
        return self.convert_int(result)

    def multiply(self, arg_list):
        """return product of all in args_list
        """
        result = 1
        for arg in arg_list:
            result *= arg
        return self.convert_int(result)

    def divide(self, arg_list):
        """return division of two number
        """
        if len(arg_list) > 2:
            raise bad_args

        result = arg_list[0] / arg_list[1]
        return self.convert_int(result)

    def combination(self, arg_list):
        """wrapper of math package - return combination of two number
        """
        if len(arg_list) > 2:
            raise bad_args
            
        result = math.comb(arg_list[0], arg_list[1])
        return self.convert_int(result)

    def factorial(self, arg_list):
        """wrapper of math package - return factorial of a number
        """
        if len(arg_list) > 1:
            raise bad_args

        result = math.factorial(arg_list[0])
        return self.convert_int(result)

    def gcd(self, arg_list):
        """wrapper of math package - return gcd of numbers
        """
        result = math.gcd(arg_list)
        return self.convert_int(result)

    def lcm(self, arg_list):
        """wrapper of math package - return lcm of numbers
        """
        result = math.lcm(arg_list)
        return self.convert_int(result)

    def permutations(self, arg_list):
        """wrapper of math package - return permutation of two number
        """
        if len(arg_list) > 2:
            raise bad_args

        result = math.perm(arg_list[0], arg_list[1])
        return self.convert_int(result)

    def power(self, arg_list):
        """wrapper of math package - return power a ^ b
        """
        if len(arg_list) > 2:
            raise bad_args

        result = math.pow(arg_list[0], arg_list[1])
        return self.convert_int(result)
