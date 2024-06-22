# mathematic.py

from operation import Operation

class Mathematic(Operation):
    def execute(self, a, b, operation):
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        else:
            raise ValueError("Unsupported operation")
