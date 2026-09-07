import turtle

def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "INIT":
        state = "LEFT"
        t.setheading(180)
        return state, turn

    elif state == "LEFT":
        t.forward(10) # Перемещение
        if x <= -turn:
            state = "UP_AFTER_LEFT"
            t.setheading(90)   #Разворот вверх
        return state, turn

    elif state == "UP_AFTER_LEFT":
        t.forward(10) # Перемещение
        if y >= turn:
            state = "RIGHT"
            t.setheading(0)    #Разворот вправо
        return state, turn

    elif state == "RIGHT":
        t.forward(10) # Перемещение
        if x >= turn:
            state = "UP_AFTER_RIGHT"
            t.setheading(90)   #Разворот вверх
        return state, turn

    elif state == "UP_AFTER_RIGHT":
        t.forward(10) # Перемещение
        if y >= turn:
            turn = turn + 1 # Начало нового витка
            if turn > num_turns:
                state = "STOP"
            else:
                state = "LEFT"
                t.setheading(180)  #Разворот влево
        return state, turn

    elif state == "STOP":
        return state, turn

    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)

    turtle.done()


if __name__ == "__main__":
    draw()
