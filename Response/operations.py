from Response.calculation import Calculate
from Response.interaction import Interaction


class Operations:
    def __init__(self):
        self.calculate = Calculate()
        self.interact = Interaction()

        self.calculation_operation = {
            'add': self.calculate.add,
            'addition': self.calculate.add,
            'sum': self.calculate.add,
            '+': self.calculate.add,
            'plus': self.calculate.add,
            'difference': self.calculate.subtract,
            'differences': self.calculate.subtract,
            'subtract': self.calculate.subtract,
            'minus': self.calculate.subtract,
            '-': self.calculate.subtract,
            'multiply': self.calculate.multiply,
            'product': self.calculate.multiply,
            '*': self.calculate.multiply,
            'times': self.calculate.multiply,
            'divide': self.calculate.divide,
            'break': self.calculate.divide,
            '/': self.calculate.divide,
            '//': self.calculate.divide,
        }

        self.interaction_operation = {
            'name': self.interact.name,
            'who': self.interact.name,
            'do': self.interact.do,
            'feel': self.interact.feel,
            'how': self.interact.how,
            'amazing': self.interact.amazing,
            'great': self.interact.amazing,
            'oops': self.interact.oops,
            'whats': self.interact.whatsup,
            'age': self.interact.age,
        }
