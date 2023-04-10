import tkinter as tk
import random
import string
import pyperclip

# Declare entry as a global variable
global length_entry, sign_entry, uppercase_entry, number_entry, lowercase_entry, l
length_entry = None

# Creating a list with numbers
number_list = [str(i) for i in range(10)]
# Creating a list with signs
sign_list = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_',
             '`','{','|','}','~']
# Creating a list with uppercase letters
uppercase_list = [chr(i+65) for i in range(26)]
# Creating a list with lowercase letters
lowercase_list  = [chr(i+97) for i in range(26)]

# Define a function to handle button click
def button_click(length):
    global length_entry, l
    l = []
    l.append(length_entry.get())
    l.append(sign_entry.get())
    l.append(uppercase_entry.get())
    l.append(number_entry.get())
    l.append(lowercase_entry.get())

def copy_to_clipboard():
    global password_str
    pyperclip.copy(password_str)


def input_data(window, t, x_co, y_co):
    global length_entry, sign_entry, uppercase_entry, number_entry, lowercase_entry
    label1 = tk.Label(window, text=t, bg="yellow", font=20)
    label1.place(x=x_co, y=y_co)

    # Create an Entry widget and make it a global variable
    if t == "The length of password: ":
        length_entry = tk.Entry(window)
        length_entry.place(x=x_co, y=y_co+30)
    elif t == "how many signs in pass:":
        sign_entry = tk.Entry(window)
        sign_entry.place(x=x_co, y=y_co+30)
    elif t == "how many uppercase letters in pass:":
        uppercase_entry = tk.Entry(window)
        uppercase_entry.place(x=x_co, y=y_co+30)
    elif t == "how many numbers in pass:":
        number_entry = tk.Entry(window)
        number_entry.place(x=x_co, y=y_co+30)
    elif t == "how many lowercase letters in pass:":
        lowercase_entry = tk.Entry(window)
        lowercase_entry.place(x=x_co, y=y_co+30)

    # Create a button to trigger the function
    button = tk.Button(window, text="Submit", command=lambda: button_click(length_entry.get()))
    button.place(x=x_co+130, y=y_co+30)


def create_window():
    global password_str, window
    # Creating the window
    window = tk.Tk()

    # Setting the window title
    window.title("password generator")
    # Setting the window size
    window.geometry("500x600")
    # Adding a lable to the window
    label = tk.Label(window, text="PASSWORD GENERATOR", bg="blue", font=25)
    label.pack()

    input_data(window, "The length of password: ", 50, 50)
    input_data(window, "how many signs in pass:", 50, 110)
    input_data(window, "how many uppercase letters in pass:", 50, 170)
    input_data(window, "how many numbers in pass:", 50, 230)
    input_data(window, "how many lowercase letters in pass:", 50, 290)

    # Create a button to trigger the function
    generate_button = tk.Button(window, text="Generate", command=lambda: generate_password())
    generate_button.place(x=50, y=350)

    # Starting the main event loop
    window.mainloop()

def generate_password():
    global password_str, window
    passwd = []
    for i in range(int(l[1])):
        letter = random.choice(sign_list)
        passwd.append(letter)
    for i in range(int(l[2])):
        letter = random.choice(uppercase_list)
        passwd.append(letter)
    for i in range(int(l[3])):
        letter = random.choice(number_list)
        passwd.append(letter)
    for i in range(int(l[4])):
        letter = random.choice(lowercase_list)
        passwd.append(letter)

    random.shuffle(passwd)
    password_str = "".join(passwd)

    # Display the password in the Tkinter window
    label_above_pass = tk.Label(window, text="Your password is: ", font=25)
    label_above_pass.place(x=50, y=350)
    password_label = tk.Label(window, text=password_str, font=60, bg="green")
    password_label.place(x=150, y=400)
    label_under_pass = tk.Label(window, text="Your password has been copied in your clipboard", font=10)
    label_under_pass.place(x=50, y=450)
    copy_to_clipboard()


create_window()