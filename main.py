import time
weapon = False
key = False

def introScene():
  directions = ["left", "right", "forward"]
  print("You've stepped outside.")
  print("Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    match input:
      case "left":
        showEyes()
      case "right":
        showFigure()
      case "forward":
        emptyRoom()
      case "backward":
        bedroom()
      case other:
        print("You're standing still. You can't make your body move.")
        break

def returnScene():
  directions = ["yes", "no"]
  print("You went back.")
  print("I told you this was for the best.")
  time.sleep(2)
  print("You can always go home again. Do you wish to go back?")
  userInput = ""
  while userInput not in directions:
    print("yes/no")
    userInput = input()
    match input:
      case 'yes':
        bedroom()
      case 'no':
        print("Alright then. I'll help you back.")
        introScene()
      case other:
        print("You must make a choice. Yes or no.")


def showEyes():
    directions = ["right", "backward"]
    print("You see large, glowing eyes.")
    print("They're staring at you.")
    time.sleep(2)
    print("You can feel their gaze piercing your soul.")
    userInput = ""
    while userInput not in directions:
      print("Options: right/left/backwards")
      userInput = input()
    match input:
      case 'backwards':
        returnScene()
      case 'right':
        woods()
      case 'left':
        print("You can't go there. Something is blocking your path.")
      case other:
        print("Something hinders your movement. Try something else.")

def showFigure():
  print("There's someone else here.")
  action = ["Leave", "Ignore", "Fight"]
  time.sleep(2)
  print("What do you wish to do?")
  userInput = ""
  while userInput not in action:
    match input:
      case 'Leave':
        returnScene()
      case 'Ignore':
        directions: ["left", "downwards"]
        print("You decide to ignore it.")
        userInput = ""
        while userInput not in directions:
          print("Options: left/downwards")
          match input:
            case 'left':
              recovery()
            case 'downwards':
              water()
            case other:
              print("Your body isn't moving. Try something else.")
      case 'Fight':
        actions = ["Return","Lay Down","Kill yourself"]
        if weapon:
           print("You stab the figure with all your might.")
        time.sleep(2)
        print("The sound of it's limp body hitting the floor echoes in your head.")
        time.sleep(2)
        print("What will you do now?")
        while userInput not in actions:
            print("Options: Leave/Lay down/ Kill yourself")
            match input:
              case 'Leave':
                returnScene()
              case 'Lay down':
                print("You lay down next to the figure.")
                time.sleep(3)
                print("The corpse is laying in its own blood. You can feel it seeping into your clothes.")
                time.sleep(3)
                print("...")
                print("Guilt overcomes you.")
                print("You decide to lay there until you also pass away.")
                quit()
              case 'Kill yourself':
                print("You stare into the dark room, your eyes landing on the figure.")
                time.sleep(3)
                print("The air becomes thick. It's hard to breathe.")
                time.sleep(2)
                print("To end your own suffering you stab yourself in the neck.")
                quit()
              case other:
                print("You have to do something.")
        else:
          print("You have to do something")
      case other:
        print("You decide to back out of this. You don't actually want to fight it.")
        time.sleep(1)
        print("Just as you're about to turn around to leave you feel your ribs splitting open.")
        time.sleep(2)
        print("The figure wouldn't let you leave.")
        print("Your torso tears open in front of your eyes. You don't even have the chance to scream.")
        print("I told you this was a bad idea.")
        quit()

def emptyRoom():
  directions = ["right/forwards/backwards"]
  print("When you enter the room you start hearing your own heartbeat. It's eerily silent.")
  userInput = ""
  while userInput not in directions:
    match input:
      case 'right':
        introScene()
      case 'forwards':
        recovery()
      case 'backwards':
        woods()
      case other:
        print("You can't move. Try something else.")

def bedroom():
    print("You're in your room. The bed hasn't been made in months.")
def recovery():
  print("Something about this place makes you feel safe.")

def water():
  actions = ["Touch the water", "Step in", "Return"]
  global key
  print("There is a vast amount of water here.")
  print("It feels oddly calming, but it also gives you a feeling of unease.")
  userInput = ""
  while userInput not in actions:
    print("Options: Touch the water/Step in/Return")
    userInput = input()
    match input:
      case 'Touch the water':
        key = True
        print("You feel something touching your fingertips as you reach into the blank surface of the water.")
    
    
def woods():
  directions = ["right, backwards"]
  global weapon
  print("You enter an opening in the dense woods. You can only see slivers of moonlight falling through the leaves.")
  time.sleep(3)
  print("There seems to be something here.")
  print("I don't know if you should stay here. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/backwards/forward")
    userInput = input()
    match input:
      case 'backwards':
        showEyes()
      case 'right':
        emptyRoom()
      case 'forward':
        print("You see something reflecting the moonlight. It looks like a knife. You decide to take it.")
        weapon = True
      case other:
        print("You feel like you're stuck in place. Try something else.")
  
if __name__ == "__main__":
  while True:
    print("Welcome to the game.")
    print("It has been a while since you last stepped foot outside the door.")
    print("Are you sure you're ready?")
    print("Maybe you should turn back while you still can.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Oh?")
    print("Well, if you insist.")
    print("Remind me of your name again: ")
    name = input()
    print("Good luck, " +name+ ". I hope you realize I'm just trying to do what's best for you.")
    introScene()
    
else:
  returnScene()
