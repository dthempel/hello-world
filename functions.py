### functions

x_pos = 0
e_pos = 4
print(x_pos)

def move():
    global x_pos
    x_pos += 1

move()
print(x_pos)

def move_by(amount):
    global x_pos
    x_pos += amount


def collide_check():
    global x_pos
    global e_pos
    if x_pos == e_pos:
        return True
    else:
        return False

move_by(2)
did_collide = collide_check()

print(x_pos)
print(did_collide)