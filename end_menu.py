from tkinter import *


play_again():
    root = Tk()
    root.title("Puzzle-Hunter")
    root.geometry("1080x1080")


    start_button = Button(root, text="Play Again",bg="Gold", command = root.destroy)
    start_button.place(bordermode=OUTSIDE, x=200, y=200)

    quit_button = Button(root, text="Start Game", command = root.exit)
    quit_button.place(bordermode=OUTSIDE, x=200, y=200)
