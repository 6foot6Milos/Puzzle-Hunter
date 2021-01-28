from tkinter import *
#Menu at the end of the game
def play_again():
    import main
    from main import window, pygame, final_score

    def play_again_command():
        main.window=1
        pygame.mixer.music.stop()
        root.destroy()

    def game_end_command():
        main.window = -1
        pygame.mixer.music.stop()
        root.destroy()

    def instructions_command():
        main.window=4
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

    #Opens the instructions menu
    instructions_button = Button(root, text="Instructions", font=("Helvetica",10), bg = "goldenrod2",fg = "cyan4", width = 20, command = instructions_command)
    instructions_button.place(bordermode=OUTSIDE, x=10, y=10)

    #Text that displays the final score
    score_text = Text(root, width=13, height=1, borderwidth=5, bg="lightgoldenrod", fg="DeepSkyBlue3", font=("Helvetica", 64))
    score_text.insert(INSERT, f"Final Score: {final_score}")
    score_text.place(x=340, y=10)

    #Takes the user back into the game
    start_button = Button(root, text="Play Again", font=("Helvetica, 32"), bg="cyan4", fg="goldenrod2", width=28, command = play_again_command)
    start_button.place(bordermode=OUTSIDE, x=266, y=540)
   
    #Completely exits the game
    quit_button = Button(root, text="Quit", font=("Helvetica, 32"), bg="cyan4", fg="goldenrod2", width=28, command = game_end_command)
    quit_button.place(bordermode=OUTSIDE, x=266, y=720)


    root.mainloop()