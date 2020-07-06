import math

from tkinter import *
from tkinter import messagebox

from util import OptionsWindow, CustomisedCanvas
from config import *


class MathFunction(object):
    """docstring for MathFunction"""
    def __init__(self):
        super(MathFunction, self).__init__()
        
    def sine(x):
        """
        returns the co-ordinates of the points that will be displayed
        on the canvas when the function called is "sine"
        """
        displayed_function['name'] = 'sine'
        return(center - (math.sin(x * x_factor) * y_amplitude))


    def cosine(x):
        """
        returns the co-ordinates of the points that will be displayed
        on the canvas when the function called is "cosine"
        """
        displayed_function['name'] = 'cosine'
        return(center - (math.cos(x * x_factor) * y_amplitude))


    def linear(x):
        """
        returns the co-ordinates of the points that will be displayed
        on the canvas when the function called is "linear"
        """
        displayed_function['name'] = 'linear'
        return(center-x)


    def modulus(x):
        """
        returns the co-ordinates of the points that will be displayed
        on the canvas when the function called is "moduls"
        """
        displayed_function['name'] = 'modulus'
        if x < 0:
            return(center + int(x))
        else:
            return(center - int(x))


    def quadratic(x):
        """
        returns the co-ordinates of the points that will be displayed
        on the canvas when the function called is "quadratic"
        """
        displayed_function['name'] = 'quadratic'
        return(center - ((x*x*x_factor*x_factor)*y_amplitude))


    def expo(x):
        """
        returns the co-ordinates of the points that will be displayed
        on the canvas when the function called is "exponential"
        """
        displayed_function['name'] = 'exponential'
        return(center - (math.exp(x * x_factor) * y_amplitude))


    def inv(x):
        """
        returns the co-ordinates of the points that will be displayed
        on the canvas when the function called is "inverse"
        """
        displayed_function['name'] = 'inverse'
        if x != 0:
            return(center - (y_amplitude/(x*x_factor)))
        else:
            return(0)


    def tang(x):
        """
        returns the co-ordinates of the points that will be displayed
        on the canvas when the function called is "tangent"
        """
        displayed_function['name'] = 'tangent'
        return(center - (math.tan(x * x_factor) * y_amplitude))


    def cubic(x):
        """
        returns the co-ordinates of the points that will be displayed
        on the canvas when the function called is "cubic"
        """
        return(center - (x*x*x*x_factor*x_factor*x_factor*y_amplitude))


class ValueReader(object):
    """docstring for ValueReader"""
    def __init__(self):
        super(ValueReader, self).__init__()
        
    def get_a_in_range(a):
        """
        returns the value of the parameter "a" and parse it to a float if this
        parameter was not entred or was not a type that can be parsed to a float
        it will show a warning and return "1" as the value of "a"
        """
        try:
            value = (float(a.get()))
            if value in range(-20,21):
                return value
            messagebox.showerror(
                "Error: Input out of Range!",
                'Please inter a valid integer or float value for "a"' +
                'which is in the range of -20 to 20.'
            )
            return 1
        except:
            messagebox.showerror(
                "Error: Invalid Input!",
                'Please enter a valid integer/float for the value of "a". ' +
                'The value of "a" shall be considered as 1 in this instance'
            )
            return 1
    def get_a(a):
        """
        returns the value of the parameter "a" and parse it to a float if this
        parameter was not entred or was not a type that can be parsed to a float
        it will show a warning and return "1" as the value of "a"
        """
        try:
            return float(a.get())
        except:
            messagebox.showerror(
                "Unvalid a format",
                'Please inter a valid Integer or Float "a"' +
                'the value of "a" wil be considered 1 this time'
            )
            return 1


    def get_a_with_no_error(a):
        """
        returns the value of the parameter "a" and parse it to a float if this
        parameter was not entered or was not a type that can be parsed to a float
        it will show a warning and return "1" as the value of "a"
        """
        try:
            return(float(a.get()))
        except:
            return(float(1))


class FunctionTransformations(object):
    """docstring for FunctionTransformations"""
    def __init__(self):
        super(FunctionTransformations, self).__init__()

        
    def transform_f_a_x(self, center, func_2_display, y_amplitude, a, x_history):
        """
        returns f(a*x), parameters taken: the function to display, the value of a and x and the canvas paramters' x_factor y_amplitude
        """
        list_x = [x*a for x in x_history]
        list_y = [func_2_display(x) for x in list_x]
        return list_x, list_y

    def transform_1_f_x(self, center, func_2_display, y_amplitude, a, y_history, old_x):
        y_history = [
            center + 
            y_amplitude*y_amplitude/((y-center) or 0.001)
            for y in y_history
        ]
        return(y_history)

    def transform_f_x_plus_a(self, center, func_2_display, y_amplitude, a, x_history):
        """
        returns f(x+a), parameters: the function to display,
        the value of a and x and the canvas parameters' x_factor y_amplitude
        """
        factor = a * y_amplitude

        list_x = [x + factor for x in x_history]
        list_y = [func_2_display(x) for x in list_x]
        return list_x ,list_y


    def transform_a_f_x(self, center, func_2_display, y_amplitude, a, y_history, old_x):
        """
        returns a*f(x), parameters: the function to display, the value of a and x and the
        canvas paramters' x_factor y_amplitude
        """
        y_history = [center-a*(center -y) for y in y_history]
        return(y_history)


    def transform_a_plus_f_x(self, center, func_2_display, y_amplitude, a, y_history, old_x):
        """
        returns a+f(x) it takes as parameters the function to display,
        the value of a and x and the canvas paramters' x_factor y_amplitude
        """
        y_history = [y - a*y_amplitude for y in y_history]
        return(y_history)


    def store_old_coordinates(self, func_2_display):
        """
        stores latest old x and y co-ordinates to decide what to do later
        """
        x_history[:] = []
        y_history = []
        displayed_function['now'] = func_2_display
        for x in range(-int(canvas1_width/2), int(canvas1_width//2)):
            # x coordinates
            x_history.append(x)
            # y coordinates
            y_history.append(func_2_display(x))
        return x_history, y_history



    def display(self, canvases, func_2_display, a, text2, choice):
        """
        displays the chosen function 'func_2_display' and applies the effect of the input "a"
        which is 'a_effect'. Default value of functions is f(x*1).
        parameters taken: the value of 'a' and 'x'
        """
        if options_menu['is_active'] == 0:
            CustomisedCanvas.reset(canvases)
            center = canvas1_height//2

            if len(text2) > 60:
                text21 = text2[:60]
                text22 = text2[60:120]
                if len(text22)>10:
                    text = canvases.canvas2.canvas.create_text(10, 20, anchor=SW, text=text21)
                    lines2.append(text)
                    text = canvases.canvas2.canvas.create_text(10, 35, anchor=SW, text=text22)
                else :
                    text = canvases.canvas2.canvas.create_text(10, 20, anchor=SW, text=text2)
            else :
                text = canvases.canvas2.canvas.create_text(10, 20, anchor=SW, text=text2)
            lines2.append(text)
            y_history = [xy1[2*i+1] for i in range(len(xy1)//2)]
            x_history = [xy1[2*i] for i in range(len(xy1)//2)]
            xy1[:] = []
            if choice == 0:
                x_history, y_history = self.store_old_coordinates(func_2_display)
                old_x[:] = []
            elif displayed_function['now'] != '' :
                if choice == 1:
                    x_history ,y_history = self.transform_f_a_x(center, displayed_function['now'], y_amplitude, a, old_x)
                    old_x[:] = []
                elif choice == 2:
                    x_history, y_history = self.transform_f_x_plus_a(center, displayed_function['now'], y_amplitude, a, old_x)
                    old_x[:] = []
                elif choice == 3:
                    y_history = self.transform_a_plus_f_x(center, displayed_function['now'], y_amplitude, a, y_history, old_x)
                elif choice == 4:
                    y_history = self.transform_a_f_x(center, displayed_function['now'], y_amplitude, a, y_history, old_x)
                elif choice == 5:
                    y_history = self.transform_1_f_x(center, displayed_function['now'], y_amplitude, a, y_history, old_x)
            else:
                return None
            for i in range(len(y_history)):
                xy1.append(i)
                xy1.append(y_history[i])
                old_x.append(x_history[i])
            if len(xy1)!=0:
                line = canvases.canvas1.canvas.create_line(xy1, activefill='red', fill='blue')
                lines.append(line)
