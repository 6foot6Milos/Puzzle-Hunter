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
    root.geometry("1080x1080")
    pygame.mixer.music.load("Objects/01_Main Menu.mp3")
    pygame.mixer.music.play(loops=2)

    start_button = Button(root, text="Start Game", command = start_command)
    start_button.place(bordermode=OUTSIDE, x=200, y=200)
    
    root.mainloop()



