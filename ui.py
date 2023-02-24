from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", background=THEME_COLOR,
                           foreground="white", font=("Arial", 15, "normal"))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0,
                                  borderwidth=0, activebackground=THEME_COLOR, command=self.true)
        self.true_button.config(padx=25, pady=25)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0,
                                   borderwidth=0, activebackground=THEME_COLOR, command=self.false)
        self.false_button.grid(row=2, column=1)

        self.update_question()

        self.window.mainloop()

    def restore_default_canvas(self):
        self.canvas.config(background="White")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)

    def update_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())

    def update_score(self):
        self.score.config(text=f"Score: {self.quiz.score}")

    def after_answer(self):
        self.restore_default_canvas()
        self.update_question()
        self.update_score()

    def finished_quiz(self):
        self.restore_default_canvas()
        self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
        self.score.config(text=f"Final score: {self.quiz.score}")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def give_feedback(self, user_answer):
        if self.quiz.check_answer(user_answer):
            self.canvas.config(background="Green")
            self.canvas.itemconfig(self.question_text, fill="White")
        else:
            self.canvas.config(background="Red")
            self.canvas.itemconfig(self.question_text, fill="White")
        self.canvas.update()

        if self.quiz.still_has_questions():
            self.canvas.after(1000, self.after_answer)

        else:
            self.canvas.after(1000, self.finished_quiz)

    def true(self):
        self.give_feedback("True")

    def false(self):
        self.give_feedback("False")
