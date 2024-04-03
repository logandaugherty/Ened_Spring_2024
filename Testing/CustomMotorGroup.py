from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_3
from time import sleep
# from Ramp_Speed import ramp_speed_rotation

# Motor Group
# Contains all relevant functions pertaining to operation for Subtasks 1 and 2
class MotorGroup:
    # Create and store motors and sensors
    m1 = LargeMotor(OUTPUT_A)
    m2 = LargeMotor(OUTPUT_D)
    gyro = GyroSensor(INPUT_3)
    gyro.mode = GyroSensor.MODE_GYRO_ANG
    
    INCHES_TO_DEGREES = 360/(2.204724*3.14159265)

    DELTA_T = 0.02
    LEFT_MOTOR_DELAY = 0.04
    LEFT_MOTOR_DELAY_INTERVAL = LEFT_MOTOR_DELAY/DELTA_T

    # Reset motor encoders
    def reset_encoders(self):
        self.m1.reset()
        self.m2.reset()

    # Store the amount of motor degrees to allot for speeding up or slowing down
    SLOW_SPEED_DEG = 180

    def move_distance_in(self, min_speed, max_speed, distance_in, gyro_header, break_hold):
        distance_deg= distance_in * self.INCHES_TO_DEGREES
        self.move_distance_deg(min_speed,max_speed,distance_deg,gyro_header,break_hold)

    def move_distance_deg(self, min_speed, max_speed, distance_deg, gyro_header, break_hold):
        self.on_to_position(min_speed,max_speed,self.SLOW_SPEED_DEG,gyro_header)
        self.on_to_position(max_speed,max_speed,distance_deg-self.SLOW_SPEED_DEG,gyro_header)
        self.on_to_position(max_speed,min_speed,distance_deg,gyro_header,break_hold)

    # Drive to a certain rotation with a start and end speed
    def on_to_position(self, start_speed, end_speed, position_degrees, gyro_header=0, break_hold=False):
        
        # Determine the degrees between the starting and ending position
        rel_end_degrees = position_degrees - self.m1.degrees

        if rel_end_degrees == 0:
            return 

        # Determine the amount of speed to change 
        speed_per_degree = (end_speed-start_speed) / rel_end_degrees

        # Determine if the wheels are traveling forwards or backwards
        direction = rel_end_degrees > 0

        # Store the error as the distance from the target
        error_degrees = rel_end_degrees

        # i = 0
        # While the robot has not yet reached its target
        while ((error_degrees > 0 ) and direction) or ((error_degrees<0) and not direction):
            # Find the distance from the target
            error_degrees = position_degrees-self.m1.degrees

            # Determine the speed in which to run the motors
            speed = (rel_end_degrees-error_degrees)*speed_per_degree+start_speed

            realign_speed = 0
            if (self.gyro.angle - gyro_header) > 1:
                realign_speed = - 1
            elif (self.gyro.angle - gyro_header) < -1:
                realign_speed = 1


            # if i >= LEFT_MOTOR_DELAY_INTERVAL:
            # i+=1
            self.m1.on(SpeedPercent(speed-realign_speed))
            self.m2.on(SpeedPercent(speed+realign_speed))

            # Wait for sensors to update
            sleep(self.DELTA_T)

        # If the user want to brake after driving, do so
        if break_hold:
            self.stop()

    # Reset Gyroscope
    # Used at the start of each program
    def reset_gryo(self):
        self.gyro.calibrate()
        self.gyro.reset()

    # Drive to a certain rotation with a start and end speed
    def on_to_gyro_rotation(self, start_speed, end_speed, angle_degrees, break_hold=False):
        
        # Determine the degrees between the starting and ending position
        rel_end_angle = angle_degrees - self.gyro.angle

        if abs(rel_end_angle) < 2:
            return 

        # Determine the amount of speed to change 
        speed_per_degree = (end_speed-start_speed) / rel_end_angle

        # Determine if the wheels are traveling forwards or backwards
        reversed = rel_end_angle < 0

        # Store the error as the distance from the target
        error_degrees = rel_end_angle

        i = 0

        # While the robot has not yet reached its target
        while ((error_degrees > 0 ) and not reversed) or ((error_degrees<0) and reversed):
            # Find the distance from the target
            error_degrees = angle_degrees-self.gyro.angle

            # Determine the speed in which to run the motors
            speed = (rel_end_angle-error_degrees)*speed_per_degree+start_speed

            if reversed:
                speed *= -1

            self.m1.on(SpeedPercent(-speed))

            if i >= self.LEFT_MOTOR_DELAY_INTERVAL:
                self.m2.on(SpeedPercent(speed))
            i+=1

            # Wait for sensors to update
            sleep(self.DELTA_T)

        # If the user want to brake after driving, do so
        if break_hold:
            self.stop()
    
    # Stop the drive motors
    def stop(self):
        self.m1.stop()
        self.m2.stop()