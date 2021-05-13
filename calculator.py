from numpy import empty, float_, floating
from numpy.core.arrayprint import FloatingFormat
from tkinter import *
from tkinter import messagebox

# Variável global da variável resultado de alguma operação
result = float

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title('Python Calculator')
root.geometry("382x%d+%d+0" % (height, (width/2) - 200))
root.resizable(width=False, height=False)

# CLEAR CALCULATOR SCREEN


def clear_screen():
    global result
    lbl_result.config(text='')
    result = None

# COMPUTE THE VALUE OF THE CLICKED BUTTON


def number_click(button):
    global result
    if (lbl_result.cget('text')) == None:
        lbl_result.config(text=button)
    elif (lbl_result.cget('text')) == result:
        lbl_result.config(text='')
        lbl_result.config(text=button)
    else:
        current_text = str(lbl_result.cget('text'))
        lbl_result.config(text=current_text + str(button))


# CALC FUNCTIONS


def plus_button():
    if (lbl_result.cget('text')) == None:
        lbl_result.config(text='+')
    else:
        current_text = str(lbl_result.cget('text'))
        lbl_result.config(text=current_text + '+')


def less_button():
    if (lbl_result.cget('text')) == None:
        lbl_result.config(text='-')
    else:
        current_text = str(lbl_result.cget('text'))
        lbl_result.config(text=current_text + '-')


def multiply_button():
    if (lbl_result.cget('text')) == None:
        lbl_result.config(text='*')
    else:
        current_text = str(lbl_result.cget('text'))
        lbl_result.config(text=current_text + '*')


def divide_button():
    if (lbl_result.cget('text')) == None:
        lbl_result.config(text='/')
    else:
        current_text = str(lbl_result.cget('text'))
        lbl_result.config(text=current_text + '/')


def equal_button():
    global result
    result = str(lbl_result.cget('text'))
    lbl_result.config(text='')
    # Função eval tranforma a string em uma equação matemática!!
    result = eval(result)
    lbl_result.config(text=result)


# DEFINE THE RESULT SCREEN
lbl_result = Label(root, width=45, height=5, border=5)
lbl_result.grid(row=0, column=1, columnspan=4)

# DEFINE THE BUTTONS
btn_1 = Button(root, text='1', padx=40, pady=50,
               bg='lightblue', command=lambda: number_click(1))
btn_2 = Button(root, text='2', padx=40, pady=50,
               bg='lightblue', command=lambda: number_click(2))
btn_3 = Button(root, text='3', padx=40, pady=50,
               bg='lightblue', command=lambda: number_click(3))
btn_4 = Button(root, text='4', padx=40, pady=50,
               bg='lightblue', command=lambda: number_click(4))
btn_5 = Button(root, text='5', padx=40, pady=50,
               bg='lightblue', command=lambda: number_click(5))
btn_6 = Button(root, text='6', padx=40, pady=50,
               bg='lightblue', command=lambda: number_click(6))
btn_7 = Button(root, text='7', padx=40, pady=50,
               bg='lightblue', command=lambda: number_click(7))
btn_8 = Button(root, text='8', padx=40, pady=50,
               bg='lightblue', command=lambda: number_click(8))
btn_9 = Button(root, text='9', padx=40, pady=50,
               bg='lightblue', command=lambda: number_click(9))
btn_0 = Button(root, text='0', padx=88, pady=45,
               bg='lightblue', command=lambda: number_click(0))
btn_dot = Button(root, text=',', padx=41, pady=45,
                 bg='lightblue', command=lambda: number_click('.'))

btn_clear = Button(root, text='C', padx=134, pady=50,
                   bg='lightyellow', command=clear_screen)
btn_plus = Button(root, text='+', padx=42, pady=50,
                  bg='lightpink', command=plus_button)
btn_less = Button(root, text='-', padx=42, pady=50,
                  bg='lightpink', command=less_button)
btn_multiply = Button(root, text='x', padx=42, pady=50,
                      bg='lightpink', command=multiply_button)
btn_divide = Button(root, text='/', padx=42, pady=50,
                    bg='lightpink', command=divide_button)
btn_equal = Button(root, text='=', padx=42, pady=45,
                   bg='lightpink', command=equal_button)

# PUT THE BUTTONS ON SCREEN
btn_0.grid(row=5, column=1, columnspan=2)
btn_1.grid(row=4, column=1)
btn_2.grid(row=4, column=2)
btn_3.grid(row=4, column=3)
btn_4.grid(row=3, column=1)
btn_5.grid(row=3, column=2)
btn_6.grid(row=3, column=3)
btn_7.grid(row=2, column=1)
btn_8.grid(row=2, column=2)
btn_9.grid(row=2, column=3)
btn_dot.grid(row=5, column=3)
btn_clear.grid(row=1, column=1, columnspan=3)
btn_plus.grid(row=1, column=4)
btn_less.grid(row=2, column=4)
btn_multiply.grid(row=3, column=4)
btn_divide.grid(row=4, column=4)
btn_equal.grid(row=5, column=4)


root.mainloop()
