#Menu at the end of the game
def play_again():
    from tkinter import *
    from main import window, pygame
    pygame.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    root = Tk()
    root.title("Puzzle-Hunter")
    root.geometry("1080x1080")


    start_button = Button(root, text="Play Again",bg="Gold", command = root.destroy)
    start_button.place(bordermode=OUTSIDE, x=200, y=200)
    window = 1
    return window

    quit_button = Button(root, text="Quit", command = root.destroy)
    quit_button.place(bordermode=OUTSIDE, x=200, y=250)

    root.mainloop()