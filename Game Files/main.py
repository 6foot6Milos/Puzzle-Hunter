import tkinter
from tkinter import *
from PIL import ImageTk, Image
import pygame
import random, time, sys
from menu import start_menu
from end import play_again
from timer import timer
import threading
from multiprocessing import Process
import concurrent.futures
#from pygame.locals import *
pygame.mixer.init()


#Decides which menu to go to
window=0

#Puzzle lists
puzzle_01 = ["Game Files/Images/d4+.png", "Game Files/Images/d4#.png"]
puzzle_02 = ["Game Files/Images/g6.png", "Game Files/Images/g6 hxg6.png", "Game Files/Images/g6 hxg6 Nxg6#.png"]
puzzle_03 = ["Game Files/Images/Qa5+.png", "Game FilesImages/Qa5+ Kf1.png", "Images/Qa5+ Kf1 Qxb5.png"]
puzzle_04 = ["Game Files/Images/Qg7.png", "Game Files/Images/Qg7 Ng7.png", "Game Files/Images/Qg7 Ng7 Nh6.png"]
puzzle_05 = ["Game Files/Images/Nd6+.png", "Game Files/Images/Nd6#.png"]
puzzle_06 = ["Game Files/Images/Bf6+.png", "Game Files/Images/Bf6#.png"]
puzzle_07 = ["Game Files/Images/c8+.png", "Game Files/Images/c8+ Qd8.png", "Game Files/Images/c8+ Qd8 Qd8.png"]
puzzle_08 = ["Game Files/Images/Qh5.png", "Game Files/Images/Qh5 g6.png", "Game Files/Images/Qh5 g6 Qg6 hg6.png", "Game Files/Images/Qh5 g6 Qg6 hg6 Bg6.png"]
puzzle_09 = []


#master list of all the puzzle lists
master_list = [puzzle_01, puzzle_02, puzzle_03, puzzle_04, puzzle_05, puzzle_06, puzzle_07, puzzle_08]


#Answers list in order
answer_01 = ["d4"]
answer_02 = ["g6", "ng6"]
answer_03 = ["qa5", "qb5"]
answer_04 = ["qg7", "nh6"]
answer_05 = ["nd6"]
answer_06 = ["bf6"]
answer_07 = ["c8", "qd8"]
answer_08 = ["qh5", "qg6", "bg6"]


#nested list of puzzle answers
master_answer = [answer_01, answer_02, answer_03, answer_04, answer_05, answer_06, answer_07, answer_08]

def action():
    action_label = Label(root, text="You clicked")
    action_label.pack(pady = 20)






def click():
    labell = Label(root, text=e)
    labell.pack(padx=100)

#Updates text after 5 mins
def timer_update():
    #timer_label.config(text="Time's up", font=("Helvetica", 32))
    window = 2
    root.destroy()

def play():

    #Mostly in the interest of learning how to use music, the following code takes
    #a random number (1-4) which randomly selects a track for the pygame mixer to play
    random_number = random.randrange(1,4)
    print(random_number)

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

  
    
    #Text changes from "GOGOGO" to "Times up bro" after 5 minutes (300000 milliseconds) 
    #timer_label = Label(root, text="5:00", font=("Helvetica", 32), fg=("gold"), bg = "white")
    #timer_label.place(x=810, y=300)
    #timer_label.after(300000, timer_update)

    #with concurrent.futures.ProcessPoolExecutor() as executor:
    #    f1 = executor.submit(timer)

  
    #Play music button
    music_start_button = Button(root, text="Play Song", font=("Helvetica", 32), command = play)
    music_start_button.configure(bg="gold", fg="purple")
    music_start_button.place(bordermode = OUTSIDE, x=745, y=100)


    #Stop music button
    music_stop_button = Button(root, text="Stop song", font=("Helvetica", 32), command=stop)
    music_stop_button.configure(bg="gold", fg="purple")
    music_stop_button.place(bordermode = OUTSIDE, x=745, y=200)

    #Input for chess moves
    user_move_input = Entry(root, width = 15)
    user_move_input.config(bg="orange")
    user_move_input.place(bordermode=OUTSIDE, x=730, y=850)

    #Slider for music volume
    music_slider = Scale(root, from_=1, to=10, tickinterval = 10, orient=HORIZONTAL)
    music_slider.pack()
    pygame.mixer.music.set_volume(music_slider.get()/10)

    #RANDOM BUTTON NOT CURRENTLY IN USE
    random_button = Button(root, text = "Enter Move")
    random_button.bind("<Return>", click)
    random_button.place(bordermode=OUTSIDE, x=830, y=845)


    #Timer process
    #p1 = Process(target = timer)
    #p1.start()
    timer()


    #for every puzzle answered add one to score
    score = 0

    #Three incorrect answers ends the game
    incorrect = 0

    #x and y of checkmark/red x/ neutral gray
    solution_x = 80
    solution_y = 300

    
   

    #For different puzzle program will run different code
    while True:
        
        #Generate random puzzle
        random_puzzle = random.randrange(0, 8)
    

        if incorrect ==3:
            print(f"thats it, your score is: {score}")
            break


        elif len(master_list[random_puzzle]) == 2:
            image_chooser = 0
            answer_choose = 0
            my_pic = Image.open(master_list[random_puzzle][image_chooser])
            resized = my_pic.resize((500, 500), Image.ANTIALIAS)
            new_pic = ImageTk.PhotoImage(resized)
            my_label = Label(root, image=new_pic)
            my_label.place(bordermode = OUTSIDE, x=100, y=495)
            my_label = Label(root, image=None)
            chess_move = input("Answer: ")

            if chess_move == master_answer[random_puzzle][image_chooser]:
                image_chooser += 1
                my_pic = Image.open(master_list[random_puzzle][image_chooser])
                resized = my_pic.resize((500, 500), Image.ANTIALIAS)
                new_pic = ImageTk.PhotoImage(resized)
                my_label = Label(root, image=new_pic)
                my_label.place(bordermode = OUTSIDE, x=100, y=495)
                coin_sound = pygame.mixer.Sound("Objects/Coin solve sound.x-wav")
                pygame.mixer.Sound.play(coin_sound)
                chess_move = input("PRESS ANY KEY")
                time.sleep(1)
                score += 1
                print(score)


                #Correct answer places checkmark
                checkmark = PhotoImage(file="Objects/Green checkmark.png")
                checkmark_label = Label(root, image=checkmark)
                checkmark_label.config(bg="white")
                checkmark_label.place(x=solution_x, y=solution_y)
                checkmark_label = Label(root, image=None)

                solution_x += 50
               
        
            else:
                print("Incorrect")
                incorrect += 1
        

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
                    coin_sound = pygame.mixer.Sound("Objects/Coin solve sound.x-wav")
                    pygame.mixer.Sound.play(coin_sound)
                    chess_move = input("PRESS ANY KEY")
                    time.sleep(1)
                    score += 1
                    print(score)
                
                    #Correct answer places checkmark
                    checkmark = PhotoImage(file="Objects/Green checkmark.png")
                    checkmark_label = Label(root, image=checkmark)
                    checkmark_label.config(bg="white")
                    checkmark_label.place(x=solution_x, y=solution_y)
                    checkmark_label = Label(root, image=None)

                    solution_x += 50
                    

                else:
                    print("Incorrect")    
                    incorrect += 1
            else:
                print("Incorrect")
                incorrect += 1

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
                    

                else:
                    incorrect += 1
                    break

            my_pic = Image.open(master_list[random_puzzle][image_chooser])
            resized = my_pic.resize((500, 500), Image.ANTIALIAS)
            new_pic = ImageTk.PhotoImage(resized)
            my_label = Label(root, image=new_pic)
            my_label.place(bordermode = OUTSIDE, x=100, y=495)
            coin_sound = pygame.mixer.Sound("Objects/Coin solve sound.x-wav")
            pygame.mixer.Sound.play(coin_sound)
            chess_move = input("PRESS ANY KEY")
            time.sleep(1)
            score += 1
            print(score)

    

#Main game loop
while True:
    if window==0:
        start_menu()
        
        

    elif window==1:
        root = Tk()
        root.title("Puzzle-Hunter")
        root.geometry("1080x1080")
        bg = PhotoImage(file="Game Files/Objects/bg.png")
        bg_label = Label(root, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        

        window=2
        
        game_loop()
        root.destroy()
        

    elif window==2:
        play_again()

    elif window== -1:
        sys.exit()
        

root.mainloop()

