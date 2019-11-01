def addition(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sol = num1 + num2
    return sol


def subtraction(num1, num2):
    sol = num2 - num1
    return sol


def multiplication(num1, num2):
    sol = num1 * num2
    return sol


def division(num1, num2):
    sol = num1 / num2
    return sol


def square(num1):
    sol = num1 ** 2
    return sol


def square_root(num1):
    sol = num1 ** 0.5
    return sol


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
