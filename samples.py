## Relational Operators II

def greater_than(x, y):
  if x > y:
    return x
  if y > x:
    return y
  if x == y:
    return "These numbers are the same"
    
def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"

print(greater_than(6,6))
print(graduation_reqs(120))

## Boolean And

def graduation_reqs(gpa,credits):
  if (credits >= 120) and (gpa >= 2.0):
    return "You meet the requirements to graduate!"
  
print(graduation_reqs(2.0,120))

## Ands and Ors

statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and (credits < 120):
    return "You do not have enough credits to graduate."
  if (gpa < 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if (gpa < 2.0) or (credits < 120):
    return "You do not meet either requirement to graduate!"
  
  print(graduation_reqs(2.0,0))

## Else

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and (credits < 120):
    return "You do not have enough credits to graduate."
  if (gpa < 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."

print(graduation_reqs(0.0,120))

## Elif

def grade_converter(gpa):
  if (gpa >= 4.0):
    return "A"
  elif (gpa >= 3.0):
    return "B"
  elif (gpa >= 2.0):
    return "C"
  elif (gpa >= 1.0):
    return "D"
  else:
    return "F"

print(grade_converter(0.5))

## Try / Except

def raises_value_error():
  raise ValueError
  
try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")
  
## Control Flow "graduation"

def applicant_selector(gpa, ps_score, ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) and (ec_count < 3):
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."

applicant_selector(2.0,100,5)

## ship calculator

def ground_shipping(weight):
  if (weight <= 2):
    cost = weight * 1.50 + 20.00
  elif (weight >2) and (weight <= 6):
    cost = weight * 3.00	+ 20.00
  elif (weight >6) and (weight <=10):
    cost = weight * 4.00	+ 20.00
  else:
  	cost = weight * 4.75 + 20.00
  
  return cost

def drone_shipping(weight):
  if (weight <= 2):
    cost = weight * 4.50
  elif (weight >2) and (weight <= 6):
    cost = weight * 9.00
  elif (weight >6) and (weight <=10):
    cost = weight * 12.00
  else:
  	cost = weight * 14.25
    
  return cost

premium_ground = 125.00

def cheap_shipping(weight):
  drone_cost = drone_shipping(weight)
  ground_cost = ground_shipping(weight)
  
  if (premium_ground < drone_cost) and (premium_ground < ground_cost):
    cheapest = "Premium ground shipping is cheapest at: $" + str(premium_ground)
  elif (drone_cost < ground_cost):
    cheapest = "Drone shipping is cheapest at: $" + str(drone_cost)
  else:
    cheapest = "Ground shipping is cheapest at: $" + str(ground_cost)
    
  return cheapest

print(cheap_shipping(4.8))
print(cheap_shipping(41.5))

## optional
print(
"The cheapest option available is $%.2f with %s shipping." 
% (cost,method)
)

## lists and combining lists
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dogs_names = zip(names,dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

## more list combine

orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']
new_orders = orders + ['lilac','iris']
broken_prices = [5, 3, 4, 5, 4] + [4]

## append

orders = ['daisies', 'periwinkle']
print(orders)
orders.append('tulips')
orders.append('roses')
print(orders)

## range

list1 = range(5, 15, 3)
list2 = range(0,40,5)

## exercise
first_names = ['Ainsley','Ben','Chani','Depak']
age = []
age.append(42)
all_ages = age + [32,41,29]
name_and_age = zip(first_names,all_ages)
ids = range(0,4)

## exercise
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]
subjects.append("compsci")
grades.append(100)
gradebook = list(zip(subjects,grades))
gradebook.append(("visarts", 93))
print(gradebook)
big_list = list(zip(last_semester_gradebook,gradebook))
print(big_list)
