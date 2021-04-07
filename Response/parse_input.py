from Response.operations import Operations
from Response.calculation import Calculate
from Response.interaction import Interaction
from Response.Exceptions.bad_args import BadArgumentExceptions


class ParseInput:
    """Parse input, extract information like args and methods to bind
    """
    def __init__(self, text=None):
        self.text = None
        self.arg_list = []
        self.operation = Operations()

    def input(self, text):
        """take text and assign it to object
        """
        self.text = text

    def filter_arg(self):
        """filter argument to perform numerical operations
        """
        arg = []
        for element in self.text.split():
            try:
                arg.append(float(element))
            except ValueError:
                pass
        self.arg_list = arg

    def operate(self):
        """call methods wrt args
        """
        if len(self.arg_list) >= 1:
            for element in self.text.split():
                try:
                    return self.operation.calculation_operation[element.lower()](self.arg_list)
                except (KeyError, TypeError, ValueError, BadArgumentExceptions):
                    pass
        else:
            for element in self.text.split():
                try:
                    return self.operation.interaction_operation[element.lower()]()
                except KeyError:
                    pass

    def parse(self, text):
        """bind input, filter_arg and operate
        """
        self.input(text)
        self.filter_arg()
        return self.operate()
