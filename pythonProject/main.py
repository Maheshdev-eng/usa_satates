import turtle
import pandas

screen=turtle.Screen()
screen.title("u.s. state game")
image="blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491,width=725)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")
all_state= data.state.to_list()
guessed_state = []

while len(guessed_state)<50:

    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 state correct",prompt="what's another state name").title()
    print(answer_state)

    if answer_state in all_state:
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

screen.exitonclick()