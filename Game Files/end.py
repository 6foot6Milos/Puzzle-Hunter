from tkinter import *
#Menu at the end of the game
def play_again():
    import main
    from main import window, pygame

    def play_again_command():
        main.window=1
        root.destroy()

    def game_end_command():
        main.window = -1
        root.destroy()

    root = Tk()
    root.title("Puzzle-Hunter")
    root.geometry("1080x1080")
    root.resizable(width=False, height=False)


    start_button = Button(root, text="Play Again",bg="Gold", command = play_again_command)
    start_button.place(bordermode=OUTSIDE, x=200, y=200)
   

    quit_button = Button(root, text="Quit", command = game_end_command)
    quit_button.place(bordermode=OUTSIDE, x=200, y=250)

    root.mainloop()