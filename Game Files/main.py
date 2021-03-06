import tkinter
from tkinter import *
from PIL import ImageTk, Image
import pygame
import random, time, sys, os
from menu import start_menu
from instructions import instructions_menu
from end import play_again
pygame.mixer.init()

#Decides which menu to go to
window=0

#Puzzle lists containing each frame of the chess puzzle
puzzle_01 = ["Game Files/Images/d4+.png", "Game Files/Images/d4#.png"]
puzzle_02 = ["Game Files/Images/g6.png", "Game Files/Images/g6 hxg6.png", "Game Files/Images/g6 hxg6 Nxg6#.png"]
puzzle_03 = ["Game Files/Images/Qa5+.png", "Game Files/Images/Qa5+ Kf1.png", "Game Files/Images/Qa5+ Kf1 Qxb5.png"]
puzzle_04 = ["Game Files/Images/Qg7.png", "Game Files/Images/Qg7 Ng7.png", "Game Files/Images/Qg7 Ng7 Nh6.png"]
puzzle_05 = ["Game Files/Images/Nd6+.png", "Game Files/Images/Nd6#.png"]
puzzle_06 = ["Game Files/Images/Bf6+.png", "Game Files/Images/Bf6#.png"]
puzzle_07 = ["Game Files/Images/c8+.png", "Game Files/Images/c8+ Qd8.png", "Game Files/Images/c8+ Qd8 Qd8.png"]
puzzle_08 = ["Game Files/Images/Qh5.png", "Game Files/Images/Qh5 g6.png", "Game Files/Images/Qh5 g6 Qg6 hg6.png", "Game Files/Images/Qh5 g6 Qg6 hg6 Bg6.png"]
puzzle_09 = ["Game Files/Images/Ra5.png", "Game Files/Images/Ra5 c5.png", "Game Files/Images/Ra5 c5 Rxc5.png"]
puzzle_10 = ["Game Files/Images/Qa7.png", "Game Files/Images/Qa7 Ka7.png", "Game Files/Images/Qa7 Ka7 bc8.png"]
puzzle_11 = ["Game Files/Images/Rxa4.png", "Game Files/Images/Rxa4 bxa4.png", "Game Files/Images/Rxa4 bxa4 Qb6 Ka3.png", "Game Files/Images/Rxa4 bxa4 Qb6 Ka3 Qb2.png"]
puzzle_12 = ["Game Files/Images/Qh4.png", "Game Files/Images/Qh4 Kg1.png", "Game Files/Images/Qh4 Kg1 Rg8.png"]

#master list of all the puzzle lists
master_list = [puzzle_01, puzzle_02, puzzle_03, puzzle_04, puzzle_05, puzzle_06, puzzle_07, puzzle_08, puzzle_09, puzzle_10, puzzle_11, puzzle_12]

#Answers list in order of the puzzle lists
answer_01 = ["d4"]
answer_02 = ["g6", "ng6"]
answer_03 = ["qa5", "qb5"]
answer_04 = ["qg7", "nh6"]
answer_05 = ["nd6"]
answer_06 = ["bf6"]
answer_07 = ["c8", "qd8"]
answer_08 = ["qh5", "qg6", "bg6"]
answer_09 = ["ra5", "rc5"]
answer_10 = ["qa7", "bc8=n"]
answer_11 = ["ra4", "qb6", "qb2"]
answer_12 = ["qh4", "rg8"]

#nested list of puzzle answers
master_answer = [answer_01, answer_02, answer_03, answer_04, answer_05, answer_06, answer_07, answer_08, answer_09, answer_10, answer_11, answer_12]


#Offers the user the feature to randomly select a song
def play():
    
    #a random number (1-4) which randomly selects a track for the pygame mixer to play
    random_number = random.randrange(1,4)

    if random_number == 1:
        pygame.mixer.music.load("Game Files/Objects/02_Shop Theme.mp3")
        pygame.mixer.music.play(loops=0)
        
    elif random_number == 2:
        pygame.mixer.music.load("Game Files/Objects/03_Prepare to Race.mp3")
        pygame.mixer.music.play(loops=0)

    elif random_number == 3:
        pygame.mixer.music.load("Game Files/Objects/13_The Arena.mp3")
        pygame.mixer.music.play(loops=0)

    else:
        print("Should not be possible")


#Simple function stops music
def stop():
    pygame.mixer.music.stop()

#Game menu 
def game_loop():
    
    #Receives input from volume slider
    def get_music_volume(event):
        slider_value = music_slider.get()
        pygame.mixer.music.set_volume(slider_value/10)
        
    #Receives chess move from entry widget
    def chess_input_return(event):
        input_value = user_move_input.get()
        print(input_value)
        user_move_input.delete(0, END)
        return input_value


    #Play music button
    music_start_button = Button(root, text="Play Song", font=("Helvetica", 32), command=play)
    music_start_button.configure(bg="gold", fg="purple")
    music_start_button.place(bordermode = OUTSIDE, x=745, y=100)


    #Stop music button
    music_stop_button = Button(root, text="Stop song", font=("Helvetica", 32), command=stop)
    music_stop_button.configure(bg="gold", fg="purple")
    music_stop_button.place(bordermode = OUTSIDE, x=745, y=200)


    #(Entry) Input for chess moves (Not working properly)
    user_move_label = Label(root, text="Your move:")
    user_move_label.place(bordermode=OUTSIDE, x=715, y=850)
    user_move_input = Entry(root, width = 15)
    user_move_input.config(bg="orange")
    user_move_input.bind("<Return>", chess_input_return)
    user_move_input.place(bordermode=OUTSIDE, x=785, y=850)
    

    #Title for music volume slider
    music_slider_title = Label(root, text="Music Volume", bg="white", fg="goldenrod2", font=("Helvetica", 16))
    music_slider_title.place(bordermode=OUTSIDE, x=790, y=320)


    #Music volume slider
    music_slider = Scale(root, from_=1, to=10, tickinterval=10, borderwidth=2, bg="goldenrod2", orient=HORIZONTAL, command=get_music_volume)
    music_slider.set(0)
    music_slider.place(bordermode=OUTSIDE, x=805, y=350)
    
    #for every puzzle answered add one to score
    score = 0

    #Three incorrect answers ends the game
    incorrect = 0

    #For different puzzle program will run different code
    while True:
        
        #Displays the current score
        score_text = Text(root, width=2, height=1, borderwidth=5, bg="goldenrod2", fg="DeepSkyBlue3", font=("Helvetica", 28))
        score_text.insert(INSERT, f"{score}")
        score_text.place(x=802, y=420)

        #Displays how many wrong answers the user has 
        incorrect_text = Text(root, width=2, height=1, borderwidth=5, bg="goldenrod2", fg="red2", font=("Helvetica", 28))
        incorrect_text.insert(INSERT, f"{incorrect}")
        incorrect_text.place(x=862, y=420)

        #Generate random puzzle
        random_puzzle = random.randrange(0, 12)
    
        if window == 4:
            break

        elif incorrect == 3:
            return score
            
        #Handles all chess puzzles with a length of 2 images 
        elif len(master_list[random_puzzle]) == 2:
            image_chooser = 0
            answer_choose = 0
            my_pic = Image.open(master_list[random_puzzle][image_chooser])
            resized = my_pic.resize((500, 500), Image.ANTIALIAS)
            new_pic = ImageTk.PhotoImage(resized)
            my_label = Label(root, image=new_pic)
            my_label.place(x=100, y=495)
            my_label = Label(root, image=None)
            chess_move = input("answer: ")


            if chess_move == master_answer[random_puzzle][image_chooser]:
                image_chooser += 1
                my_pic = Image.open(master_list[random_puzzle][image_chooser])
                resized = my_pic.resize((500, 500), Image.ANTIALIAS)
                new_pic = ImageTk.PhotoImage(resized)
                my_label = Label(root, image=new_pic)
                my_label.place(bordermode = OUTSIDE, x=100, y=495)
                coin_sound = pygame.mixer.Sound("Game Files/Objects/Coin solve sound.x-wav")
                pygame.mixer.Sound.play(coin_sound)
                root.update()
                time.sleep(1)
                score += 1


            else:
                print("Incorrect")
                incorrect_sound = pygame.mixer.Sound("Game Files/Objects/Incorrect.mp3")
                pygame.mixer.Sound.play(incorrect_sound)
                incorrect += 1
        
        #Handles all chess puzzles with a length of 3 images 
        elif len(master_list[random_puzzle]) == 3:
            image_chooser = 0
            answer_choose = 0
            my_pic = Image.open(master_list[random_puzzle][image_chooser])
            resized = my_pic.resize((500, 500), Image.ANTIALIAS)
            new_pic = ImageTk.PhotoImage(resized)
            my_label = Label(root, image=new_pic)
            my_label.place(bordermode = OUTSIDE, x=100, y=495)
            my_label = Label(root, image=None)
            chess_move = input("Answer: ")
            

            if chess_move == master_answer[random_puzzle][answer_choose]:
                image_chooser = 1
                answer_choose = 1
                my_pic = Image.open(master_list[random_puzzle][image_chooser])
                resized = my_pic.resize((500, 500), Image.ANTIALIAS)
                new_pic = ImageTk.PhotoImage(resized)
                my_label = Label(root, image=new_pic)
                my_label.place(bordermode = OUTSIDE, x=100, y=495)
                chess_move = input("Answer: ")
                
                
                if chess_move == master_answer[random_puzzle][answer_choose]:
                    image_chooser += 1
                    my_pic = Image.open(master_list[random_puzzle][image_chooser])
                    resized = my_pic.resize((500, 500), Image.ANTIALIAS)
                    new_pic = ImageTk.PhotoImage(resized)
                    my_label = Label(root, image=new_pic)
                    my_label.place(bordermode = OUTSIDE, x=100, y=495)
                    coin_sound = pygame.mixer.Sound("Game Files/Objects/Coin solve sound.x-wav")
                    pygame.mixer.Sound.play(coin_sound)
                    root.update()
                    time.sleep(1)
                    score += 1
                
                
                else:
                    print("Incorrect")    
                    incorrect_sound = pygame.mixer.Sound("Game Files/Objects/Incorrect.mp3")
                    pygame.mixer.Sound.play(incorrect_sound)
                    incorrect += 1
            else:
                print("Incorrect")
                incorrect_sound = pygame.mixer.Sound("Game Files/Objects/Incorrect.mp3")
                pygame.mixer.Sound.play(incorrect_sound)
                incorrect += 1


        #Handles all puzzles with a length of 4 images
        elif len(master_list[random_puzzle]) == 4:
            image_chooser = 0
            answer_choose = 0
            for i in range(3):
                my_pic = Image.open(master_list[random_puzzle][image_chooser])
                resized = my_pic.resize((500, 500), Image.ANTIALIAS)
                new_pic = ImageTk.PhotoImage(resized)
                my_label = Label(root, image=new_pic)
                my_label.place(bordermode = OUTSIDE, x=100, y=495)
                my_label = Label(root, image=None)
                chess_move = input("Answer: ")
                

                if chess_move == master_answer[random_puzzle][answer_choose]:
                    image_chooser += 1
                    answer_choose += 1
                    break_again = 0

                else:
                    incorrect += 1
                    incorrect_sound = pygame.mixer.Sound("Game Files/Objects/incorrect.mp3")
                    pygame.mixer.Sound.play(incorrect_sound)
                    break_again = 1
                    break

            #resolves issue where the player gains score even when their answer is wrong
            if break_again == 1:
                continue

            else:
                my_pic = Image.open(master_list[random_puzzle][image_chooser])
                resized = my_pic.resize((500, 500), Image.ANTIALIAS)
                new_pic = ImageTk.PhotoImage(resized)
                my_label = Label(root, image=new_pic)
                my_label.place(bordermode = OUTSIDE, x=100, y=495)
                coin_sound = pygame.mixer.Sound("Game Files/Objects/Coin solve sound.x-wav")
                pygame.mixer.Sound.play(coin_sound)
                root.update()
                time.sleep(1)
                score += 1

    
pygame.mixer.music.load("Game Files/Objects/01_Main Menu.mp3")
pygame.mixer.music.play(loops=2)

#Main game loop
while True:
    
    if window == 0:
        start_menu()
        
    elif window == 4:
        instructions_menu()

    elif window == 1:
        #fundamental screen settings
        root = Tk()
        root.title("Puzzle-Hunter")
        root.geometry("1080x1080")
        root.resizable(width=False, height=False)

        bg = PhotoImage(file="Game Files/Objects/bg.png")
        bg_label = Label(root, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        final_score = game_loop()
        pygame.mixer.music.stop()
        window=2
        
       
        root.destroy()
    
    
    elif window == 2:
        play_again()

    elif window == -1:
        sys.exit()
        

root.mainloop()

