from time import sleep

box_num = 1

# ----- CONSTANTS
BOX_MARGIN_X = 0

def drive(inches):
    print('Drive: {0:0.1f} in fwd'.format(inches))

def turn_right(deg):
    print('Turn: {0:0.1f} right'.format(deg))

# ---- GET TO BOX 
# Exit home and drive to correct Y level of target
leave_home_fwd = 12 + 24 * bool(box_num >= 7)
drive(leave_home_fwd)


turn_right(90)

# Drive towards box
to_box_fwd = BOX_MARGIN_X + 9 + 6 * ((box_num-1) % 6)
drive(to_box_fwd)

sleep(5)

# Drive towards side aisle of home
fwd = 96 - to_box_fwd
drive(fwd)

turn_right(90)

# Drive towards home B
drive(leave_home_fwd)