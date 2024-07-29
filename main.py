def on_gesture_shake():
    global jankenpon
    jankenpon = randint(1, 3)
    if jankenpon == 1:
        basic.show_icon(IconNames.SQUARE)
    elif jankenpon == 2:
        basic.show_icon(IconNames.CHESSBOARD)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

jankenpon = 0
basic.show_string("\"jankenpon\"")
