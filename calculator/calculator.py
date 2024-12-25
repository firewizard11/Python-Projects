class Calculator():

    def __init__(self):
        self.total: int = 0
        self.digits: str = '0'
        print(self)
    
    def __str__(self):
        return f'Total: {self.digits}'
    
    def add(self, operand: int) -> None:
        self.total += operand
        
        self.update_digits()
        print(self)

    def subtract(self, operand: int) -> None:
        self.total -= operand

        self.update_digits()
        print(self)

    def multiply(self, operand: int) -> None:
        self.total = self.total * operand

        self.update_digits()
        print(self)

    def divide(self, operand: int) -> None:
        self.total = self.total // operand
        
        self.update_digits()
        print(self)

    def update_digits(self) -> None:
        self.digits = str(self.total)

    def add_digits(self, digit: int) -> None:
        if self.total == 0:
            self.digits = str(digit)
        else:
            self.digits += str(digit)

        self.total = int(self.digits)

        print(self, self.total)

    def clear_digits(self) -> None:
        self.digits = '0'
        self.total = 0

        print(self, self.total)


if __name__ == '__main__':
    print('====== Creation ======')
    calc = Calculator()

    print('====== Addition ======')
    calc.add(5)
    calc.add(15)

    print('====== Subtraction ======')
    calc.subtract(7)
    calc.subtract(3)

    print('====== Multiplication ======')
    calc.multiply(3)
    calc.multiply(5)

    print('====== Division ======')
    calc.divide(5)
    calc.divide(3)

    print('====== Digit Ops ======')
    calc.add_digits(5)
    calc.clear_digits()

    calc.add_digits(3)
    calc.add_digits(2)
    calc.clear_digits()