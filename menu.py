#Menu at the beginning of the game
from tkinter import *

#from main import window, pygame

def start_menu():
    import main
    from main import pygame, window, sys
    pygame.init()
    pygame.mixer.init()

    def start_command():
        pygame.mixer.music.stop()
        main.window=1
        root.destroy()
        
        
    #Handles a quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit([arg])


    root = Tk()
    root.title("Puzzle-Hunter")
    root.geometry("1280x960")
    pygame.mixer.music.load("Objects/01_Main Menu.mp3")
    pygame.mixer.music.play(loops=2)

    bg = PhotoImage(file="Objects/Start Menu.png")
    bg_label = Label(root, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    start_button = Button(root, text="Start Game", bg = "cyan4", fg = "goldenrod2", width = 90, height = 5, command = start_command)
    start_button.place(bordermode=OUTSIDE, x=300, y=540)
    
    root.mainloop()



