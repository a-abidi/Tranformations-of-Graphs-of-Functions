import os
import webbrowser
import subprocess
import math

from tkinter import *
from tkinter import filedialog

from config import *


class OptionsWindow(object):
    """
    displays the options window that appears after clicking the options button
    """
    def __init__(self, arg):
        super(OptionsWindow, self).__init__()
        self.canvas1 = arg
        if options_menu['is_active'] == 0:
            options_menu['is_active'] = 1
            root = Tk()
            root.title('Options')
            root.configure(background='white')
            r = 0
            Label(
                root,
                text='Graph Settings :',
                bg='white'
            ).grid(row=r, column=0, sticky=W)
            r += 1
            x_axis = Checkbutton(
                root,
                text="show-x axis label",
                state='active',
                bg='white',
                command=lambda: self.canvas1.delete_axis_x()
            )
            x_axis.grid(row=r, padx=50, pady=10, sticky=N)
            x_axis.select()
            r += 1
            s = IntVar()
            y_axis = Checkbutton(
                root,
                text="show-y axis label",
                bg='white',
                command=lambda: self.canvas1.delete_axis_y()
            )
            y_axis.grid(row=r, padx=50, pady=10, sticky=W)
            y_axis.select()
            r += 1
            grid = Checkbutton(
                root,
                text="show grid lines   ",
                bg='white',
                command=lambda: self.canvas1.delete_grid()
            )
            grid.grid(row=r, padx=50, pady=10, sticky=W)
            grid.select()
            r += 1
            Label(
                root,
                text="_____________________________________",
                bg='white'
            ).grid(row=r)
            r += 1
            Label(
                root,
                text="Printer :",
                bg='white'
            ).grid(row=r, sticky=W)
            r += 1
            button = Button(
                root,
                text="      Print  Screen     ",
                command=lambda: self.canvas1.print_canvas(),
                bg='white'
            ).grid(row=r, padx=20)
            r += 1
            Label(
                root,
                text="_____________________________________",
                bg='white'
            ).grid(row=r)
            r += 1
            Label(
                root,
                text="Help :",
                bg='white'
            ).grid(row=r, sticky=W)
            r += 1
            button = Button(
                root,
                text="      User Manual       ",
                command=lambda: webbrowser.open_new(
                    os.path.abspath('.')+os.path.sep+'a.pdf'
                ),
                bg='white'
            ).grid(row=r)
            r += 1
            button = Button(
                root,
                text="  Contact Developer  ",
                command=self.show_dev_contact,
                bg='white'
            ).grid(row=r)
            root.wait_window()
            options_menu['is_active'] = 0
        else:
            pass

    def show_dev_contact(self):
        """
        displays the window that displays the developer email address
        """
        window = Tk()
        window.title("Developer's Contact")
        window.configure(background='white')
        Label(
                window,
                text='Developer e-mail :',
                bg='white'
            ).grid(row=0, column=0, padx=10, pady=10, sticky=W+E+N+S)
        Label(
                window,
                text='email@address.com',
                bg='white'
            ).grid(row=0, column=1, padx=10, pady=10, sticky=W+E+N+S)


class CustomisedCanvas(object):
    """Creates a new Canvas widget"""
    def __init__(self, window,canvas_height,canvas_width,bg_color,bd_width,canvas_relief,row,column,columnspan,rowspan,number):
        super(CustomisedCanvas, self).__init__()
        self.canvas = Canvas(
            window,
            height=canvas_height,
            width=canvas_width,
            bg=bg_color,
            bd=bd_width,
            relief=canvas_relief
        )
        if number == 1:
            padding=0
        else:
            padding=10
        self.canvas.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            rowspan=rowspan,
            padx=padding
        )
        if number == 1 and options_menu['is_active'] == 0:
            self.draw_axis_y()
            self.draw_axis_x()

    def reset(can):
        """
        reset the screen to its initial stateb y deleting
        all the drawn lines and recreating the x and the y co-ordinate axes
        """
        if options_menu['is_active'] == 0:
            for i in lines:
                can.canvas1.canvas.delete(i)
            for i in lines2:
                can.canvas2.canvas.delete(i)
            lines2[:] = []
            lines[:] = []
            can.canvas1.draw_axis_y()
            can.canvas1.draw_axis_x()

    def draw_axis_x(self):
        """ draw the x axis """
        for i in axe_x:
            self.canvas.delete(i)
        axe_x[:] = []
        axe_x.append(
            self.canvas.create_line(
                0,
                canvas1_height/2,
                canvas1_width,
                canvas1_height/2
            )
        )
        for i in range(int(-canvas1_width/2), int(canvas1_width/2)):
            axe_x.append(
                self.canvas.create_line(
                    canvas1_width/2 + 25*i,
                    canvas1_height/2 - 2,
                    canvas1_width/2 + 25*i,
                    canvas1_height/2 + 2
                )
            )
            if i != 0:
                axe_x.append(
                    self.canvas.create_text(
                        canvas1_width/2 + 25*i-5,
                        canvas1_height/2 - 2,
                        anchor=SW,
                        text=str(i)
                    )
                )

    def del_XAxis(self): 
        for i in axe_x:
            self.canvas.delete(i)
            del_Axis() # Recursion to delete all x components

    def draw_axis_y(self):
        """ draw the y axis """
        for i in axe_y:
            self.canvas.delete(i)
        axe_y[:] = []
        for i in range(int(-canvas1_height/2), int(canvas1_height/2)):
            axe_y.append(
                self.canvas.create_text(
                    canvas1_width/2 + 4,
                    canvas1_height/2 + 25*i,
                    anchor=SW,
                    text=str(-i)
                )
            )
            axe_y.append(
                self.canvas.create_line(
                    canvas1_width/2 + 2,
                    canvas1_height/2 + 25*i,
                    canvas1_width/2 - 2,
                    canvas1_height/2 + 25*i
                )
            )
            axe_y.append(
                self.canvas.create_line(
                    canvas1_width/2,
                    0,
                    canvas1_width/2,
                    canvas1_height
                )
            )

    def del_YAxis(self): 
        for i in axe_y:
            self.canvas.delete(i)
            del_Axis() # Recursion to delete all y components
