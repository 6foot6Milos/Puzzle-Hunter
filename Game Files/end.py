from tkinter import *
#Menu at the end of the game
def play_again():
    import main
    from main import window, pygame

    def play_again_command():
        main.window=1
        pygame.mixer.music.stop()
        root.destroy()

    def game_end_command():
        main.window = -1
        pygame.mixer.music.stop()
        root.destroy()

    #Fundamental window settings
    root = Tk()
    root.title("Puzzle-Hunter")
    root.geometry("1280x960")
    root.resizable(width=False, height=False)

    #Menu music
    pygame.mixer.music.load("Game Files/Objects/01_Main Menu.mp3")
    pygame.mixer.music.play()

    #Background photo
    bg = PhotoImage(file="Game Files/Objects/End Menu.png")
    bg_label = Label(root, image=bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Takes the user back into the game
    start_button = Button(root, text="Play Again", font=("Helvetica, 32"), bg="cyan4", fg="goldenrod2", width=28, command = play_again_command)
    start_button.place(bordermode=OUTSIDE, x=266, y=540)
   
    #Completely exits the game
    quit_button = Button(root, text="Quit", font=("Helvetica, 32"), bg="cyan4", fg="goldenrod2", width=28, command = game_end_command)
    quit_button.place(bordermode=OUTSIDE, x=266, y=720)


    root.mainloop()