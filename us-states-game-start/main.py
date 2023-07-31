import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed_states = []
score = 0
while len(guessed_states) < 50:
    input_box = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt="Type the name of a state").title()
    # input_box = input_box.title()
    if input_box in all_states:
        guessed_states.append(input_box)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == input_box]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(input_box)

    if input_box == "Exit":
        break
missing_states = []
for state in all_states:
    if state not in guessed_states:
        missing_states.append(state)

df2 = pandas.DataFrame(missing_states)
print(df2)






screen.exitonclick()