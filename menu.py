from tkinter import *


def game_start(): 
    quit()


def start_menu():
    root = Tk()
    root.title("Puzzle-Hunter")
    root.geometry("1080x1080")





    start_button = Button(root, text="Start Game", command = game_start)
    start_button.place(bordermode=OUTSIDE, x=200, y=200)



    root.mainloop()
