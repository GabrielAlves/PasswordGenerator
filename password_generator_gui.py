import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from classes.password_generator import PasswordGenerator

# Creates and define window configuration

win = tk.Tk()
win.title("Password Generator")
win.geometry("350x300")
win.resizable(False, False)

# Defines the size configuration of ScrolledText widget

scrolled_text_width = 30
scrolled_text_height = 3

# Defines font configuration for texts

font_family = "Comic Sans MS"
font_size = 10

# Defines padding configuration

padding_width = 5
padding_height = 5

# Creates frame that wraps every widget

frame = ttk.LabelFrame(win, text = "")
frame.pack(padx = 70)

# Creates title for the window and above it the entry where the password will be written

title_password_generator = ttk.Label(frame, text = "Password Generator", font = (font_family, 16))
title_password_generator.pack(pady = padding_height * 2) 

entry_password = ttk.Entry(frame, width = 30)
entry_password.insert(0, "Your password will be written here")
entry_password.configure(state = "readonly")
entry_password.pack(padx = 5)

# Creates a labelframe wraping the features the generated password must have

labelframe_password_options = ttk.LabelFrame(frame, text = "Options")
labelframe_password_options.pack(pady = padding_height)

# Defines a combobox that defines the number of characters

text_number_characters = ttk.Label(labelframe_password_options, text = "Number of characters", font = (font_family, font_size))
text_number_characters.grid(column = 0, row = 0, sticky = tk.W)

number_characters = tk.IntVar()
combo_box_number_characters = ttk.Combobox(labelframe_password_options, textvariable = number_characters, state = "readonly")
combo_box_number_characters["values"] = (8, 9, 10, 11, 12, 13, 14, 15, 16)
combo_box_number_characters.current(0)
combo_box_number_characters.grid(column = 0, row = 1, sticky = tk.W, padx = 5)

# Creates the checkbuttons for uppercase, lowercase and numbers features

value_check_button_uppercase = tk.IntVar()
value_check_button_lowercase = tk.IntVar()
value_check_button_numbers = tk.IntVar()

values_check_button = [value_check_button_uppercase, value_check_button_lowercase, value_check_button_numbers]
texts_check_button = ["Include uppercase?", "Include lowercase?", "Include numbers?"]

for i in range(3):
    check_button = tk.Checkbutton(labelframe_password_options, text = texts_check_button[i], font = (font_family, font_size), variable = values_check_button[i])
    check_button.grid(column = 0, row = 2 + i, sticky = tk.W)

# Selects the chose features and creates the password

def generate_password():
    num_chars = number_characters.get()
    uppercase = value_check_button_uppercase.get()
    lowercase = value_check_button_lowercase.get()
    numbers = value_check_button_numbers.get()

    password = PasswordGenerator(num_chars, numbers, uppercase, lowercase).generate_password()

    change_password_on_entry(password)

# Modifies the current password at entry widget

def change_password_on_entry(password):
    entry_password.configure(state = "normal")
    entry_password.delete(0, 'end')
    entry_password.insert(0, password)
    entry_password.configure(state = "readonly")

# Creates the button

button_generate_password = ttk.Button(frame, text = "Generate password", command = generate_password)
button_generate_password.pack(pady = padding_height)

# Closes the window

def _quit():
    win.quit()
    win.destroy()
    exit()

# Creates the menu bar

menu_bar = Menu(win)
win.configure(menu = menu_bar)

file_menu = Menu(menu_bar, tearoff = 0)
file_menu.add_command(label = "Exit", command = _quit) # The exit item trigger the function that closes the window
menu_bar.add_cascade(label = "File", menu = file_menu)

win.mainloop()