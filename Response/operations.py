class Operations:
    calculation_operation = {
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

    interaction_operation = {
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

    def __init__(self):
        pass
