import tkinter as tk
from tkinter import ttk
from tkinter import Menu

from constants import *
from classes.password_generator import PasswordGenerator

class PasswordGeneratorView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(PROJECT_NAME)
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.window.resizable(False, False)

        self.create_menu()

        self.form_frame = ttk.Frame(self.window)
        self.form_frame.pack(padx = 70)

        self.project_title = ttk.Label(self.form_frame, text = PROJECT_NAME, font = (FONT_FAMILY, PROJECT_TITLE_FONT_SIZE))
        self.project_title.pack(pady = PROJECT_TITLE_PADDING_HEIGHT) 

        self.random_password_entry = ttk.Entry(self.form_frame, width = PASSWORD_ENTRY_WIDTH)
        self.random_password_entry.pack(padx = PADDING_HEIGHT)

        self.write_initial_message_on_password_entry()

        self.labelframe_with_password_options = ttk.LabelFrame(self.form_frame, text = "Options")
        self.labelframe_with_password_options.pack(pady = PADDING_HEIGHT)

        text_number_characters = ttk.Label(self.labelframe_with_password_options, text = "Number of characters", font = (FONT_FAMILY, FONT_SIZE))
        text_number_characters.grid(column = 0, row = 0, sticky = tk.W)

        self.characters_number = tk.IntVar()
        self.combo_box_characters_number = ttk.Combobox(self.labelframe_with_password_options, textvariable = self.characters_number, state = "readonly")
        self.combo_box_characters_number["values"] = tuple(range(8, 17))
        self.combo_box_characters_number.current(0)
        self.combo_box_characters_number.grid(column = 0, row = 1, sticky = tk.W, padx = PADDING_HEIGHT)
    
        self.create_checkbuttons()

        self.button_generate_password = ttk.Button(self.form_frame, text = BUTTON_TEXT, command = self.generate_password)
        self.button_generate_password.pack(pady = PADDING_HEIGHT)

    def generate_password(self):
        num_chars = self.characters_number.get()
        has_uppercase = self.value_checkbutton_uppercase.get()
        has_lowercase = self.value_checkbutton_lowercase.get()
        has_numbers = self.value_checkbutton_numbers.get()

        password_generator = PasswordGenerator(num_chars, has_numbers, has_uppercase, has_lowercase)
        random_password = password_generator.generate_password()

        self.change_password_on_entry(random_password)

    def write_initial_message_on_password_entry(self):
        self.random_password_entry.insert(0, INITIAL_MESSAGE_PASSWORD_ENTRY)
        self.random_password_entry.configure(state = "readonly")

    def change_password_on_entry(self, random_password):
        self.random_password_entry.configure(state = "normal")
        self.random_password_entry.delete(0, 'end')
        self.random_password_entry.insert(0, random_password)
        self.random_password_entry.configure(state = "readonly")

    def create_menu(self):
        self.menu_bar = Menu(self.window)
        self.window.configure(menu = self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff = 0)
        self.file_menu.add_command(label = "New", command = self.open_new_gui)
        self.file_menu.add_command(label = "Exit", command = self.close_gui) # The exit item trigger the function that closes the self.windowdow
        self.menu_bar.add_cascade(label = "File", menu = self.file_menu)

    def create_checkbuttons(self):
        self.value_checkbutton_uppercase = tk.IntVar()
        self.value_checkbutton_lowercase = tk.IntVar()
        self.value_checkbutton_numbers = tk.IntVar()

        values_checkbuttons = [self.value_checkbutton_uppercase, self.value_checkbutton_lowercase, self.value_checkbutton_numbers]
        texts_checkbuttons = ["Include uppercase?", "Include lowercase?", "Include numbers?"]
        
        number_of_checkbuttons = len(values_checkbuttons) if len(values_checkbuttons) == len(texts_checkbuttons) else min(len(values_checkbuttons), len(texts_checkbuttons))

        for i in range(number_of_checkbuttons):
            checkbutton = tk.Checkbutton(self.labelframe_with_password_options, text = texts_checkbuttons[i], font = (FONT_FAMILY, FONT_SIZE), variable = values_checkbuttons[i])
            checkbutton.grid(column = 0, row = 2 + i, sticky = tk.W)

    def open_new_gui(self):
        PasswordGeneratorView()

    def close_gui(self):
        self.window.quit()
        self.window.destroy()
        exit()

if __name__ == "__main__":
    password_generator_view = PasswordGeneratorView()
    password_generator_view.window.mainloop()