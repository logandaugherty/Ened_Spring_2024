#reads barcodes vertically 
#!/usr/bin/env python3
#port 1 color sensor and port b is medium motor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
from ev3dev2.motor import MediumMotor, OUTPUT_B
import time

# Initialize the sensor and motor
sensor = ColorSensor()
liftMtr = MediumMotor(OUTPUT_B)

#code for the assigned box number
def assigned_num(numba):
    #start the movement and direct itself towards each box for subtask 3 and scan each code to try and find the assigned number and when it does the box will be picked up and dropped and point B
    print(numba)




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
    increment = -100
    for i in range(4):
        position = 0 + i * increment # Defined positions for each box
        arm_movement(position)  # Move the sensor to the position for the current box
        
        box_color = scan()
        qr_code.append(box_color)
    
    arm_movement(30,0)

    
    # Convert the QR code into a string or other format needed for further processing
    qr_code_str = ''.join(['1' if color == 'white' else '0' for color in qr_code])
    return qr_code_str

# Main logic
if __name__ == "__main__":
    qr_data = decode_qr()
    print("QR Code:", qr_data)
    # Perform actions based on the qr_data
    Sound().beep()

assigned_num(1010)

