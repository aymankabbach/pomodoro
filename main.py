from tkinter import *
import time
window=Tk()
window.title("pomodoroo app")
window.config(bg="#f7f5dd")
PINK = "#e2979c"
RED = "#e7305b"
Tomato_RED="#ff6347"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reset_cliked=False
WORK_MIN=25
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20
seconds=0
canvas=Canvas(width=200,height=224, bg="#f7f5dd", highlightthickness=0)
window.config(padx=100,pady=50)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
#
def create_page_element():
    global Mode_Label,timer,canvas,start_button,reset_button
    page_element=[]
    #
    Mode_Label=Label(window, text="Work",fg=GREEN,bg="#f7f5dd",font=(FONT_NAME,50))
    timer=canvas.create_text(100,130,text=f"{WORK_MIN}:{seconds}",fill="white",font=(FONT_NAME,20,"bold"))
    #
    start_button=Button(window,text="start",command=start_pomodoro)
    reset_button=Button(window,text="reset",command=reset_pomodoro)
    page_element.extend([Mode_Label,canvas,start_button,reset_button])
    return page_element
def grid_page_element():
    page_element=create_page_element()
    row=0
    column=1
    for element in page_element: 
        element.grid(row=row, column=column)
        row+=1
        if row==2:
            row=3
            column=0
        if row>3:
            row=3
            column=2
def work_countdown():
    global WORK_MIN,seconds,reset_cliked
    cliked=True
    while cliked:
        if reset_cliked:
            Mode_Label["text"]="Work"
            canvas.itemconfig(timer,text=f"{WORK_MIN}:{seconds}")
            break
        canvas.itemconfig(timer, text=f"{WORK_MIN}:{seconds}")
        seconds-=1
        if seconds==-1:
            WORK_MIN-=1
            seconds=59
        if WORK_MIN==-1:
            seconds=0
            Mode_Label["text"]="Break"
            canvas.itemconfig(timer,text=f"{SHORT_BREAK_MIN}:{seconds}")
            cliked=False
            WORK_MIN=1
        time.sleep(0.1)
        window.update()
def break_countdown():
    global SHORT_BREAK_MIN,seconds,reset_cliked
    cliked=True
    while cliked:
        if reset_cliked:
            Mode_Label["text"]="Work"
            canvas.itemconfig(timer,text=f"{WORK_MIN}:{seconds}")
            break
        canvas.itemconfig(timer,text=f"{SHORT_BREAK_MIN}:{seconds}")
        seconds-=1
        if seconds==-1:
            SHORT_BREAK_MIN-=1
            seconds=59
        if SHORT_BREAK_MIN==-1:
            seconds=0
            SHORT_BREAK_MIN=1
            cliked=False
        time.sleep(0.1)
        window.update()
def long_break_countdown():
    global LONG_BREAK_MIN,seconds,reset_cliked
    Mode_Label["text"]="Long Break"
    canvas.itemconfig(timer,text=f"{LONG_BREAK_MIN}:{seconds}")
    cliked=True
    while cliked:
        if reset_cliked:
            Mode_Label["text"]="Work"
            canvas.itemconfig(timer,text=f"{WORK_MIN}:{seconds}")
            break
        canvas.itemconfig(timer,text=f"{LONG_BREAK_MIN}:{seconds}")
        seconds-=1
        if seconds==-1:
            LONG_BREAK_MIN-=1
            seconds=59
        if LONG_BREAK_MIN==-1:
            LONG_BREAK_MIN=3
            seconds=0
            cliked=False
        time.sleep(0.1)
        window.update() 
def reset_pomodoro():
    global WORK_MIN,SHORT_BREAK_MIN,LONG_BREAK_MIN,seconds,reset_cliked
    reset_cliked=False
    WORK_MIN=25
    SHORT_BREAK_MIN=5
    LONG_BREAK_MIN=20
    seconds=0
    Mode_Label["text"]="Work"
    canvas.itemconfig(timer,text=f"{WORK_MIN}:{seconds}")
def start_pomodoro():
    global reset_cliked,WORK_MIN,Mode_Label,timer,canvas,seconds
    for x in range(4):
        Mode_Label["text"]="Work"
        work_countdown()
        break_countdown()
        if reset_cliked:
            Mode_Label["text"]="Work"
            canvas.itemconfig(timer,text=f"{WORK_MIN}:{seconds}")
            break
    long_break_countdown()
grid_page_element()
window.mainloop()