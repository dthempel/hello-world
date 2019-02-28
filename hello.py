# input_name = input("Enter a name: ")
# output_text = "Hello, " + input_name

# print(output_text)

x_pos = 5
speed = 2.5
is_game_over = False
character_name = "Doug"

print(type(x_pos))

# % modulus operator = remainder
# // floor operator = number of divisions

test = 12 % 5
print(test)

floor = 22 // 5
print(floor)

x_pos = x_pos + 5
# same as
x_pos += 5

## conditionals mostly same as Perl
# != not equal
# == is equal

print(5 == 2)

# collections
# tuples, arrays/lists, dictionaries

width = 100
height = 200

size = (100,200)
new_size = size + (300,)

print(size[0])
print(new_size)

print(len(size))  #number of elements
print(max(size))
print(min(size))

print(100 in size)

## array/list

movement = [5, -2, -3, 4, -1]

print(movement[2])

movement[2] = 3

print(movement[2])

movement.append(-5) ## add to end of array
movement.remove(-2) ## remove actual value not array reference

## dictionaries

starting_positions = {'p0':50,'p1':100,'p2':150}

print(starting_positions['p2'])
print(starting_positions.keys())
print(starting_positions.values())

      
