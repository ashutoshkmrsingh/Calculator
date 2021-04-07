from Response.operations import Operations
from Response.calculation import Calculate
from Response.interaction import Interaction
from Response.Exceptions.bad_args import BadArgumentExceptions


class ParseInput:
    def __init__(self, text=None):
        self.text = None
        self.arg_list = []
        self.operation = Operations()

    def input(self, text):
        self.text = text

    def filter_arg(self):
        arg = []
        for element in self.text.split():
            try:
                arg.append(float(element))
            except ValueError:
                pass
        self.arg_list = arg

    def operate(self):
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
        self.input(text)
        self.filter_arg()
        return self.operate()
