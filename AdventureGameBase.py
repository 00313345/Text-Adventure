# A text adventure game by MTW
# Original story based on "22 short films about Springfield"

# Imports and setup
import time
playerchoice = ["1","2"]

# Scene 1
print("Sunday, April 14th, 1996.")
print("You've been preparing an old family recipe roast since earlier this Sunday morning,")
print("Soon your boss will be visiting your home for lunch, and you wouldn't want to disappoint him.")
print("As you begin to slide the roast into the oven you hear someone approach the front door.")
time.sleep(1)
print("\nThe doorbell rings throughout the house.")

input("\nENTER TO CONTINUE...\n")

print("That must be him now, you close the oven door, turning the dial as you make your route through the living room to the entrance.")
print("You see your boss in front of you the moment you open the door, he seems to have brought some wine for dinner.")
print("He's dawning a blue suit, white undershirt, with a red tie this afternoon too.\n")
print('- CHALMERS: "Well Seymour, I made it, despite your directions..."')
print('\n1: Greet him')
print('2: Tell him off')

# Choice 1
response = ""
while response not in playerchoice:
  response = input("CHOICE: ")
  if response == "1":
      print("\n- SEYMOUR: Ah. Superintendent Chalmers. Welcome. -I hope you're prepared for an unforgettable luncheon.")
      print("- CHALMERS: Yeah.")
  elif response == "2":
      print("\n- SEYMOUR: Change of plans Superintendent, that roast is for me alone.")
      print("- SEYMOUR: You're not wanted here, and how dare you complain about my directions.")
      print("- CHALMERS: Seymour your disrespect is out of line.")
      time.sleep(1)
      print("- CHALMERS: You're fired.")
      print("- SEYMOUR: Oh.")
      print("\n End: A roast never ruined.")
      quit()
  else:
      print("\nEnter 1, or 2 please!")

input("\nENTER TO CONTINUE...\n")
print("You walk with Chalmers into the dining room where he promptly takes his seat as you walk into the kitchen")
print("You gasp in shock, the oven is spewing smoke from the door, you dash over and open to find your roast in a blaze of fire.")
print("- SEYMOUR: Oh egads!")
print("- SEYMOUR: My roast is ruined!")
print("You close the oven, uncertain of what to do, your boss is in your home and you couldn't dare go back out empty handed.")
print("The windows view catches your attention, there just across the street resides a Krusty Burger, Springfield's favorite fast food joint.")
print("- SEYMOUR: But what if I were to purchase fast food and disguise it as my own cooking?")
print("You chuckle to yourself about your cunning plan")

input("\nENTER TO CONTINUE...\n")
print("- SEYMOUR: Oh ho ho, Delightfully devilish, Seymour.")
print("You take off your apron, and open the window, just as you put your leg over the frame, Chalmers enters.\n")
input("\nENTER TO CONTINUE...\n")
print("- CHALMERS: Ah...")
print("- CHALMERS: SEYMOUR!!")
print("- SEYMOUR: Superintendent! I was just uh...")

# Choice 2
print('\n1: You were just letting the smoke out...')
print('2: You were just stretching your calves...')
response = ""
while response not in playerchoice:
  response = input("CHOICE: ")
  if response == "1":
      print("\n- SEYMOUR: er... just letting the smoke out of the kitchen")
      print("- CHALMERS: Smoke? From the oven? You burnt the lunch?")
      print("- SEYMOUR: Oh, I can explain uh...")
      print("- CHALMERS: And you were climbing out of the window to escape, without warning me?")
      print("- SEYMOUR: I was just er...")
      print("- CHALMERS: Seymour, I've had enough!")
      print("- CHALMERS: You, are, fired!")
      print("\n End: Fired")
      quit()
  elif response == "2":
      print("\n- SEYMOUR: I was just-uh stretching my calves on the windowsill. Isometric exercise. Care to join me?")
  else:
      print("\nEnter either 1, or 2 please!")

print("- CHALMERS: Why is there smoke coming out of your oven Seymour?")
print("- SEYMOUR: Uh- Oh. That isn't smoke. It's steam. Steam from the steamed clams we're having.")
print("You gesture circular motions with your hand, trying to sell the lie further.")
print("- SEYMOUR: Mmm, Steamed clams.")
input("\nENTER TO CONTINUE...\n")
print("Chalmers gives you a final stern stare, and turns to take his leave, the door closing behind him.")
print("You wipe the sweat off of your face, and make your way across the street to the Krusty Burger.")
print("\nAfter a short lived trip to the Krusty Burger, you make your way back through the window.")
print("You quickly place the burgers onto a tray, and push the kitchen door open into the dining room.")
input("\nENTER TO CONTINUE...\n")
print("\n- SEYMOUR: Superintendent I hope your ready for mouth watering hamburgers")
print("- CHALMERS: I thought we were having steamed clams?")

#Choice 3
print("\n1: You've misheard...")
print("2: Admit")
response = ""
while response not in playerchoice:
  response = input("CHOICE: ")
  if response == "1":
      print("\n D'oh, no. I said 'steamed hams'. That's what I call hamburgers.")
  elif response == "2":
      print("\n - SEYMOUR: Superintendent...")
      print("- SEYMOUR: To tell you the truth I've been lying to you, the roast was ruined.")
      print("- SEYMOUR: I purchased fast food in place of my own cooking.")
      print("-SEYMOUR: I just didn't want to make a complete fool out of myself.")
      print("- CHALMERS: Seymour...")
      input("\nENTER TO CONTINUE...\n")
      print("- CHALMERS: If a problem were to arise you can just tell me.")
      print("- CHALMERS: We've been working together for years, you can be honest with me.")
      print("- SEYMOUR: Ah. I'm sorry Superintendent, I didn't mean for things to go this way.")
      print("- CHALMERS: Well a meal is a meal, we can't just leave these Krusty Burgers to waste")
      print("- CHALMERS: There's always next time Seymour, don't worry about it.")
      print("End: Good honesty")
      quit()
  else:
      print("\nEnter either 1, or 2 please!")

print("- CHALMERS: You call hamburgers steamed hams?")
print("- SEYMOUR: Yes. It's a, regional dialect.")
print("- CHALMERS: Uh-huh. Uh, What region?")

#Choice 4
print("\n1: Upstate New York")
print("2: Utica")
response = ""
while response not in playerchoice:
  response = input("CHOICE: ")
  if response == "1":
      print("- SEYMOUR: Uh, upstate New York.")
      print("- CHALMERS: Really? Well I'm from Utica, and I've never heard anyone use the phrase 'steamed hams'")
      print("- SEYMOUR: Oh, not in Utica no, it's an Albany expression.")
      print("- CHALMERS: I see...")
      input("\nENTER TO CONTINUE...\n")
      print("Chalmers bites into his burger, and studys it briefly before looking back up at you.")
      print("- CHALMERS: You know these hamburgers are quite similar to the ones they have at Krusty Burger.")
      print("- SEYMOUR: Oh, no. Patented Skinner burgers, old family recipe.")
      print("- CHALMERS: Yes. and you call them steamed hams despite the fact...")
      input("\nENTER TO CONTINUE...\n")
      print("Chalmers takes the bun off of the burger and faces it's top towards you.")
      print("- CHALMERS: That they are obviously grilled.")
      print("- SEYMOUR: Ye- you know, the-")
      print("The burger's grill marks are painfully obvious, sweat rolls down your head as you stammer.")
      print("- SEYMOUR: One thing I should...")
      print("You quickly rise from your seat and push it in.")
      print("- SEYMOUR: Excuse me for one second")
      print("- CHALMERS: Of course.")
      input("\nENTER TO CONTINUE...\n")
      print("You leave through the door to the kitchen behind you, you noticed the fire has taken over.")
      print("You need to get Chalmers out soon as possible, you immediately step back out and play it off by yawning.")
      print("- SEYMOUR: That was wonderful, good time was had by all I'm pooped.")
      print("- CHALMERS: Yes, I should be-")
      print("Chalmers stands and points to the swinging door behind you to the fiery kitchen.")
      print("- CHALMERS: Good lord what is happening in there!?")
      print("- SEYMOUR: Aurora Borealis?")
      input("\nENTER TO CONTINUE...\n")
      print("- CHALMERS: Uh- Aurora borealis, at this time of year,")
      time.sleep(2)
      print("- CHALMERS: At this time of day,")
      time.sleep(2)
      print("- CHALMERS: In this part of the country,")
      time.sleep(2)
      print("- CHALMERS: Localized entirely within your kitchen.")
      input("\nENTER TO CONTINUE...\n")
      print("In the heat of the moment, you carelessly blurt out...")
      print("- SEYMOUR: Yes!")
      print("A small pause is between the two of you as you stare at eachother, Chalmers is stunned and asks...")
      print("- CHALMERS: May I see it?")
      print("You stare blankly at him for a brief moment.")
      print("- SEYMOUR: No.")
      input("\nENTER TO CONTINUE...\n")
      print("The two of you make your way to the front porch, everything is almost wrapped up before you remember mother.")
      print("She had been upstairs looking at her photos the whole time.")
      print("- MRS. SKINNER: Seymour! The house is on fire!")

#Choice 5
print ("\n1: Save mother")
print ("2: Pretend there is no fire")
response = ""
while response not in playerchoice:
  response = input("CHOICE: ")
  if response == "1":
      print("You most certainly heroically yell out")
      print("I'm coming to save you mother!")
      print("You run back into the burning home, as Chalmer yells out your name, but atleast mother will be alright.")
      print("End: Mother!")
      quit()
  elif response == "2":
      print("\n- SEYMOUR: No mother it's just the northern lights.")
      print("- CHALMERS: Well Seymour you're an odd fellow, but I must say...")
      print("Chalmers smiles and says to you:")
      input("\nENTER TO CONTINUE...\n")
      print("- CHALMERS: You steam a good ham.")
      print("As Chalmers makes his way down the street, mother calls out, and Chalmers turns back")
      print("- MRS. SKINNER: Help! Help!")
      print("You give Chalmers a grand smile and a thumbs up, as he turns away you sprint back into the house...")
      print("End: Delightfully Devilish.")
      quit()
