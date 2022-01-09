class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate_left(self):
        self.x, self.y = self.y, -self.x

    def rotate_right(self):
        self.x, self.y = -self.y, self.x

    def add(self, vec2d):
        self.x += vec2d.x
        self.y += vec2d.y

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # if the instructions are repeated to infinity, does the robots position NOT approach infinity?
        
        position = Vec2d(0, 0)
        direction = Vec2d(1, 0)
        goStraight = "G"
        turnLeft = "L"
        turnRight = "R"
        
        

        # collaspe instructions into a movement vector, and the resulting normal vector
        for instruction in instructions:
            if instruction == goStraight:
                position.add(direction)
            elif instruction == turnLeft:
                direction.rotate_left()
            elif instruction == turnRight:
                direction.rotate_right()

        # If we end back up at our starting position our ending direction doesn't matter
        if position.x == 0 and position.y == 0:
            return True
        
        # If we have a new direction we will end up going in a circle or doing an about face
        if not(direction.x == 1 and direction.y == 0):
            return True

        # We've moved, and are in the same direction
        # We can expect to have the same movement forever.
        return False

            

        
