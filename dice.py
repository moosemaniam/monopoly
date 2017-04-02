import random
def is_double(roll):
  return(roll[2])


def random_num():
  num = random.randint(1,6)
  return num

def dice_sum(roll):
  return (roll[0]+roll[1])


dice_sides=[1,2,3,4,5,6]

# ----------------------------------------------------------------------
##
# @Description rolls a dice and returns a list
#  list element 0 and 1 contain the rolls. List element
#  2 contain information on whether or not the rolls are
#  same in number
#
# @Returns
# ----------------------------------------------------------------------
def roll_dice():
 roll=[]
 num1 = random_num()
 num2 = random_num()
 roll.append(num1)
 roll.append(num2)
 roll.append(num1==num2)
 return roll
