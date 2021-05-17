# Creating a temperature converter
from tkinter import *
from tkinter import messagebox

root = Tk()
# Creating a title
root.title("Temperature Converter")
# Setting the window size
root.geometry("700x500")
# Setting a background color
root.config(bg="#fff642")


# Creating & positioning the fahrenheit frame with a background color
frame_f = Frame(root, width=200, height=200, borderwidth=1, relief="ridge", bg="#fff642")
frame_f.place(relx=0.1, rely=0.1)

# Creating & positioning the Fahrenheit label & entry point with a background color
label_f = Label(frame_f, text="Fahrenheit to Celsius", bg="#fff642")
label_f.place(relx=0, rely=0)
entry_f = Entry(frame_f)
entry_f.place(relx=0.1, rely=0.6)

# Creating & positioning the celsius frame with a background color
frame_c = Frame(root, width=200, height=200, borderwidth=1, relief="ridge", bg="#fff642")
frame_c.place(relx=0.5, rely=0.1)

# Creating & positioning the Celsius label & entry point with a background color
label_c = Label(frame_c, text="Celsius to Fahrenheit", bg="#fff642")
label_c.place(relx=0, rely=0)
entry_c = Entry(frame_c)
entry_c.place(relx=0.1, rely=0.6)


# Making the c to f activate functional
def activate_f_to_c():
    entry_f.config(state="normal")
    entry_c.config(state="normal")
    entry_c.delete(0, END)
    entry_c.config(state="readonly")


# Making the f to c activate functional
def activate_c_to_f():
    entry_c.config(state="normal")
    entry_f.config(state="normal")
    entry_f.delete(0, END)
    entry_f.config(state="readonly")


# Creating & positioning an activate button for frame f
activate_f_to_c = Button(root, text="Activate - Fahrenheit to Celsius", command=activate_f_to_c)
activate_f_to_c.place(relx=0.1, rely=0.5)

# Creating & positioning an activate button for frame c
activate_c_to_f = Button(root, text="Activate - Celsius to Fahrenheit", command=activate_c_to_f)
activate_c_to_f.place(relx=0.5, rely=0.5)


# Defining the function used to convert the temperature
def convert_temperature():
    try:
        # Fahrenheit to Celsius
        if entry_f["state"] == "normal":
            temp_f = float(entry_f.get())
            result_c = round((temp_f - 32) * (5/9), 1)
            calculate_label.config(text=str(result_c))

        # Celsius to Fahrenheit
        elif entry_c["state"] == "normal":
            temp_c = float(entry_c.get())
            result_f = round((temp_c * (9/5)) + 32, 1)
            calculate_label.config(text=str(result_f))

    # If invalid entry is given raise value error
    except ValueError:
        messagebox.showinfo(message="Entry is invalid")


# Defining the function that makes the "Clear" button operational
def delete():
    entry_f.delete(0, END)
    entry_f.focus()
    entry_c.delete(0, END)
    entry_c.focus()
    entry_a.config(state="normal")
    entry_a.delete(0, END)
    entry_a.config(state="readonly")


# Creating & positioning an answer frame and it's entry point
frame_a = Frame(root, height=100, width=100, borderwidth=1, relief="ridge", bg="#fff642")
frame_a.place(relx=1, rely=1)
entry_a = Entry(root, bg="white", state="readonly")
entry_a.place(relx=1, rely=1)

# Creating, labeling & positioning the temperature converter button
calculate_label = Label(root, width=25, height=5, bg="white")
calculate_label.place(relx=0.4, rely=0.7)
calculate = Button(root, text="Calculate Conversion", command=convert_temperature)
calculate.place(relx=0.1, rely=0.7)

# Creating & positioning the clear button
button_clear = Button(root, text="Clear", command=delete)
button_clear.place(relx=0.8, rely=0.7)

# Creating & positioning the exit button
button_exit = Button(root, text="Exit", command="exit")
button_exit.place(relx=0.8, rely=0.8)

root.mainloop()