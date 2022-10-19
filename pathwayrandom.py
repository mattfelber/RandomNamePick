import random
from tkinter import *
import tkinter
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


root = customtkinter.CTk()
root.title("Pathway Student Randomizer")
p1 = PhotoImage(file='pathwicon.png')
root.iconphoto(False, p1)
root.geometry("480x220")


names = [
    'William G.', 'Marcos', 'Samuel', 'Joao Alberto', 'Bia M.', 'Rane', 'Julia C.', 'Ricardo M.',
    'Ludmilla', 'Cassius', 'Daniel G.', 'Robert', 'Joao Pedro', 'Orlando', 'Ingryd', 'Kyle', 'Fernando',
    'Morone', 'Lucas G.', 'Oliver C.', 'Natasha A.', 'Tassio', 'Richardson', 'Thays', 'Cleiton', 'Nathali'

]

wlabel = customtkinter.CTkLabel(root, text=f"")


def clearwidget(widget):
    widget.destroy()


def get_name():
    global wlabel
    clearwidget(wlabel)
    r = random.choice(names)
    wlabel = customtkinter.CTkLabel(root, text=f"Winner: {r}", text_font=("Helvetica", -18))
    wlabel.pack()


topLabel = customtkinter.CTkLabel(root, text="Click below to choose a student:", text_font=("Roboto Medium", -14))
topLabel.pack(pady=20)

ranButton = customtkinter.CTkButton(root, text="RANDOM", command=get_name)
ranButton.pack(pady=20)

root.mainloop()
