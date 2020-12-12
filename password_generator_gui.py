import tkinter as tk
from tkinter import ttk
from tkinter import Menu

from constants import *
from password_generator import PasswordGenerator

class PasswordGeneratorView:
    def __init__(self):
        self.create_widgets()

    def create_widgets(self):
        self.create_window()
        self.create_menu()
        self.create_formulary_frame()
        self.create_heading_label()
        self.create_random_password_entry()
        self.create_labelframe_with_password_options()
        self.create_characters_number_label()
        self.create_combo_box_with_characters_number_options()
        self.create_checkbuttons_with_password_options()
        self.create_password_copy_button()
        self.create_password_generation_button()

    def create_window(self):
        self.window = tk.Tk()
        self.configure_window()
    
    def configure_window(self):
        self.window.title(PROJECT_NAME)
        self.window.iconbitmap(self.window, WINDOW_ICON_PATH)
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.window.resizable(False, False)

    def create_menu(self):
        self.create_menu_bar()
        self.create_menu_items()

    def create_menu_bar(self):
        self.menu_bar = Menu(self.window)
        self.window.configure(menu = self.menu_bar)

    def create_menu_items(self):
        self.create_file_menu_item()

    def create_file_menu_item(self):
        self.file_menu = Menu(self.menu_bar, tearoff = 0)
        self.file_menu.add_command(label = "New", command = self.open_new_gui)
        self.file_menu.add_command(label = "Exit", command = self.close_gui) 
        self.menu_bar.add_cascade(label = "File", menu = self.file_menu)

    def create_formulary_frame(self):
        self.form_frame = ttk.Frame(self.window)
        self.form_frame.pack(padx = FORMULARY_FRAME_PADDING_WIDTH)

    def create_heading_label(self):
        self.heading_label = ttk.Label(self.form_frame, text = PROJECT_NAME, font = (FONT_FAMILY, HEADING_LABEL_FONT_SIZE))
        self.heading_label.pack(pady = HEADING_LABEL_PADDING_HEIGHT) 

    def create_random_password_entry(self):
        self.random_password_entry = ttk.Entry(self.form_frame, width = PASSWORD_ENTRY_WIDTH)
        self.random_password_entry.pack(padx = PADDING_WIDTH)
        self.write_initial_message_on_password_entry()

    def write_initial_message_on_password_entry(self):
        self.random_password_entry.insert(0, INITIAL_MESSAGE_PASSWORD_ENTRY)
        self.random_password_entry.configure(state = "readonly")

    def create_labelframe_with_password_options(self):
        self.labelframe_with_password_options = ttk.LabelFrame(self.form_frame, text = LABELFRAME_WITH_PASSWORD_OPTIONS_LABEL)
        self.labelframe_with_password_options.pack(pady = PADDING_HEIGHT)

    def create_characters_number_label(self):
        self.characters_number_label = ttk.Label(self.labelframe_with_password_options, text = CHARACTERS_NUMBER_LABEL_TEXT, font = (FONT_FAMILY, FONT_SIZE))
        self.characters_number_label.grid(column = 0, sticky = tk.W)

    def create_combo_box_with_characters_number_options(self):
        self.characters_number = tk.IntVar()
        self.combo_box_characters_number_options = ttk.Combobox(self.labelframe_with_password_options, textvariable = self.characters_number, state = "readonly")
        self.set_values_range_for_characters_number_combo_box(SMALLEST_NUMBER_IN_CHARACTERS_NUMBER_OPTIONS, BIGGEST_NUMBER_IN_CHARACTERS_NUMBER_OPTIONS)
        self.combo_box_characters_number_options.current(0)
        self.combo_box_characters_number_options.grid(column = 0, sticky = tk.W, padx = PADDING_WIDTH)

    def set_values_range_for_characters_number_combo_box(self, smallest_value, biggest_value):
        self.combo_box_characters_number_options["values"] = tuple(range(smallest_value, biggest_value + 1))

    def create_checkbuttons_with_password_options(self):
        self.value_checkbutton_uppercase = tk.IntVar()
        self.value_checkbutton_lowercase = tk.IntVar()
        self.value_checkbutton_digits = tk.IntVar()
        self.value_checkbutton_special_chars = tk.IntVar()

        values_checkbuttons = [self.value_checkbutton_digits, self.value_checkbutton_uppercase, self.value_checkbutton_lowercase, self.value_checkbutton_special_chars]
        texts_checkbuttons = ["Include digits?", "Include uppercase?", "Include lowercase?", "Include special chars?"]
        
        # number_of_checkbuttons = len(values_checkbuttons) if len(values_checkbuttons) == len(texts_checkbuttons) else min(len(values_checkbuttons), len(texts_checkbuttons))
        number_of_checkbuttons = len(values_checkbuttons)

        for i in range(number_of_checkbuttons):
            checkbutton = tk.Checkbutton(self.labelframe_with_password_options, text = texts_checkbuttons[i], font = (FONT_FAMILY, FONT_SIZE), variable = values_checkbuttons[i])
            checkbutton.grid(column = 0, sticky = tk.W)

    def create_password_generation_button(self):
        self.password_generation_button = ttk.Button(self.form_frame, text = PASSWORD_GENERATION_BUTTON_TEXT, command = self.generate_password)
        self.password_generation_button.pack(pady = PADDING_HEIGHT)

    def create_password_copy_button(self):
        self.password_copy_button = ttk.Button(self.form_frame, text = COPY_PASSWORD_BUTTON_TEXT, command = self.copy_password)
        self.password_copy_button.pack(pady = PADDING_HEIGHT)

    def copy_password(self):
        random_generated_password = self.random_password_entry.get()
        self.window.clipboard_clear() 
        self.window.clipboard_append(random_generated_password)

    def generate_password(self):
        num_chars = self.characters_number.get()
        has_uppercase = self.value_checkbutton_uppercase.get()
        has_lowercase = self.value_checkbutton_lowercase.get()
        has_digits = self.value_checkbutton_digits.get()
        has_special_chars = self.value_checkbutton_special_chars.get()

        password_generator = PasswordGenerator(num_chars, has_digits, has_uppercase, has_lowercase, has_special_chars)
        random_password = password_generator.generate_password()

        self.change_password_on_entry(random_password)

    def change_password_on_entry(self, random_password):
        self.random_password_entry.configure(state = "normal")
        self.random_password_entry.delete(0, 'end')
        self.random_password_entry.insert(0, random_password)
        self.random_password_entry.configure(state = "readonly")

    def open_new_gui(self):
        PasswordGeneratorView()

    def close_gui(self):
        self.window.quit()
        self.window.destroy()
        exit()

def run():
    password_generator_view = PasswordGeneratorView()
    password_generator_view.window.mainloop()

if __name__ == "__main__":
    run()