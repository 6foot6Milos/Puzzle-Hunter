import time
from tkinter import *
from tkinter import messagebox


def timer():
    timer_root = Tk()
    timer_root.geometry("800x800")
    timer_root.title("Timer")


    import main
    from main import root
    # Declaration of variables
    hour=StringVar()
    minute=StringVar()
    second=StringVar()
    
    # setting the default value as 0
    
    minute.set("05")
    second.set("00")
    
    # Use of Entry class to take input from the user
    minuteEntry= Entry(timer_root, width=3, font=("Arial",18,""),textvariable=minute)
    minuteEntry.place(x=130,y=20)
    
    secondEntry= Entry(timer_root, width=3, font=("Arial",18,""),textvariable=second)
    secondEntry.place(x=180,y=20)

    time.sleep(5)
    
    
    def submit():
        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        if temp >-1:
            
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60) 
    
            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = temp//60, secondvalue 
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            # using format () method to store the value up to 
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
    
            # updating the GUI window after decrementing the
            # temp value every time
            timer_root.update()
            time.sleep(1)
    
            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
            
            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1

        else:
            main.window= -1
            timer_root.destroy()
    
    submit()
    
    # infinite loop which is required to
    # run tkinter program infinitely
    # until an interrupt occurs
    root.mainloop()