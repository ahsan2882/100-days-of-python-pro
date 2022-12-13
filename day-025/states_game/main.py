from PIL import Image
from pathlib import Path
from turtle import Turtle, Screen

import pandas as pd


image_loc = Path(Path(__file__).parent.resolve(),
                 r'blank_states_img.gif').resolve()
# # Uncomment the commented code first time only

# with open(image_loc, 'rb') as f:
#     image = f.read()
image = str(image_loc)
# img = Image.open(image_loc)
# img = img.convert('RGB').convert('P', palette=Image.ADAPTIVE)
# img.save(image_loc)
states_file = Path(Path(__file__).parent.resolve(), r'50_states.csv').resolve()
data = pd.read_csv(states_file)
all_states = data.state.to_list()

screen = Screen()
turtle = Turtle()
t = Turtle()
t.penup()
t.hideturtle()
screen.title("U.S. States Game")
screen.addshape(image)
screen.setup(width=725, height=491)

turtle.shape(image)
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50  Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [
            state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(Path(Path(__file__).parent.resolve(),
                        'states_to_learn.csv').resolve())
        break
    if answer_state in all_states:
        data_state = data[data.state == answer_state]
        t.goto(
            int(data_state.x),
            int(data_state.y)
        )
        t.write(data_state.state.item(), align="center",
                font=("Arial", 8, "normal"))
        guessed_states.append(answer_state.lower())
        all_states.remove(answer_state)


screen.exitonclick()
