from tkinter import *


def game_start(): 
    x=10
    print(x)


def start_menu():
    root = Tk()
    root.title("Puzzle-Hunter")
    root.geometry("1080x1080")





    start_button = Button(root, text="Start Game", command = game_start)
    start_button.grid(column=2,row=3)



    root.mainloop()
