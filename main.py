import tkinter
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
GREEN2 = "#06FF00"
WORK_MIN = 7
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():

    global timer_text 
    window.after_cancel(counter)
    canvas.itemconfig(timer_text,text="00:00")
   # timer_text = canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))

    #RESET = False


def no():
    print("")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, timer_label, check_button, RESET
    RESET = True
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        timer_label = tkinter.Label(text='BREAK', bg=PINK, fg='black')
        timer_label.grid(column=1, row=0)
        check_button.select()


    else:
        check_button.toggle()
        count_down(WORK_MIN)
        timer_label = tkinter.Label(text='WORK', bg=RED, fg='black')
        timer_label.grid(column=1, row=0)


#

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global  counter
    if RESET:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        print(count)
        if count > 0:
           counter= window.after(1000, count_down, count - 1)

        elif count == 0:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# adding controls
timer_label = tkinter.Label(text='TIMER', bg=YELLOW, fg=GREEN2)
timer_label.grid(column=1, row=0)

start_button = tkinter.Button(text="start", height=2, width=5, bg="#C0D8C0", command=start_timer)
start_button.grid(column=0, row=3)

reset_button = tkinter.Button(text="reset", height=2, width=5, bg="#C0D8C0", command=reset_timer)
reset_button.grid(column=3, row=3)

check_button = tkinter.Checkbutton(bg='red', text="  ", height=2, width=5, command=start_timer)
check_button.grid(column=1, row=4)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=2)
photo = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

window.mainloop()
