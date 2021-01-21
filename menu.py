#Menu at the beginning of the game
def start_menu():
    from tkinter import *
    from main import window, pygame
    pygame.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    root = Tk()
    root.title("Puzzle-Hunter")
    root.geometry("1080x1080")

    
    

    window = 1
    start_button = Button(root, text="Start Game", command = root.destroy)
    start_button.place(bordermode=OUTSIDE, x=200, y=200)
    


    root.mainloop()
