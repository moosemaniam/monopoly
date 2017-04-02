from dice import roll_dice,is_double,dice_sum
global turns
global box
global modulobox
global number_consecutive_doubles
global current_roll_is_double
global last_roll_was_double
global boxes
global in_jail_count
global in_jail_for_good
global in_jail_but_passing
global JAIL
global GOTOJAIL
global current_box

turns=10000000
box=1 #Box 1 is go
modulobox=40
number_consecutive_doubles=0
current_roll_is_double=False
last_roll_was_double=False
boxes=[]
in_jail_count=0
in_jail_for_good=False
in_jail_but_passing=False
JAIL=10-1
GOTOJAIL=30-1
current_box=0


def goto_to_jail():
 global turns
 global box
 global modulobox
 global number_consecutive_doubles
 global current_roll_is_double
 global last_roll_was_double
 global boxes
 global in_jail_count
 global in_jail_for_good
 global in_jail_but_passing
 global JAIL
 global GOTOJAIL
 global current_box

 #print"rolled ",roll[0],roll[1],"GOING TO JAIL ",JAIL
 current_box = JAIL
 boxes[current_box] += 1
 number_consecutive_doubles=0
 last_roll_was_double=0
 in_jail_for_good=True
 in_jail_but_passing=False

def move_to_box():
 global turns
 global box
 global modulobox
 global number_consecutive_doubles
 global current_roll_is_double
 global last_roll_was_double
 global boxes
 global in_jail_count
 global in_jail_for_good
 global in_jail_but_passing
 global JAIL
 global GOTOJAIL
 global current_box
 in_jail_for_good=False
 in_jail_count=0
 boxes[current_box] += 1
 if(current_box == JAIL):
  in_jail_but_passing=True
 if(current_box == GOTOJAIL):
   goto_to_jail()
   return
 #print"rolled ",roll[0],roll[1],"GOING TO ",current_box
 return

for i in range(0,modulobox):
  boxes.append(0)


for turn in range(0,turns):
  #print
  #print"current box",current_box
  ##print("TURN ",turn)
#Do a roll
  roll = roll_dice()

#if previous roll was double, update number_consecutive_doubles
  current_roll_is_double = is_double(roll)

  if(current_roll_is_double and last_roll_was_double):
    number_consecutive_doubles += 1
    #print("Rolled a double")
  else:
    number_consecutive_doubles=0

  last_roll_was_double = current_roll_is_double

#################NOT IN JAIL#########################
  if(in_jail_for_good!=True):
   if( number_consecutive_doubles ==3):
    #print("Rolled 3 consecutive doubles")
    goto_to_jail()
    continue

   current_box = current_box + dice_sum(roll)
   current_box = current_box % modulobox
   move_to_box()
   continue

################# IN JAIL#########################
  if(in_jail_for_good == True):
    #print "Jail time"
    in_jail_count+=1
    roll = roll_dice()


    #print "Jail turns ",in_jail_count
   #if in_jail_count == 3
    #Move out of jail and update
    if( in_jail_count == 3):
     current_box = current_box + dice_sum(roll)
     current_box = current_box % modulobox
     move_to_box()
     continue

  #if got double roll move out of jail
  #update current box count
  #reset in_jail_count
    if(is_double(roll) == True):
     current_box = current_box + dice_sum(roll)
     current_box = current_box % modulobox
     move_to_box()
     continue

  #if not got double roll
    #increment in_jail_count
    #increment current box count
    goto_to_jail()
    current_box = JAIL

total = sum(boxes)
print "Probabilities"
for i in range(0,len(boxes)):
  print "Box",i,(100.0*boxes[i])/total
