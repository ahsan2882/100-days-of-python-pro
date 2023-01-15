from tkinter import Tk, Label, Button, Canvas, PhotoImage
from pathlib import Path
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

TRUE_PATH = Path(
    Path(__file__).parent.resolve(),
    'images',
    'true.png'
).resolve()

FALSE_PATH = Path(
    Path(__file__).parent.resolve(),
    'images',
    'false.png'
).resolve()


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file=TRUE_PATH)
        self.true_button = Button(
            image=true_image, highlightthickness=0, bg=THEME_COLOR, command=lambda: self.check_answer('True'))
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file=FALSE_PATH)
        self.false_button = Button(
            image=false_image, highlightthickness=0, bg=THEME_COLOR, command=lambda: self.check_answer('False'))
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer(self, answer):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)
        self.window.after(1000, self.get_next_question)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
