box_num = 8

# ----- CONSTANTS
BOX_MARGIN_X = 0
BOX_MARGIN_Y = 6

def drive(inches):
    print('Drive: {0:0.1f} in fwd'.format(inches))

def turn_right(deg):
    print('Turn: {0:0.1f} right'.format(deg))

print('Pick up Box')

drive(-BOX_MARGIN_Y)

turn_right(-90)

to_box_fwd = BOX_MARGIN_X + 9 + 6 * ((box_num-1) % 6)
fwd = 54 - to_box_fwd
fwd -= 12
drive(fwd)

print('Lower Box')