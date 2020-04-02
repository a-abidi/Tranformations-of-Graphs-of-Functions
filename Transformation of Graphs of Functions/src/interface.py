import math
from tkinter import *

from func import *
from util import *
from config import *

# List of mathematical functions to be used and called
MathFunctionList = [
    MathFunction.linear,
    MathFunction.quadratic,
    MathFunction.cubic,
    MathFunction.sine,
    MathFunction.cosine,
    MathFunction.tang,
    MathFunction.expo,
    MathFunction.inv,
    MathFunction.modulus
]


get = [
    ValueReader.get_a, # f(a*x) validation (no range check required)
    ValueReader.get_a_in_range, # f(x+a) validation (range check required)
    ValueReader.get_a_in_range, # f(x)+a validation (range check required)
    ValueReader.get_a # a*f(x) validation (no range check required)
]

class MathDisplayer(object):
    """docstring for FunctionTransformations().MathDisplayer"""
    def __init__(self):
        super(MathDisplayer, self).__init__()
        self.button = [i for i in range(9)] # creates nine buttons, one for each function
        # creating the main window
        self.MainWindow = Tk()
        self.MainWindow.title('Transformations of Graphs of Functions')
        i = 0
        for i in range(9):
            # creating the widget Button for Linear Functions
            self.button[i]= Button(
                self.MainWindow,
                text=label[i],
                height=button_height,
                command=lambda i=i: FunctionTransformations().display(
                    self,
                    MathFunctionList[i],
                    1,
                    message[i],
                    init_build
                ),
                bg='white').grid(
                    row=i,
                    column=0,
                    columnspan=button_columnspan,
                    ipadx=20,
                    sticky=W+E+N+S
                )
        # creating the main Canvas widget
        self.canvas1 = CustomisedCanvas(
            window=self.MainWindow,
            canvas_height=canvas1_height,
            canvas_width=canvas1_width,
            bg_color=canvas1_bg_color,
            bd_width=canvas1_bd_width,
            canvas_relief=canvas1_canvas_relief,
            row=canvas1_row,
            column=canvas1_column,
            columnspan=canvas1_columnspan,
            rowspan=canvas1_rowspan,
            number=1
        )
        self.a_entry = []
        for i in range(9,13):
            # entry fields to read the value of "a" entred by the user
            self.a_entry.append(
                Entry(
                    self.MainWindow,
                    bd=4,
                    relief=RIDGE
                )
            )
            self.a_entry[i-9].grid(row=i, column=2, columnspan=entry_columnspan)
        self.trans = []
        for i in range(4):
            self.trans.append(
                Button(
                    self.MainWindow,
                    text=title_trans[i],
                    command=lambda i=i: FunctionTransformations().display(
                        self,
                        displayed_function['now'],
                        get[i](self.a_entry[i]),
                        message_canvas_2[i],
                        i+1
                    )
                ).grid(row=9+i, sticky=W, columnspan=trans_columnspan)
            )
        self.check_box = []
        # creating check box for negative x co-ordinates
        self.check_box.append(
            Checkbutton(
                self.MainWindow,
                text="f(-x)    ",
                state='active',
                command=lambda: FunctionTransformations().display(
                self,
                displayed_function['now'],
                -1,
                "This transformation multiplies x by the -1"+
                ' then applies    function '+displayed_function['name']+' therefore we have '+
                displayed_function['name']+'(-x)',
                #dynamic description allows displayed function to be mentioned in description box
                1
                )
            )
        )
        # creating check box for negative x co-ordinates
        self.check_box.append(
            Checkbutton(
                self.MainWindow,
                text="-f(x)      ",
                state='active',
                command=lambda: FunctionTransformations().display(
                self,
                displayed_function['now'],
                -1,
                "This transformation multiplies x by the -1"+
                ' then applies    function '+displayed_function['name']+' therefore we have -'+
                displayed_function['name']+'(x)',
                #dynamic description allows displayed function to be mentioned in description box
                4
                )
            )
        )
        # creating the inverse checkbox (1/f(x))
        self.check_box.append(
            Checkbutton(
                self.MainWindow,
                text="1/f(x)      ",
                state='active',
                command=lambda: FunctionTransformations().display(
                self,
                displayed_function['now'],
                -1,
                "This transformation inverts the function, "+
                ' therefore we have 1/'+displayed_function['name']+'(x).',
                #dynamic description allows displayed function to be mentioned in description box
                5
                )
            )
        )
        for i in range(3):
            self.check_box[i].grid(row=9+i, column=4, columnspan=trans_columnspan, sticky=W)
        # creating the second canvas (description box)
        self.canvas2 = CustomisedCanvas(
            window=self.MainWindow,
            canvas_height=canvas2_height,
            canvas_width=canvas2_width,
            bg_color=canvas1_bg_color,
            bd_width=canvas1_bd_width,
            canvas_relief=canvas1_canvas_relief,
            row=canvas2_row,
            column=5,
            columnspan=canvas2_columnspan,
            rowspan=canvas2_rowspan,
            number=2
        )
        # creating the reset print and option buttons in the bottom right hand corner of program
        self.button_reset, self.button_print, self.button_options = self.side_buttons()
        # main loop method keeps the project running
        self.MainWindow.mainloop()


    def print_canvas(self):
        """
        print the items of the main canvas on a PostScript file
        """
        name = filedialog.asksaveasfilename()
        if name != '' :
            self.canvas1.canvas.postscript(file=name+'.ps', colormode='color')



    def delete_axis_x(self):
        """
        deletes the x axis and the numbers on it from the canvas
        """
        if axe_x != []:
            for i in axe_x:
                self.canvas1.canvas.delete(i)
            axe_x[:] = []


    def delete_axis_y(self):
        """
        deletes the y axis and the numbers on it from the canvas
        """
        if axe_y != []:
            for i in axe_y:
                self.canvas1.canvas.delete(i)
            axe_y[:] = []


    def delete_grid(self):
        """
        deletes the diplayed function on the canvas
        """
        for i in lines:
            self.canvas1.canvas.delete(i)
        lines[:] = []


    def side_buttons(self):
        """
        create the Reset, Print and Options
        button in the bottom right hand side of the window
        """
        # side buttons properties
        side_button_height = 1
        # Creating reset button and placing it in row 10 column 11
        button_reset = Button(
            self.MainWindow,
            text='Reset',
            height=side_button_height,
            command=lambda: CustomisedCanvas.reset(self),
            bg='white'
        ).grid(row=10, column=15, sticky=W+E+N+S)
        # Creating Print button and placing it one row under the reset button
        button_print = Button(
            self.MainWindow,
            text='Print',
            height=side_button_height,
            command=lambda: self.print_canvas(),
            bg='white'
        ).grid(row=11, column=15, sticky=W+E+N+S)
        # Creating Options button and placing it one row under the reset button
        button_options = Button(
            self.MainWindow,
            text='Options',
            height=side_button_height,
            command=lambda: OptionsWindow(self),
            bg='white'
        ).grid(row=12, column=15, sticky=W+E+N+S)
        return button_reset, button_print, button_options
