from Response.operations import operations as op
from Response.calculation import Calculate
from Response.interaction import Interaction
from Response.Exceptions import bad_args


class ParseInput:
    def __init__(self, text=None):
        self.text = None
        self.arg_list = []
        self.calculate = Calculate()
        self.interact = Interaction()

    def input(self, text):
        self.text = text

    def filter_arg(self):
        arg = []
        for element in self.msg.split():
            try:
                arg.append(float(element))
            except ValueError:
                pass
        self.arg_list = arg

    def operate(self):
        if len(self.arg_list) >= 1:
            for element in self.msg.split():
                try:
                    return self.calculate.op.calculation_operation[element.lower()](arg_list)
                except (KeyError, bad_args, TypeError, ValueError):
                    pass
        else:
            for element in self.msg.split():
                try:
                    return self.interact.op.interaction_operation[element.lower()]()
                except KeyError:
                    pass

    def parse(self, input):
        self.input(text)
        self.filter_arg()
        self.operate()
