from tkinter import *
from tkinter import ttk
from enum import Enum, auto

from calculator import Calculator


class Mode(Enum):
    DIGIT = auto()
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()


class calc_gui():

    def __init__(self):
        self.calc = Calculator()
        self.mode = Mode.DIGIT
        
        self.root = Tk()
        
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()

        self.display_label = StringVar(value=self.calc.digits)
        self.display = ttk.Label(self.frame, textvariable=self.display_label)
        self.display.grid(column=0, row=0, columnspan=4)

        self.button_0 = ttk.Button(self.frame, text='0', command=lambda:(self.button_num_action(0)))
        self.button_0.grid(column=1, row=4)

        self.button_1 = ttk.Button(self.frame, text='1', command=lambda:(self.button_num_action(1)))
        self.button_1.grid(column=0, row=3)

        self.button_2 = ttk.Button(self.frame, text='2', command=lambda:(self.button_num_action(2)))
        self.button_2.grid(column=1, row=3)

        self.button_3 = ttk.Button(self.frame, text='3', command=lambda:(self.button_num_action(3)))
        self.button_3.grid(column=2, row=3)

        self.button_4 = ttk.Button(self.frame, text='4', command=lambda:(self.button_num_action(4)))
        self.button_4.grid(column=0, row=2)

        self.button_5 = ttk.Button(self.frame, text='5', command=lambda:(self.button_num_action(5)))
        self.button_5.grid(column=1, row=2)

        self.button_6 = ttk.Button(self.frame, text='6', command=lambda:(self.button_num_action(6)))
        self.button_6.grid(column=2, row=2)

        self.button_7 = ttk.Button(self.frame, text='7', command=lambda:(self.button_num_action(7)))
        self.button_7.grid(column=0, row=1)

        self.button_8 = ttk.Button(self.frame, text='8', command=lambda:(self.button_num_action(8)))
        self.button_8.grid(column=1, row=1)

        self.button_9 = ttk.Button(self.frame, text='9', command=lambda:(self.button_num_action(9)))
        self.button_9.grid(column=2, row=1)

        self.button_plus = ttk.Button(self.frame, text='+', command=lambda:self.button_op_action(Mode.ADD))
        self.button_plus.grid(column=3, row=4)

        self.button_minus = ttk.Button(self.frame, text='-', command=lambda:self.button_op_action(Mode.SUBTRACT))
        self.button_minus.grid(column=3, row=3)

        self.button_multiply = ttk.Button(self.frame, text='X', command=lambda:(self.button_op_action(Mode.MULTIPLY)))
        self.button_multiply.grid(column=3, row=2)

        self.button_divide = ttk.Button(self.frame, text='/', command=lambda:(self.button_op_action(Mode.DIVIDE)))
        self.button_divide.grid(column=3, row=1)

        self.button_clear = ttk.Button(self.frame, text='C', command=lambda:(self.clear_display()))
        self.button_clear.grid(column=2, row=4)

        self.root.mainloop()

    def update_display(self):
        self.display_label.set(self.calc.digits)

    def clear_display(self):
        self.calc.clear_digits()
        self.update_display()

    def button_num_action(self, number: int):
        if self.mode == Mode.DIGIT:
            self.calc.add_digits(number)
        elif self.mode == Mode.ADD:
            self.calc.add(number)
        elif self.mode == Mode.SUBTRACT:
            self.calc.subtract(number)
        elif self.mode == Mode.MULTIPLY:
            self.calc.multiply(number)
        elif self.mode == Mode.DIVIDE:
            self.calc.divide(number)

        self.mode = Mode.DIGIT
        self.update_display()

    def button_op_action(self, operation):
        self.mode = operation

if __name__ == '__main__':
    gui = calc_gui()