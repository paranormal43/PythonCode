from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th:
    if reps % 8 == 0:
        count_down(long_break_sec)
    elif reps %2 == 0:
        # if it's 2nd\4th\6th rep:
        count_down(short_break_sec)
    else:
        #If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    # if count_sec == 0:
    #     count_sec = "00"
    if count_sec < 10:
        count_sec = "0"+str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
check_mark = "✔"
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

lb_timer = Label(text="TIMER", padx=10, pady=10, fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
lb_timer.grid(column=1, row=0)

bt_start = Button(text="START", highlightthickness=0, command=start_timer)
bt_start.grid(column=0, row=2)

bt_reset = Button(text="RESET", highlightthickness=0)
bt_reset.grid(column=2, row=2)

lb_check = Label(text=check_mark, padx=10, pady=10, fg=GREEN, font=(FONT_NAME, 10,"bold"), bg=YELLOW)
lb_check.grid(column=1, row=3)


window.mainloop()