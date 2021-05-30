from tkinter import *

# Main
root = Tk()
global done
done = 0

# Function when number was clicked.
def number_click(number):
    global done
    if done:
        entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))
    done = 0

def symbol_click(symbol):
    global done
    done = 0
    current = entry.get()
    entry.delete(0, END)
    try:
        if current[-1].isnumeric():
            entry.insert(0, str(current) + str(symbol))
        else:
            current[-1] = str(symbol)
            entry.insert(0, str(current))
    except IndexError as err:
        entry.insert(0, str(current) + str(symbol))
        

def calculate():
    global done
    try:
        formula = entry.get()
        entry.delete(0, END)
        entry.insert(0, eval(str(formula)))
    except SyntaxError as err:
        err_msg = "ERR: '" + formula + "' is invalid."
        entry.insert(0, err_msg)
    done = 1

def delete():
    global done
    if done:
        entry.delete(0, END)
    else:
        current = entry.get()
        current = current[0:-1]
        entry.delete(0, END)
        entry.insert(0, str(current))
    done = 0

def clear():
    entry.delete(0, END)
    
entry = Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Create number buttons.
num_1 = Button(root, text="1", width=5, height=2, command=lambda: number_click("1"))
num_2 = Button(root, text="2", width=5, height=2, command=lambda: number_click("2"))
num_3 = Button(root, text="3", width=5, height=2, command=lambda: number_click("3"))
num_4 = Button(root, text="4", width=5, height=2, command=lambda: number_click("4"))
num_5 = Button(root, text="5", width=5, height=2, command=lambda: number_click("5"))
num_6 = Button(root, text="6", width=5, height=2, command=lambda: number_click("6"))
num_7 = Button(root, text="7", width=5, height=2, command=lambda: number_click("7"))
num_8 = Button(root, text="8", width=5, height=2, command=lambda: number_click("8"))
num_9 = Button(root, text="9", width=5, height=2, command=lambda: number_click("9"))
num_0 = Button(root, text="0", width=5, height=2, command=lambda: number_click("0"))

# Place number buttons.
num_1.grid(row=4,column=0)
num_2.grid(row=4,column=1)
num_3.grid(row=4,column=2)
num_4.grid(row=3,column=0)
num_5.grid(row=3,column=1)
num_6.grid(row=3,column=2)
num_7.grid(row=2,column=0)
num_8.grid(row=2,column=1)
num_9.grid(row=2,column=2)
num_0.grid(row=5,column=1)

# Mathematical symbol buttons.
add     = Button(root, text="+", width=5, height=2, command=lambda: symbol_click("+"))
clear   = Button(root, text="c", width=5, height=2, command=clear)
decimal = Button(root, text=".", width=5, height=2, command=lambda: symbol_click("."))
delete  = Button(root, text="del", width=5, height=2, command=delete)
divide  = Button(root, text="/", width=5, height=2, command=lambda: symbol_click("/"))
equal   = Button(root, text="=", width=5, height=5, command=calculate)
minus   = Button(root, text="-", width=5, height=2, command=lambda: symbol_click("-"))
modulus = Button(root, text="%", width=5, height=2, command=lambda: symbol_click("%"))
times   = Button(root, text="*", width=5, height=2, command=lambda: symbol_click("*"))

# Place mathematical symbol buttons.
add.grid(row=3,column=3)
clear.grid(row=1, column=0)
decimal.grid(row=5, column=2)
delete.grid(row=1, column=3)
divide.grid(row=1, column=1)
equal.grid(row=4, column=3, rowspan=2)
minus.grid(row=2, column=3)
modulus.grid(row=5, column=0)
times.grid(row=1, column=2)

root.mainloop()
