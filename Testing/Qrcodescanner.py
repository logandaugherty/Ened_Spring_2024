#reads barcodes vertically 
#!/usr/bin/env python3
#port 1 color sensor and port b is medium motor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
import time
from time import sleep
from ev3dev2.motor import MediumMotor, LargeMotor, SpeedPercent, OUTPUT_B,OUTPUT_D,OUTPUT_A
from ev3dev2.sound import Sound



# Initialize the sensor and motor
sensor = ColorSensor()
liftMtr = MediumMotor(OUTPUT_B)
driveLMtr = LargeMotor(OUTPUT_D)
driveRMtr = LargeMotor(OUTPUT_A)
speaker = Sound()
#code for the assigned box number
#cap off list to the first four numbers 
#destroy 4 numbers from the final list in decode_qr
def assigned_num(numba):
    #move toward the box then do decode_qr()
    if decode_qr() == numba:
        #mechanism to lift the box if it equals the assigned number
        liftMtr.reset()
        liftMtr.on_to_position(-100,550,True)
        sleep(0.125)

        driveLMtr.on(-20,True,False)
        driveRMtr.on(-20,True,False)
        sleep(1)
        driveLMtr.on(20,True,False)
        driveRMtr.on(20,True,False)
        sleep(1.3)
        driveLMtr.stop()
        driveRMtr.stop()

        liftMtr.on_to_position(100,100,True)
        sleep(5)
        #move 180 degrees to go back to the line then move 90 again to bring to point B
    else:
        print("placeholder")
        #move 180 degrees to go back to the line then move 90 again to bring to point B
    return 0





# interpreting the color
def scan():
    intensity = sensor.reflected_light_intensity
    # Using 30 for distinguishing between black and white
    if intensity < 30:
        return 'black'
    else:
        return 'white'
    

# Function to move the sensor to the next box using the medium motor
def arm_movement(position):
    # Use on_to_position to move the sensor to the exact position for the next box
    # The first parameter is the speed, and the second parameter is the target position
    liftMtr.on_to_position(30, position)
    time.sleep(0.5)  # Wait a bit for the movement to stabilize

# Function to scan 4 boxes and decode the QR code
def decode_qr():
    qr_code=[]
    liftMtr.reset()
    increment = 115
    
    for i in range(4):
        position = 0 + i * increment # Defined positions for each box
        arm_movement(position)  # Move the sensor to the position for the current box
        
        box_color = scan()
        qr_code.append(box_color)
    
    arm_movement(0)
    

    
    # Convert the QR code into a string or other format needed for further processing
    qr_code_str = ''.join(['1' if color == 'white' else '0' for color in qr_code])
    print(qr_code_str)
    speaker.speak(qr_code_str)
    
    return qr_code_str



