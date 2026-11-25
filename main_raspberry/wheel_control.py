import math
from gpiozero import Robot

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angular = 0
class WheelControl:
    def __init__(self,robot):
        self.robot = robot
        self.position = None
        self.max_error_count = 50
        self.goal_threshold = 5
        self.forward_p = 0.5
        self.angular_p = 0.5
    def move_wheel(self,forward = 0,curve_right=0):
        forward = max(-1,min(1,forward))
        curve_right = max(-1,min(1,curve_right))
        if forward == 0 and curve_right == 0:
            self.robot.stop()
        if forward > 0:
            if curve_right > 0:
                self.robot.forward(speed = forward,curve_right = curve_right)
            else:
                self.robot.forward(speed = forward,curve_left = -1 * curve_right)
        elif forward < 0:
            if curve_right > 0:
                self.robot.backward(speed = forward,curve_right = curve_right)
            else:
                self.robot.backward(speed = forward,curve_left = -1 * curve_right)
        else:
            if curve_right > 0:
                self.robot.right(speed = curve_right)
            else:
                self.robot.left(speed = -1 * curve_right)
        
    def set_position(self,is_None,x,y,angular):
        if is_None:
            self.position = None
        else:
            self.position = Position(x,y,angular)
    def get_distance(self,x1,x2,y1,y2):
        return math.pow((x2 - x1) ** 2 + (y2 - y1) ** 2 )
    def get_target_direction(self,x1,x2,y1,y2):
        return math.arctan2(y2 - y1,x2 - x1)
    def go_point(self,destination):
        error_count = 0
        while True:
            if self.position is None:
                print("robot is lost!")
                error_count += 1
                if self.max_error_count <= error_count:
                    print("Maximum error count exceeded. Stopping movement.")
                    self.robot.stop()
                    return -1
                continue
            distance =  self.get_distance(self.x,destination.x,self.y,destination.y)
            target_direction = self.get_target_direction(self.x,destination.x,self.y,destination.y)
            if distance < 5:
                print("robot goal!")
                return 0

            angular_diff = self.angular - target_direction
            if abs(angular_diff) > math.pi/4:
                self.move_wheel(distance * self.forward_p,angular_diff * self.angular_p)
            else:
                self.move_wheel(0,angular_diff)



                