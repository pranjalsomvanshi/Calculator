from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Calculator using TKinter")
window.configure(background='black')
label1 = Label(window, text="Enter First Number", bg='black',fg='blue').grid(row=0, column=0, padx=10, pady=10)
label2 = Label(window, text="Enter Second Number", bg='black',fg='blue').grid(row=1, column=0, padx=10, pady=10)
label3 = Label(window,text='Result',bg='black',fg='blue')
label3.grid(row=2, column=0, padx=10, pady=10,sticky='W')
n1=StringVar()
n2=StringVar()
n1_entry=Entry(window,bg='grey',fg='white',textvariable=n1).grid(row=0, column=1, padx=10, pady=10)
n2_entry=Entry(window,bg='grey',fg='white',textvariable=n2).grid(row=1, column=1, padx=10, pady=10)
def Input():
    first = n1.get()
    second = n2.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(n1.get()) == 0) or (len(n2.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
def addition():
    first, second = Input()
    result = first + second
    label3.config(text="Result : " +
                             str(result))

def subtraction():
    first, second = Input()
    result = first - second
    label3.config(text="Result : " +
                             str(result))

def multiplication():
    first, second = Input()
    result = first * second
    label3.config(text="Result : " +
                             str(result))

def division():
    first, second = Input()

    if second == 0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result = first / second
        result = round(result, 2)
        label3.config(text="Result : " +
                                 str(result))
addition_button = Button(window, text="+",
                            command=lambda : addition()).grid(row=3, column=0, padx=10, pady=10)
subtraction_button = Button(window, text="-",
                            command=lambda : subtraction()).grid(row=3, column=1, padx=10, pady=10)
multiplication_button = Button(window, text="*",
                            command=lambda : multiplication()).grid(row=4, column=0, padx=10, pady=10)
division_button = Button(window, text="/",
                            command=lambda : division()).grid(row=4, column=1, padx=10, pady=10)

window.mainloop()