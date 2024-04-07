from Demo.CustomMotorGroup import *
from Demo.ScanBox import *
from Demo.Lift import *

# -------------------------------------------------------------

# Final Track
# Robot drives to a designated box, scans it, and drives to a target location, if applicable

# ENTER DATA HERE

# Shelving Locations
# A1 - 0, A2 - 1, C1 - 2, C2 - 3, B1 - 4, B2 - 5, D1 - 6, D2 - 7
shelving_list = [2]

# Box Number
# Numbered like the guide on canvas
# 1-6 on bottom, 7-12 on top
box_num_list = [5]

# Target location
# Home C - 1, Home B - 2, Home D - 3
target_location_list = [1]

# NOTE: ALL LISTS MUST HAVE THE SAME NUMBER OF ELEMENTS
#   The list is for each shelve, box, and drop-off location

# -------------------------------------------------------------

# ----- CONSTANTS
BOX_MARGIN_X = 0
BOX_MARGIN_Y = 6

# ---------- INITIALIZATION -----
drive = MotorGroup()
drive.init()

# ---------- OPERATIONS -----

for i in range(len(shelving_list)):
    # Store the values 
    shelving = shelving_list[i]
    box_num = box_num_list[i]
    target_location = target_location_list[i]

    # ---- GET TO BOX 
    # Exit home and drive to correct Y level of target
    leave_home_fwd = 12 + 24 * bool(box_num >= 7) + 24 * (shelving % 4)
    drive.drive_in(leave_home_fwd)

    drive.turn_ang_rel(90)

    # Drive towards box
    to_box_fwd = BOX_MARGIN_X + 9 + 6 * ((box_num-1) % 6) + 48 * bool(shelving >= 4)
    drive.drive_in(to_box_fwd)

    # Turn towards the box
    if box_num >= 7:
        drive.turn_ang_rel(90)
    else:
        drive.turn_ang_rel(-90)

    # Drive right in front of box
    fwd = BOX_MARGIN_Y
    drive.drive_in(fwd)

    # Scanning would take place here ~~~~
    scan_success = scan_box()

    # ---- LEAVE BOX
    if scan_success:
        raise_box()
        
    # Drive backwards away from box
    fwd = -BOX_MARGIN_Y
    drive.drive_in(fwd)

    if scan_success:
        # ---- DROP OFF BOX

        # Turn towards target location
        # If the home is on the left-hand side of the map,
        if target_location == 1:
            if box_num >= 7:
                drive.turn_ang_rel(90)
            else:
                drive.turn_ang_rel(-90)

            # Drive towards box
            fwd = to_box_fwd
            drive.drive_in(fwd)

        # If the home is on the right-hand side of the map,
        else:
            if box_num >= 7:
                drive.turn_ang_rel(-90)
            else:
                drive.turn_ang_rel(90)

            # Drive towards side aisle of home
            fwd = 96 - to_box_fwd
            drive.drive_in(fwd)

        # Turn to face drop-off home
        if target_location == 1 or target_location == 2:
            drive.turn_ang_rel(90)

        else:
            drive.turn_ang_rel(-90)
        
        # Drive to drop-off home
        if target_location == 1 or target_location == 3:
            # Drive towards box
            fwd = 108-leave_home_fwd
            drive.drive_in(fwd)

        else:
            # Drive towards home B
            fwd = leave_home_fwd-6
            drive.drive_in(fwd)
        
        lower_box()

        # ---- Drive Home
        # Back away from drop-off home
        fwd = -6
        drive.drive_in(fwd)

        # If at Drop-off B
        if target_location == 1 or target_location == 3:
            # Turn away from drop-off
            drive.turn_ang_rel(180)

            # If at Drop-off C (Directly facing home)
            if target_location == 1:

                # Simply drive straight home
                fwd = 108
                drive.drive_in(fwd)
                
            # If at any other Drop-off (B or D)
            elif target_location == 3:
                # Drive into bottom aisle 
                fwd = 102
                drive.drive_in(fwd)

        if target_location == 2 or target_location == 3:
                # Turn to drive to Home A
                drive.turn_ang_rel(90)

                # Drive in front of Home A
                fwd = 96
                drive.drive_in(fwd)

                # Turn to Home A
                drive.turn_ang_rel(-90)

                # Drive into Home A
                fwd = 12
                drive.drive_in(fwd)

    # If the scan was not successful
    else:
        # Turn towards left edge of map
        if box_num >= 7:
            drive.turn_ang_rel(-90)
        else:
            drive.turn_ang_rel(90)

        # Drive to left-hand edge of map
        drive.drive_in(to_box_fwd)

        # Turn towards the home
        drive.turn_ang_rel(-90)

        # Drive home
        drive.drive_in(leave_home_fwd)

    # Return to original direction, prepared for another order
    drive.turn_ang_abs(0)
        