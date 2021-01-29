'''
Menu accessed from start menu, briefly explains how to play the game
'''

from tkinter import *


def instructions_menu():
    import main
    from main import pygame, window
    pygame.init()
    pygame.mixer.init()

    #Sets the window to start game
    def instructions_command():
            main.window=0
            root.destroy()

    #Fundamental window settings
    root = Tk()
    root.title("Puzzle-Hunter")
    root.geometry("1280x960")
    root.resizable(width=False, height=False)
    
    #Background setup
    bg = PhotoImage(file="Game Files/Objects/Instructions Menu.png")
    bg_label = Label(root, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Button takes the player back to the start game menu
    back_button = Button(root, text="Back", font=("Helvetica",26), bg = "cyan4",fg = "goldenrod2", width = 17, command = instructions_command)
    back_button.place(bordermode=OUTSIDE, x=482, y=250)
    
    root.mainloop()