import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        ### UI SETTING ###
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        ### Create Canvas ###
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question Text", font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        ### Create Label ###
        self.score = Label(text="Score : 0", font=FONT, bg=THEME_COLOR, fg="white", padx=20,pady=20)
        self.score.grid(column=1, row=0)

        ### Create Button ###
        true_img = PhotoImage(file="images/true.png")
        self.true_bt = Button(image=true_img, highlightthickness=0,padx=20,pady=20, command=self.true_pressed)
        self.true_bt.grid(column=0, row=2)
        false_img = PhotoImage(file="images/false.png")
        self.false_bt = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_bt.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the Quiz.\nThe final Score is {self.quiz.score}")
            self.true_bt.config(state="disabled")
            self.false_bt.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
