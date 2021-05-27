import tkinter

# Main
root = tkinter.Tk()

# Define button function
def click1():
    root['background']="black"
    print(root['bg'])

# Create Label
label = tkinter.Label(root, text="Hello, Tkinter!")
label.pack()

# Create button
button1 = tkinter.Button(root,
                         text="Button1",
                         bg = "green",
                         command=click1)

button2 = tkinter.Button(root, text="Button2")

button1.pack(side=tkinter.LEFT)
button2.pack(side=tkinter.RIGHT)

root.mainloop()
