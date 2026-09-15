screen_precision = 0
console_precision = 0
myVariable = 0
current_space_number = 0
dice1 = 0
dice2 = 0
space_to_move = 0
FWD = Event()
LT = Event()
RT = Event()
move_forward = Event()
right_turn = Event()
left_turn = Event()

def roll_dice():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    dice1 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice1))
    brain.screen.next_row()
    dice2 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice2))
    brain.screen.next_row()
    space_to_move = dice1 + dice2

def move():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    brain.screen.print(str("Moving") + str(str("spaces_to_move") + str("spaces!")))
    brain.screen.next_row()
    for repeat_count in range(int(current_space_number)):
        move_forward.broadcast_and_wait()
        current_space_number = current_space_number + 1
        if current_space_number > 12:
            current_space_number = 1
        if current_space_number == 1:
            right_turn.broadcast_and_wait()
        if current_space_number == 4:
            right_turn.broadcast_and_wait()
        if current_space_number == 7:
            right_turn.broadcast_and_wait()
        if current_space_number == 10:
            right_turn.broadcast_and_wait()
        wait(5, MSEC)

def play_game():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    while True:
        roll_dice()
        move()
        complete_task()
        wait(5, MSEC)

def complete_task():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    brain.screen.print(str("Landed on space") + str(current_space_number))
    brain.screen.next_row()
    wait(1, SECONDS)
    if current_space_number == 1:
        # Space = GO
        pass
    elif current_space_number == 4:
        # Space = Jail
        pass
    elif current_space_number == 7:
        # Space = Free Parking
        pass
    elif current_space_number == 10:
        # Space = Go to Jail
        pass
    else:
        # Space = Blue 1 or 2, Green 1 or 2, Yellow 1 or 2, or Red 1 or 2
        pass
    if current_space_number == 1:
        # Space = GO
        for repeat_count2 in range(4):
            left_turn.broadcast_and_wait()
            wait(5, MSEC)
    elif current_space_number == 4:
        # Space = Jail
        wait(3, SECONDS)
    elif current_space_number == 7:
        # Space = Free Parking
        wait(5, SECONDS)
    elif current_space_number == 10:
        # Space = Go to Jail
        right_turn.broadcast_and_wait()
        for repeat_count3 in range(3):
            move_forward.broadcast_and_wait()
            wait(5, MSEC)
        left_turn.broadcast_and_wait()
        for repeat_count4 in range(3):
            right_turn.broadcast_and_wait()
            wait(5, MSEC)
        current_space_number = 4
        wait(1, SECONDS)
    else:
        # Space = Blue 1 or 2, Green 1 or 2, Yellow 1 or 2, or Red 1 or 2
        right_turn.broadcast_and_wait()
        move_forward.broadcast_and_wait()
        for repeat_count5 in range(2):
            left_turn.broadcast_and_wait()
            wait(5, MSEC)
        move_forward.broadcast_and_wait()
        right_turn.broadcast_and_wait()

def FWD_callback_0():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    pass

def FWD_callback_1():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    pass

def RT_callback_0():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    pass

def RT_callback_1():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    pass

def when_started1():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    current_space_number = 1
    play_game()

def LT_callback_0():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    pass

def LT_callback_1():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, my_event, move_forward, right_turn, left_turn, screen_precision, console_precision
    pass

# system event handlers
FWD(FWD_callback_0)
FWD(FWD_callback_1)
RT(RT_callback_0)
RT(RT_callback_1)
LT(LT_callback_0)
LT(LT_callback_1)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
