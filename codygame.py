# Team: Code Nation - Team 6
# Name: Olly, Vicky & Natalie
# Description: Cody and The mysterical Forest - Adventure Game

import sys 
import time     
from sys import exit 

aa = 2
bb = .2


def intro():
    print("One brisk evening when the moon is full and the trees whistle their songs,\n Cody (you) is walking through the forest touring his usual route.")
    time.sleep(aa) 
    print("At the stroke of midnight when the crows caw, and the animals slumber,\n you find yourself lost without any indication of where you are.")
    time.sleep(aa) 
    print("The moons reflections on the trees envelop you and the crows caw loudons until you can barely hear a thought!")
    time.sleep(aa) 
    print("You snap out of it and realise that you’re far away from home and need to get back before Breakfast,\n otherwise… well… you don’t even want to think about it!")
    time.sleep(aa)
    print() 
    print("Along your way you stumble upon a clearing in the forest.")
    time.sleep(aa) 
    print("There’s a foreboding, almost like you’re being watched from the treeline.")
    time.sleep(aa)
    print("You stop to gather your breath when you hear a low rumble.")
    time.sleep(aa) 
    print("Almost like something is rising from beneath you.")
    time.sleep(aa) 
    print("You look around and see a great big shadow, almost 20 feet high!")
    time.sleep(aa) 
    print("The shadow seems to bend over facing you and as it does you get a good look at its face- a big grinning face,\n the kind that makes you feel safe.")
    print()
    time.sleep(aa)
    print()
    sp1 = " \"My name is Mossbeard and I’m one of the tree elders that have roamed this forest since time immemorial.\n I see that you’re lost in this Mystical Forest. If you want to leave this clearing and fulfil your heart's desire,\n a riddle you will answer to get you out of this Quagmire...\""
    for charater in sp1:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    print()
    first_ans = "“What can run but never walk, has a mouth and never talks.\n Has a head but never weeps,\n has a bed but never sleeps?” \n <<< Mountain, Grandma, Forest >>>      "
    for charater in first_ans:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    first_ans = input()
    if first_ans == "Mountain" or first_ans == "MOUNTAIN" or first_ans == "mountain":
       print("Ahaaa! You guessed correctly and so you shall be free of this clearing. \nTake this Forest Key and travel yonder past here.\n It may be useful in the future...")

       path_good1()

    else:
        print()
        path_bad1()


def path_good1():
    time.sleep(aa) 
    print("You bid the Elder a fond farewell and begin to walk further, deeper into the forest.\n In the distance you hear a soft voice, almost like a baby’s cry")
    print()
    time.sleep(aa) 
    print(" As you edge closer the voice becomes louder and louder, each time in greater distress.")
    print()
    time.sleep(aa) 
    print("You see the orange glow of a fire light up beyond you. You walk closer cautiously… There!\n You see it!\n It looks like a tiny, winged creature trapped in a cage!\n It’s pulling on the bars of the cage, desperate to escape!")
    print()
    time.sleep(aa) 
    print("Dancing around the fire, gleefully at their catch, a nasty-snot-nosed Goblin!\n He stops in his tracks and smells the air…\n I think he can smell your presence..\n You cautiously step closer and the Goblins head darts to face you. ")
    print()
    
    sp2 = "\"Who’s there!! You better not be trying anything!!\n Ahhh look it’s just a tiny, helpless Kitty.\n Aren’t you cute? Wait… You can’t be serious??\n You think you can free this fairy??\n Well if you think you’re so smart then answer me this riddle!! Then and only then will I allow you to pass\"."
    for charater in sp2:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    second_good_ans = "\"I have seas without water, coast without sand, towns without people, mountains without land… What am I???\" \n <<< Moon, Compass, Map >>>   "
    for charater in second_good_ans:
        sys.stdout.write(charater)
        sys.stdout.flush()  
        time.sleep(bb)

    second_good_ans = input()
    if second_good_ans == "Map" or second_good_ans == "map" or second_good_ans == "MAP":
        print("Ahhh you’ve solved my riddle and I’ve been bested. Fine! You can have the fairy, I didn’t want it anyway…")

        path_good2()

    else: 
        print()
        path_bad2()


def path_bad1():
    print()
    time.sleep(aa)
    print("You have answered my riddle incorrectly and thus, as per the Forest Cyptid by-laws, am unable to give you this guide and prize.\nYou must continue on and leave me to slumber.\n A fond farewell, little one.")
    print()
    time.sleep(aa)
    print("With one last breath, the Elder falls back asleep and onwards you trek.\nUpon walking further into the forest, you begin to hear noises behind you, a rumbling that starts to get louder and louder.\nYou swerve to look behind you and see a shadow in the distance, it’s growing.")
    print()
    time.sleep(aa)
    print("You get the feeling that whatever the shadow is, it’s not friendly and doesn’t want you around these parts.\nYou start racing, not look where you’re going. Running straight through bramble and bushes, you may be even more lost than before.")
    print()
    time.sleep(aa)
    print("You reach what looks like the mouth of a deep and dark cave.\nYou’re hesitant to go inside but the shadowy figure behind you shows no sign of giving up their hunt of you.\nReluctantly you head into the cave.")
    print()
    time.sleep(aa)
    print("As you walk down the cave halls, crystals shimmer on the walls, lighting your way.\nYou reach the breach of the cave. It’s shimmering beauty lights up the spring - It must come straight from the source.\n Parched from the chase, you go to take a sip when you hear... ")
    print()

    sp3 = "\"Excuse me, little Kitty but we are the Thriae and we guard over this spring.\n If you have and lost you are, you must choose the correct answer…\""
    for charater in sp3:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    second_bad_ans = "\"You’ve heard me before, yet you hear me again.\n Then I die till you call me again… What am I?\"\n <<< Elder Tree, My Name, Echo >>>      "
    for charater in second_bad_ans:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    second_bad_ans = input()
    if second_bad_ans == "Echo" or second_bad_ans == "echo" or second_bad_ans == "ECHO":
        print()
        path_good1()

    else:
        print() 
        path_bad2()

def path_good2():
    print()
    sp4 = "\"Ahhh you’ve solved my riddle and I’ve been bested. Fine! You can have the fairy, I didn’t want it anyway…\""
    for charater in sp4:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    time.sleep(aa)
    print("The Goblin gathers his things and runs into a nearby cave.\n You look over at the fairy, it seems to be relieved that the Goblin has been beaten.\n You use the Forest Key on the cage and the lock clicks, swinging the heavy metal door open.\n The Fairy jumps up and begins to fly around you, basking in its newfound freedom.")
    print()
    
    sp5 = "\"You sure are a smart and wondrous Kitty!\n Thanks to you I’ve been freed and that nasty Goblin has retreated into the cave!\n As a token of my gratitude, I have a gift.\n However, the Goblin took me quite aways from where I was going.\n I have a date at the Lake of Love, so if you’d please follow me, I’ll guide you to my home!\""
    for charater in sp5:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    print("You begin to walk on a dirt path, ancient footsteps show you the way to a fork in the road.")
    print()
    time.sleep(aa)
    print("Do you turn Left or Right?")

    third_good_ans = input()
    if third_good_ans == "left" or third_good_ans == "Left" or third_good_ans == "LEFT":
        print()
        path_good3()
        path_good4()
    else:
        print()
        wrong_path()

def wrong_path():
    print()
    time.sleep(aa)
    print("You've turned right and continued down the path.\n You've plodded along so merrily that you didn't realise that you've found yourself stuck in a swamp!!! ")
    print()
    time.sleep(aa)
    print("You struggle to escape the peat but with every twist and every turn, you find yourself sinking.\n Lower and lower until all that is surrounding you is darkness...\n You find it harder to breathe and you're growing tired.")
    print()
    time.sleep(aa)
    print("You succumb to the peat... you should have just turned left...")
    print()
    time.sleep(aa)
    print("<<<<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>>>>")
    
    game_end()
    

def game_end():
    print("<<<<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>>>>")

def path_bad2():
    
    sp6 = "\"You have failed this riddle, as I suspected. Your prize for this discretion is a thousands lifetimes, trapped within the YARN OF DISASTER!\""
    for charater in sp6:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    print()
    print("You’re trapped, wrapped up in the YARN OF DISASTER, every roll yields nothing but a tighter grip.\n You begin to tire and give up, relenting that you may be trapped here forever.\n Suddenly, you hear the jovial singing of a distant thing.\n It’s growing closer- perhaps help is on its way!")
    print()
    time.sleep(aa)
    print("A happy looking Gnome appears, he’s wearing a helmet made of stone and in their hand, a pickaxe! ")
    print()
    sp7 = "\"You look like you’re in a heap of trouble! I suppose you’re going to want a hand! Well it’s not my first rodeo when it comes to string, here!\""
    for charater in sp7:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    print()
    print("The gnome helps you untangle- string has never been so troublesome…")
    print()
    sp8 = "\"Now these caves here, is tricky business… not for me, I’ve been mining here since before your grandparents were born… I can show you the way but a gnome hardly gives advice for free.\n Solve this riddle and I’ll consider showing you how to get back on the good trail.\""
    for charater in sp8:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    print()
    third_bad_ans = "\"I can't be bought, but I can be stolen with a glance.\n I'm worthless to one, but priceless to two. What am I?\"\n <<< Sleep, Love, A Good Pair of Socks >>>      "
    for charater in third_bad_ans:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    third_bad_ans = input()
    if third_bad_ans == "Love" or third_bad_ans == "love" or third_bad_ans == "LOVE":
        print()
        path_gnome_good()
    else:
        print()
        game_over()

def game_over():
    
    sp9 = "\"You have failed the riddle and that’s a shame, I quite liked you. Anyway, Forest Cryptid By-Laws decree that I cannot offer you help…\n I wish it were different but that’s how it is. Off you go now.\""
    for charater in sp9:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    
    print("You wander around the cave, turning left, then right, then left again and every which way- a deadend. You’re lost forever in the cave")
    print()
    time.sleep(bb)
    print("<<<<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>>>>")
    

def path_good3():
    print()
    time.sleep(bb)
    print("After turning left, the dirt path continues through a long and winding road.\n You reach, what may perhaps be the biggest and widest tree you’ve seen in your nine lives. Within the leaves, a wooden Treehouse sits.")
    print()
    time.sleep(bb)
    print("The Fairy flies ahead and you climb the trunk.\n At the top, the fairy shows you to a room with bottles of colourful liquids sit, old texts sit open, upon a table in the centre.\n The Fairy scans across the colourful liquids and goes “Ahaa!")
    
    sp11 = "\"Here is your prize for setting me free from that mean old Goblin. We Forest Cryptids call it ‘Magic Milk’ and its said that the drinker can gain supernormal powers.\n It’d be best to keep it close, you never know when you might need it.\""
    for charater in sp11:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

        print() 
        path_good4()

def path_good4():
    print()
    time.sleep(bb)
    print("The Fairy tells you that it needs to go to the swamp to gain entrance to the Lake of Love and you’re the only one that can help it! You accept this heroic task of love-matching and set off on your way to the Ogre’s Swamp.\n The Fairy is flying beside you, looking rather anxious to get where they’re going.")
    print()
    time.sleep(bb)
    print("The sound of a roaring snore tells you that you’re on the right track and sure enough, when you enter the swamp the thunderous snore deafens you.")
    print()
    time.sleep(bb)
    print("The Fairy flies hastily over to the Ogre and in a voice surprisingly loud for such a tiny thing, screams:")
    print()
    sp12 = "\"WAKE UP YOU SILLY OGRE, YOU CAN’T DO MUCH GUARDING WHEN YOU’RE ASLEEP!\" "
    for charater in sp12:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    print("With an arm like a loose hammer, she slams her hand right on top of the Ogre who awakes abruptly, crying from pain.")
    print()
    time.sleep(bb)
    print("The Ogre, holds its head in its arms and thrashes his leg on the ground. ")
    print()
    time.sleep(bb)
    sp13 = "\"Oh don’t be such a big baby!!” laments The Fairy.\""
    for charater in sp13:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    sp14 = "\"You hurted me on my head!!!” The Ogre babbles through tears.\""
    for charater in sp14:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    print("The Fairy, rather ashamed of her behaviour, flies over to you and says:")
    ppp = "\"I think I did a bad thing, Oh my Love will be so disappointed…Wait a second,\n I know a sure-fire cure for severe baby head- MAGIC MILK\""
    for charater in ppp:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
  
    sp15 = "\"Do you help the ogre by giving it your magic milk or do you leave it alone like a meanie?\n <<< Go on then... / No way! >>>  "
    for charater in sp15:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    magic_milk = input()
    if magic_milk == "Go on then" or magic_milk == "go on then" or magic_milk =="GO ON THEN":
        print("You give the Ogre your Magic Milk and it's shrieks with glee!\n He thanks you and tells you of a short cut to get to the Lake of Love")
        print()
        ogre_swamp_good()


    else:
        print()
        ogre_swamp_bad()


def path_gnome_good():
    print()
    time.sleep(bb)
    print("With the reluctant help of the Gnome, you exit the cave and the Gnome hands you a glass of what he called 'Magic Milk'.\n He tells you that It'll revitalise you or that it may come in handy later.\n With 'Magic Milk' in hand begin following a long and winding road.")
    

    print() 
    path_good4()

def ogre_swamp_good():
    print()
    sp16 = "\"Ahhhhh much better now, thank for the Milk, Little Kitty!\""
    for charater in sp16:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    time.sleep(bb)
    print("The Ogre glugs down the Magic Milk and sighs in relief")
    print()

    sp17 = "\"We need to get to the Lake of Love because my love is waiting for me there!\""
    for charater in sp17:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    
    sp18 = "\"I want help you Fae but only the pure of heart can open the secret passage and you donked me on my head....\""
    for charater in sp18:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    time.sleep(bb)
    print("Both the Ogre and The Fairy look at you.")
    
    sp19 = "\"You, you have a pure heart, Cody. Even though you’re lost in this forest, you have helped us all at every turn.\n If anybody can open the Passage to the Lake of Love, It’s you. Please, step on the Pedestal\""
    for charater in sp19:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    time.sleep(bb)
    print("You stand upon the pedestal the Ogre was sleep over and a bright light flashes beneath you.\n A low rumbling begins and the ground in front of you begins to open up.\n A staircase leads down into what looks like an Oasis of Pure Love. The Fairy flies down exclaimed")
    print()
    sp21 = "\"My Love, My Love, I have made it!\""
    for charater in sp21:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    time.sleep(bb)
    print("You follow Fae down and are greeted by a creature wearing a green shawl and a tall green hat. He says:")
    print()

    sp22 = "\"You have made it here to the Lake of Love and have reunited me with mine.\n You are not just a good cat, Cody but the best cat. If you’re willing, I want you to be The Great Forest Guide.\n Someone who guides lost souls through the forest, or perhaps, if they’re worthy to the Lake of Love.\""
    for charater in sp22:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    forth_good_ans = "Do you accept?\n <<< yes / no >>>  "
    for charater in forth_good_ans:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)

    forth_good_ans = input()
    if forth_good_ans == "yes" or forth_good_ans == "YES" or forth_good_ans == "Yes":
        print()
        lake_end_good()

    else:
        print()
        lake_end_bad()

def ogre_swamp_bad():
    print()
    time.sleep(bb)
    print("You decide that you’d rather keep the milk for yourself, afterall why shouldn’t you.\n You’ve helped everyone along the way and have nothing to show for it but detour after detour.\n You take the milk out and take three great big gulps, drinking it in one.")
    print()
    sp23 = "\"What a rotten little Cat you are…” The Ogre cries.\""
    for charater in sp23:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    sp24 = "\"That was horribly mean and what’s more, the Ogre won’t move so I can’t see my beloved.\""
    for charater in sp24:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    time.sleep(bb)
    print("The Fairy raises her hand and as if by magic a wand appears.")
    print()
    ssss = "\"If you want to go home, so be it!\""
    for charater in ssss:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    time.sleep(bb)
    print("She swings her arms and Cody is transported to his Home.\n A Great Big Mushroom with windows and a door. You meow and a deshevilled lady throws the door open.")

    sp27 = "\"There you are, you stinky Cat! You’re late and worse you smell of Forest Spirits.\n There’s only one punishment befitting for one such as you.\""
    for charater in sp27:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    time.sleep(bb)
    print("The Witch swings her arms over her head. With a click of her fingers, she turns you into a Clay Doll!")
    print()
    time.sleep(bb)
    print("Cody spent a millennia as a clay doll, silently watching the world change around him.\n Long after the Witch had passed and the mushroom house died.\n Nobody knows Codys name and nobody mourns him.")
    print()
    time.sleep(bb)
    print("<<<<<<<<<<<<<<<<<<<<<< YOU LOST >>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>>>>")
    
    game_end()
    exit()

def lake_end_good():
    print()
    time.sleep(bb)
    print("Cody spent a milenia guiding the lost and hungry into the caves and through the forest.\n The humans spoke of Cody as a loving God of the Forest and started a tradition of leaving Salmon out on the edges of the Forest.")
    print()
    time.sleep(bb)
    print("To this day, some believe that they see Cody, watching silently over the good people of this world.")
    print()
    time.sleep(bb)
    print("^^^^^^^^^^^^^^^^^^^^ YOU WON!! ^^^^^^^^^^^^^^^^^^^^")
    print()
    time.sleep(bb)
    print("^^^^^^^^ YOU TRULY ARE THE BEST CAT IN THE WORLD ^^^^^^^^")
    
    game_end()
    exit()

def lake_end_bad():
    print()
    time.sleep(bb)
    print("The Fairy raises her hand and as if by magic a wand appears.")
    sp28 = "\"If you want to go home, so be it!\""
    for charater in sp28:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    time.sleep(bb)
    print("She swings her arms and Cody is transported to his Home.\n A Great Big Mushroom with windows and a door.\n You meow and a deshevilled lady throws the door open.")

    sp31 = "\"There you are, you stinky Cat! You’re late and worse you smell of Forest Spirits.\n There’s only one punishment befitting for one such as you.\""
    for charater in sp31:
        sys.stdout.write(charater)
        sys.stdout.flush()
        time.sleep(bb)
    print()
    time.sleep(bb)
    print("The Witch swings her arms over her head. With a click of her fingers, she turns you into a Clay Doll!")
    print()
    time.sleep(bb)
    print("Cody spent a millennia as a clay doll,\n silently watching the world change around him. Long after the Witch had passed and the mushroom house died.\n Nobody knows Codys name and nobody mourns him.")
    print()
    time.sleep(bb)
    print("<<<<<<<<<<<<<<<<<<<<<< YOU LOST >>>>>>>>>>>>>>>>>>>>>>>")
    print("<<<<<<<<<<<<<<<<<<<<<< GAME OVER >>>>>>>>>>>>>>>>>>>>>>")

    game_end()
    exit()





print("######################################################")
print("#                                                    #")
print("#                                                    #")
print("#                                                    #")
print("#           Cody and The Mystical Forest             #")
print("#                                                    #")
print("#                                                    #")
print("#                                                    #")
print("#                                                    #")
print("#                    |\__/,|   (`\                   #")
print("#                  _.|o o  |_   ) )                  #")
print("#                 -(((---(((--------                 #")
print("######################################################")
time.sleep(aa) 
answer = input("Welcome to Cody and the Mystical Forest, would you like to play?   <yes/no>  ")
    
if answer.lower().strip() == "no":
    print("oh well.")


if answer.lower().strip() == "yes":
   time.sleep(aa) 
   answer == print()
   intro()


  