
box_num = 8

# ----- CONSTANTS
BOX_MARGIN_X = 0
BOX_MARGIN_Y = 6

def drive(inches):
    print('Drive: {0:0.1f} in fwd'.format(inches))

def turn_right(deg):
    print('Turn: {0:0.1f} right'.format(deg))


# Drive towards box
to_box_fwd = BOX_MARGIN_X + 9 + 6 * ((box_num-1) % 6)
drive(to_box_fwd)

turn_right(90)

drive(BOX_MARGIN_Y)

print('Scan Box')
scan_success = True
if scan_success:
    print('Speak: This box is correct')
else:
    print('Speak: This box is not correct')