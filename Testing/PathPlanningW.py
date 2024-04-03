import math

def printFwd(dist):
    print('Drive forward: {0:0.1f}in'.format(dist))

def printTurn(deg):
    print('Turn right {0:0.1f}deg'.format(deg))
        


# ----- INPUT

# Shelving Locations
# A1 - 0, A2 - 1, C1 - 2, C2 - 3, B1 - 4, B2 - 5, D1 - 6, D2 - 7
shelving = int(input('What shelving would you like to drive to? '))
while shelving < 0 or shelving > 7:
    shelving = int(input('Invalid location.\nWhat shelving would you like to drive to? '))

# Box Number
# Numbered like the guide on canvas
# 1-6 on top, 7-12 on bottom
box_num = int(input('What box would you like to drive to? '))
while box_num < 1 or box_num > 12:
    box_num = int(input('Invalid location.\nWhat box would you like to drive to? '))

# Invalid ID
# If the barcode is the incorrect ID
scan_success = bool(input('Will the barcode have scanned successfully? (True or False) '))

# Target location
# Home A - 0, Home C - 1, Home B - 2, Home D - 3
target_location = 0
if scan_success:
    target_location = int(input('What would be the target location?'))
    while target_location < 0 or target_location > 3:
        target_location = int(input('Invalid location.\nWhat location would you like to drive to drop off? '))


# ---------- OPERATIONS -----

# ---- GET TO BOX 
# Exit home and drive to correct Y level of target
leave_home_fwd = 12 + 24 * bool(box_num <= 7) + 24 * (shelving % 4)
printFwd(leave_home_fwd)

printTurn(90)

# Drive towards box
to_box_fwd = 9 + 6 * ((box_num-1) % 6) + 48 * bool(shelving >= 4)
print('Drive forward: {0:0.1f}in'.format(to_box_fwd))

# Turn towards the box
if box_num <= 6:
    printTurn(90)
else:
    printTurn(-90)

# Drive right in front of box
fwd = 6
printFwd(fwd)

# Scanning would take place here ~~~~

# Drive backwards away from box
fwd = 6
printFwd(fwd)

# ---- LEAVE BOX
if scan_success:
    # Turn towards target location
    # Swapped direction from previous
    if target_location <= 1:
        if box_num <= 6:
            printTurn(90)
        else:
            printTurn(-90)

        # Drive towards box
        fwd = to_box_fwd
        printFwd(fwd)

    else:
        if box_num <= 6:
            printTurn(-90)
        else:
            printTurn(90)

        # Drive towards box
        fwd = 96 - to_box_fwd
        printFwd(fwd)


    if target_location == 0 or target_location == 3:
        if box_num <= 6:
            printTurn(-90)
        else:
            printTurn(90)

    else:
        if box_num <= 6:
            printTurn(-90)
        else:
            printTurn(90)

    # Drive to home/dropoff location
    if target_location <= 1:
        if box_num <= 6:
            printTurn(90)
        else:
            printTurn(-90)

        # Drive towards box
        fwd = to_box_fwd
        printFwd(fwd)

    else:
        if box_num <= 6:
            printTurn(-90)
        else:
            printTurn(90)

        # Drive towards box
        fwd = 96 - to_box_fwd
        printFwd(fwd)

print('Turn to 0deg header')
    