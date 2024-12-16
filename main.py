import ffmpeg
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

def start_convert():
    try:
        finput = file_input.get()
        foutput = file_output.get()
        (
            ffmpeg.input(finput)
            .output(foutput)
            .run()
        )
        messagebox.showinfo(title='ETools File Type Converter', message='Conversion Complete')
        print('Conversion Complete')
    except EXCEPTION as e:
        messagebox.showerror(title='ETools File Type Converter', message=e)

window = customtkinter.CTk()
window.geometry('480x200')
window.title('ETools File Type Converter')

location_warning = CTkLabel(window, text='If file is not in the same directory as ETools, then you must inlude the directory in the file name.', fg_color='red',font=('Monoscape', 10))
location_warning.pack(pady=10)

file_input = CTkEntry(window, placeholder_text='Input File', width=300)
file_input.pack()

start_button = customtkinter.CTkButton(window, text='Start', command=start_convert)
start_button.pack(pady=10)

file_output = CTkEntry(window, placeholder_text='Output file with File Extension. EX: output.mp4 or output.png', width=350)
file_output.pack()

program_label = CTkLabel(window, text='ETools by endie', font=('Monoscape', 10))
program_label.pack(pady=10)

window.mainloop()

#© Copyright 2024 Wyatt Johnson