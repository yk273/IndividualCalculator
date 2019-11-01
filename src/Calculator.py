def addition(num1, num2):
    solution = num1 + num2
    return solution


def subtraction(num1, num2):
    solution = num2 - num1
    return solution


def multiplication(num1, num2):
    solution = num1 * num2
    return solution


def division(num1, num2):
    solution = num1 / num2
    return solution


def square(num1):
    solution = num1 ** 2
    return solution


def square_root(num1):
    solution = num1 ** 0.5
    return solution


class Calculate:
    result = 0

    def __init__(self):
        pass

    def add(self, num1, num2):
        self.result = num1 + num2
        return self.result

    def subtract(self, num1, num2):
        self.result = num1 - num2
        return self.result

    def multiply(self, num1, num2):
        self.result = num1 * num2
        return self.result

    def divide(self, num1, num2):
        self.result = num1 / num2
        return self.result

    def square(self, num1):
        self.result = num1 ** 2
        return self.result

    def square_root(self, num1):
        self.result = num1 ** 0.5
        return self.result
