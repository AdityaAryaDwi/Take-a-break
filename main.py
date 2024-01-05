from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
BLACK = "#161A30"
RED = "#e7305b"
BLUE = "#001F3F"
BG_COLOR = "#5FBDFF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK="✔"
reps=0
reset_timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_everything():
    window.after_cancel(reset_timer)
    timer_label.config(text="Timer",font=("Courier",50,"bold"),fg=BLUE,bg=BG_COLOR)
    canvas.itemconfig(timer_text,text="00:00")
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# def count_down(tmval):
#     if tmval>=0:
#         print(tmval)
#         window.after(1000,count_down,tmval-1)

# count_down(15)

def start_timer():
    global reps
    reps+=1
    work_secs=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    if reps%8==0:
        timer_label.config(text="Take a chill pill")
        count_down(long_break)
        reps=0
        #start_timer()
    elif reps%2==0:
        timer_label.config(text="Be right Back")
        count_down(short_break)
    else:
        timer_label.config(text="Crush It")
        count_down(work_secs)

def count_down(count):
    mins=count//60
    if mins<10:
        mins="0"+str(mins)
    secs=count%60
    if secs<10:
        secs="0"+str(secs)
    canvas.itemconfig(timer_text,text=f"{mins}:{secs}")
    if count>0:
        global reset_timer
        reset_timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps%2==0:
            current_text=check_label.cget("text")
            check_label.config(text=current_text+CHECK_MARK)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Take a break!")
window.config(padx=100,pady=50)
window["bg"]=BG_COLOR


img=PhotoImage(file="pineapple rani sa.png")
canvas=Canvas(width=326,height=326,bg=BG_COLOR,highlightthickness=0)
canvas.create_image(155,163,image=img,)
timer_text=canvas.create_text(172,225,text="00:00",font=(FONT_NAME,32,"bold"),fill=BLACK)
canvas.grid(row=1,column=1)
timer_label=Label()
timer_label.config(text="Timer",font=("Courier",50,"bold"),fg=BLUE,bg=BG_COLOR)
timer_label.grid(row=0,column=1)
start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)
reset_button=Button(text="Reset",highlightthickness=0,command=reset_everything)
reset_button.grid(row=2,column=2)
check_label=Label(fg=BLUE,bg=BG_COLOR)
#check_label["font"]=("FONT_NAME",20,"bold")
check_label.grid(row=2,column=1)

window.mainloop()