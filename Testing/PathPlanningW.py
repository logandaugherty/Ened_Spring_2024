import math

# Path Planning
# By: Logan Daugherty
# Created: 3-29 | Last Updated: 4-5

# ----- Commands

# These will be replaced with robot movement once Algorithm is confirmed to work

def printFwd(dist):
    print('Drive forward: {0:0.1f}in'.format(dist))

def printTurn(deg):
    print('Turn right {0:0.1f}deg'.format(deg))

def scan_box(success):
    print('Scan Box: Success or Failure: {0}'.format(success))

def place_down_box():
    print('Place Down Box')

# ----- CONSTANTS
BOX_MARGIN_X = 0
BOX_MARGIN_Y = 6

# ----- INPUT

# Shelving Locations
# A1 - 0, A2 - 1, C1 - 2, C2 - 3, B1 - 4, B2 - 5, D1 - 6, D2 - 7
shelving = int(input('What shelving would you like to drive to?\nA1 = 0, A2 = 1\nC1 = 2, C2 = 3\nB1 = 4, B2 = 5\nD1 = 6, D2 = 7\nInput: '))
while shelving < 0 or shelving > 7:
    shelving = int(input('Invalid location.\nWhat shelving would you like to drive to?\nA1 = 0, A2 = 1\nC1 = 2, C2 = 3\nB1 = 4, B2 = 5\nD1 = 6, D2 = 7\nInput: '))

# Box Number
# Numbered like the guide on canvas
# 1-6 on bottom, 7-12 on top
box_num = int(input('What box would you like to drive to? '))
while box_num < 1 or box_num > 12:
    box_num = int(input('Invalid location.\nWhat box would you like to drive to? '))

# Invalid ID
# If the barcode is the incorrect ID
scan_success_input = input('Will the barcode have scanned successfully? (True or False) ')
scan_success = scan_success_input == "True"

# Target location
# Home C - 1, Home B - 2, Home D - 3
target_location = 0
if scan_success:
    target_location = int(input('What would be the target location?\nC = 1\nB = 2\nD = 3\nInput: '))
    while target_location < 0 or target_location > 3:
        target_location = int(input('Invalid location.\nWhat location would you like to drive to drop off? '))


# ---------- OPERATIONS -----

# ---- GET TO BOX 
# Exit home and drive to correct Y level of target
leave_home_fwd = 12 + 24 * bool(box_num >= 7) + 24 * (shelving % 4)
printFwd(leave_home_fwd)

printTurn(90)

# Drive towards box
to_box_fwd = BOX_MARGIN_X + 9 + 6 * ((box_num-1) % 6) + 48 * bool(shelving >= 4)
printFwd(to_box_fwd)

# Turn towards the box
if box_num >= 7:
    printTurn(90)
else:
    printTurn(-90)

# Drive right in front of box
fwd = BOX_MARGIN_Y
printFwd(fwd)

# Scanning would take place here ~~~~
scan_box(scan_success)

# ---- LEAVE BOX

# Drive backwards away from box
fwd = -BOX_MARGIN_Y
printFwd(fwd)

if scan_success:
    # ---- DROP OFF BOX

    # Turn towards target location
    # If the home is on the left-hand side of the map,
    if target_location == 1:
        if box_num >= 7:
            printTurn(90)
        else:
            printTurn(-90)

        # Drive towards box
        fwd = to_box_fwd
        printFwd(fwd)

    # If the home is on the right-hand side of the map,
    else:
        if box_num >= 7:
            printTurn(-90)
        else:
            printTurn(90)

        # Drive towards side aisle of home
        fwd = 96 - to_box_fwd
        printFwd(fwd)

    # Turn to face drop-off home
    if target_location == 1 or target_location == 2:
        printTurn(90)

    else:
        printTurn(-90)
    
    # Drive to drop-off home
    if target_location == 1 or target_location == 3:
        # Drive towards box
        fwd = 108-to_box_fwd
        printFwd(fwd)

    else:
        # Drive towards home B
        fwd = leave_home_fwd
        printFwd(fwd)
    
    place_down_box()



    # ---- Drive Home
    # Back away from drop-off home
    fwd = -6
    printFwd(fwd)

    # Turn away from drop-off
    printTurn(180)

    # If at Drop-off C (Directly facing home)
    if target_location == 1:

        # Simply drive straight home
        fwd = 114
        printFwd(fwd)
    
    # If at any other Drop-off (B or D)
    else:
        # If at B, turn to the left
        if target_location == 2:
            # Drive into bottom aisle 
            fwd = 6
            printFwd(fwd)

            # Turn to drive to Home A
            printTurn(-90)
        
        elif target_location == 3:
            # Drive into bottom aisle 
            fwd = 102
            printFwd(fwd)

            # Turn to drive to Home A
            printTurn(90)

        # Drive in front of Home A
        fwd = 96
        printFwd(fwd)

        # Turn to Home A
        printTurn(-90)

        # Drive into Home A
        fwd = 12
        printFwd(fwd)

# If the scan was not successful
else:
    # Turn towards left edge of map
    if box_num >= 7:
        printTurn(-90)
    else:
        printTurn(90)

    # Drive to left-hand edge of map
    printFwd(to_box_fwd)

    # Turn towards the home
    printTurn(-90)

    # Drive home
    printFwd(leave_home_fwd)

# Return to original direction, prepared for another order
print('Turn to 0deg header')
    