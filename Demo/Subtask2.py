Continuing_subtask1_program = False

def drive(inches):
    print('Drive: {0:0.1f} in fwd'.format(inches))

def turn_right(deg):
    print('Turn: {0:0.1f} right'.format(deg))

# ----- CONSTANTS
BOX_MARGIN_X = 0
BOX_MARGIN_Y = 6

if not Continuing_subtask1_program:
    print('Initializing Sensors')
    print('Setting Gyro Angle to 180')

drive(-12)

turn_right(90)

drive(96)

turn_right(-90)

drive(12)

print('Turn To 0 degrees header')