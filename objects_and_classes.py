### objects and classes

### objects have "state" and "behaviour" (methods)

# fields = variables of an object
# methods = functions of an class/object
# constructors = special call to methods?

class GameCharacter:

    speed = 5

    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amt, by_y_amt):
        self.x_pos += by_x_amt
        self.y_pos += by_y_amt

# instantiate

player = GameCharacter("Doug", 50, 100, 100, 100)

print(player.name)

player.name = "Bob"

print(player.name)

player.move(100,100)

print(player.x_pos,player.y_pos)
