## control flow

is_game_over = False
p0_pos = 1
e0_pos = 2
e1_pos = 0
end_pos = 10

while not is_game_over:
    print(p0_pos)
    print(e0_pos)

    if p0_pos == e0_pos:
        print("You've lost!")
        is_game_over = True
    elif p0_pos >= end_pos:
        print("You've won!")
        is_game_over = True
    else:
        p0_pos += 3
        e0_pos += 1


