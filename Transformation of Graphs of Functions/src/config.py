from tkinter import RIDGE
#'RIDGE' is a module used for defining the style of buttons

# defining the function button's properties
button_height = 2
button_columnspan = 2

# Display options menu. Makes options menu 'active' when clicked
options_menu = {'is_active' : 0}

# Dictionary which allows program to display each function with its name
displayed_function = {'now': '','name':''}

lines = []
lines2	 = []
axe_x = []
axe_y = []
x_history = []
y_history = []

#Canvas1/Graph box properties
canvas1_width = 780
canvas1_height = 380
canvas1_bg_color = 'white'
canvas1_bd_width = 5
canvas1_canvas_relief = RIDGE
canvas1_row = 0
canvas1_column = 2
canvas1_columnspan = 17
canvas1_rowspan = 9

#Canvas2/Description box properties
canvas2_height = 100
canvas2_width = 470
canvas2_row = 9
canvas2_column = 3
canvas2_columnspan = 9
canvas2_rowspan = 9
entry_columnspan = 2
trans_columnspan = 2

center = 190
x_axis = []
# width stretch
x_factor = 0.04
# height stretch
y_amplitude = 25

old_x = []
xy1 = []
x_history = []
y_history = []
init_build = 0

#List of labels of functions of graph
label = [
    "Linear",
    'Quadratic',
    'Cubic',
    'Sine',
    'Cosine',
    'Tangent',
    'Exponential',
    'Inverse',
    'Modulus'
]

#List of descriptions output when button is selected, same order as functions in list 'label' to be called
message = [
    'Linear functions are those whose graph is a straight line.  A linear function has the following form y = f(x) = a + bx.',
    'Quadratic function has a 'U' shape and is in the form f(x) = ax² + bx + c where a, b, and c are integers not equal to 0).',
    'Cubic function has the form  f(x) = x³.',
    'Sine is a trigonometric function. Function selected is sin(x).',
    'Cosine is a trigonometric function. Function selected is cos(x).',
    'Tangent is a trigonometric function. Function selected is tan(x).',
    'Exponential function is a function of the form eˣ.',
    'An inverse function is a function in the form f(x) = 1/kx, where k is a constant.',
    'The modulus function, y =|x|, takes absolute value of the expression inside the modulus sign.'
]

#Labels of transformation on buttons 
title_trans = [
    'f(a*x) enter value of a :',
    'f(x+a) enter value of a :',
    'f(x)+a enter value of a :',
    'a*f(x) enter value of a :'
]

#Message output when transformation is applied, in same order as list 'title_trans'  
message_canvas_2 = [
    'This transformation multiplies x by the a then applies    function therefore we have f(a*x)',
    'This transformation adds the value to x and apply the   therefore we have f(x+a)',
    'This transformation  multiplies the value of a  by the  function  therefore we have a * f(x)',
    'This transformation  multiplies the value of a by the  function  therefore we have a + f(x)'
]
