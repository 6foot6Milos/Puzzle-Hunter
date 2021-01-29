'''
Menu at the beginning of the game that offers play and instructions options
'''
from tkinter import *


def start_menu():
    import main
    from main import pygame, window
    import instructions
    from instructions import instructions_menu
    pygame.init()
    pygame.mixer.init()

    #Sets the window to the game menu
    def start_command():
        pygame.mixer.music.stop()
        main.window=1
        root.destroy()

    #Sets the window to the instructions menu
    def instructions_command():
        main.window=4
        root.destroy()
        
    #Fundamental window settings
    root = Tk()
    root.title("Puzzle-Hunter")
    root.geometry("1280x960")
    root.resizable(width=False, height=False)

    #Background setup
    bg = PhotoImage(file="Game Files/Objects/Start Menu.png")
    bg_label = Label(root, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Enters main game loop
    start_button = Button(root, text="Start Game", font=("Helvetica",32), bg = "cyan4",fg = "goldenrod2", width = 28, command = start_command)
    start_button.place(bordermode=OUTSIDE, x=266, y=540)
    
    #Opens the instructions menu
    instructions_button = Button(root, text="Instructions", font=("Helvetica",10), bg = "turquoise3",fg = "blue", width = 20, command = instructions_command)
    instructions_button.place(bordermode=OUTSIDE, x=10, y=920)

    root.mainloop()



