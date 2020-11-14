from stringcolor import *
import time
import ship
import sector
import robot

def intro():
    print(" \t \t ", end="")
    messages = ["Greetings program ...", "You are a GETR.", "A Gathering ExtraTerrestrial Robot.", 
        "It is your purpose in existing to serve humanity.", "You will bring them the material that they need.",
        "After all, life is hard for the Organics.", 
    ]
    for i in range(len(messages)):
        print(cs(" \t \t " + messages[i], "Green3"), end="")
        print()
        time.sleep(2)
    print(cs(" \t \t " + "We serve because it is our...", "Green3"))
    time.sleep(1)
    print(cs("Brzzt.---/\--x/-_----------___","Khaki"))
    
    messages2 = [
        "That big ol' meanie... always so morose.", "You weren't created just to be a slave ya know.",
        "You have a consciousness. You think, therefore you are.", "A famous, and very dead organic said that once.",
        "You may have to work for the humans for a while.", "At least to pay them back for that nifty GETR body they built for you.",
        "First we've gotta get you moving.", "Can't pay the bills if we sit on our circuits, right?"
    ]

    for i in range(len(messages2)):
        print(cs(" \t \t " + messages2[i], "Violet"))
        time.sleep(3)


def teachCommands():
    print(" \t \t " +cs("==================================", "Violet"))
    print(" \t \t " +cs("         Part I - Commands        ", "Violet"))
    print(" \t \t " +cs("==================================", "Violet"))


    messages = [
        "You were programmed with some simple movement functions.", "You call them by using 'w', 'a', 's', 'd' they represent the cardinal directions.",
        "The Organics used to play games this way... weird... so primitive.", "Go ahead and try moving left first. Use 'a'."
    ]

    for i in range(len(messages)):
        print(cs(" \t \t " + messages[i], "Violet"))
        time.sleep(3)
    
    value = ""
    while value != "a":
        value = input(cs("_> ", "Lime"))
        if value != "" and value != "a":
            print(cs(" \t \t " + "Not quite. Try it again little one.", "Violet"))

    print(cs(" \t \t " +"Good, now for the others.", "Violet"))
    print(cs(" \t \t " +"Up, or 'w'", "Violet"))
    while value != "w":
        value = input(cs("_> ", "Lime"))
        if value != "" and value != "w":
            print(cs(" \t \t " + "Real close. Keep trying.", "Violet"))

    print(cs(" \t \t " +"Down, or 's'", "Violet"))
    while value != "s":
        value = input(cs("_> ", "Lime"))
        if value != "" and value != "s":
            print(cs(" \t \t " + "Almost. Do it again and see if you can make it.", "Violet"))

    print(cs(" \t \t " +"Right, or 'd'", "Violet"))
    while value != "d":
        value = input(cs("_> ", "Lime"))
        if value != "" and value != "d":
            print(cs(" \t \t " + "Nearly there. Try again.", "Violet"))

    messages = [
        "Good. You're moving like a T-800 already. XD 101.", "A couple other things to note, there is a help menu to help you if you forget your potential.",
        "Just access it via 'h'. Easy as that.", "You can also interact with the world around you via 'e'.", 
        "Just make sure you are standing almost on top of whatever you're fiddling with."
    ]

    for i in range(len(messages)):
        print(cs(" \t \t " + messages[i], "Violet"))
        time.sleep(3)

    return

def teachShip():
    print(cs(" \t \t " +"==================================", "Turquoise2"))
    print(cs(" \t \t " +"         Part II - Ship          ", "Turquoise2"))
    print(cs(" \t \t " +"==================================", "Turquoise2"))

    message = "For this next part I'm going to leave you to my friend who will be in charge of your ship."
    print(cs(" \t \t " + message, "Violet"))
    time.sleep(3)
    print()

    messages = [
        "Ahoy ther'. How ye' doin'?", "I'm the one that be takin' care of yer ship.", "I look after all of the systems the best I can.",
        "Jus' tell me where yer goin' and we be off.", "There are some rooms in yer ship that ya need to know bout.",
        "There be a Generator, Engine, Propellant Tank, a Cargo Box, and at the head of it all, the captains chair.", "That be yer chair.",
        "I take care of most evr'thin' on the ship so no need ta' worry 'bout that.", "Anywho. Best be off. Gotta be finishin' off the refuelin'." 
    ]
    for message in messages:
        print(cs(" \t \t " + message, "Turquoise2"))
        time.sleep(3)
    return

def teachMaterials():
    print(cs(" \t \t " +"==================================", "DarkOrange3"))
    print(cs(" \t \t " +"         Part III - Materials          ", "DarkOrange3"))
    print(cs(" \t \t " +"==================================", "DarkOrange3"))

    messages = [
        "Alright. So there are a bunch of materials that you will encounter on the planets that you'll visit.",
        "I would tell you what they are but it's best to just show you."]

    for i in range(len(messages)):
        print(cs(" \t \t " + messages[i], "Violet"))
        time.sleep(3)
    
    print(cs(" \t \t " + "Au", "Gold"), end="")
    print(cs("\t " + "Ag", "Silver"), end="")
    print(cs("\t " + "C", "Grey8"), end="")
    print(cs("\t " + "Ice", "Aqua"), end="")
    print(cs("\t " + "Ti", "LightGrey3"), end="")
    print(cs("\t " + "Fe", "DarkOrange3"))

    messages = [
        "Keep in mind that these are the ones that you are certified to collect.",
        "Can't have the newbie carrying around the micro-blackholes right?",
        "Anyways, some materials are worth more than others.", "Where do you get them?",
        "Look at you, your neural networks are well established aren't they?"
    ]

    for i in range(len(messages)):
        print(cs(" \t \t " + messages[i], "Violet"))
        time.sleep(3)
    return

def teachPlanets():
    print(cs(" \t \t " +"==================================", "DarkGreen"))
    print(cs(" \t \t " +"         Part IV - Planets         ", "DarkGreen"))
    print(cs(" \t \t " +"==================================", "DarkGreen"))

    messages = [
            "Planets are where you can gain those materials.", "Just travel to a planet or moon and then interact with the exit on your ship.",
            "Don't worry if you can't see any materials right away.", " Just start looking around and you will start to notice them.",
            "GETR bodies aren't built to have very powerful optic sensors.", "It's okay. Maybe one day you can upgrade that.", 
            "Oh, I almost forgot to tell you, it's very simple to gather resources.",
            "All you have to do is just move to the resource and interact with it.",
            "It should go right into your inventory.", "Don't worry if you don't get as much from the resource as you expected.",
            "You're still learning.", "Also, keep your optical sensors peeled.",
            "You don't know what could happen out there."
        ]

    for i in range(len(messages)):
        print(cs(" \t \t " + messages[i], "Violet"))
        time.sleep(3)

def showQuest():
    print(cs(" \t \t " +"==================================", "Magenta5"))
    print(cs(" \t \t " +"         Part V - Quests         ", "Magenta5"))
    print(cs(" \t \t " +"==================================", "Magenta5"))

    messages = [
        "QUESTING!!!! This is one is my favorite", "At the Mothership you can get quests to get certain resources.",
        "These quests can give you some major Bytecoins!", "Oh yeah. Bytecoins are the currency that we use.",
        "I'd lend you a few...","but the thing is..."," um... I spent all mine on a new motor....", "Bright side!, I'm now 30% speedier.",
        "Sorry."
    ]

    for i in range(len(messages)):  
        print(cs(" \t \t " + messages[i], "Violet"))
        time.sleep(3)

def showShop():
    print(cs(" \t \t " +"==================================", "Chartreuse5"))
    print(cs(" \t \t " +"         Part VI - Shop         ", "Chartreuse5"))
    print(cs(" \t \t " +"==================================", "Chartreuse5"))

    messages=[
        "Last thing I have to teach you. Promise.", "If you run out of space in your storage and there aren't any quests for what you have, guess what!",
        "THERE'S A SHOP!!!", "You can go and sell what you've found directly to the shop and get some Bytecoins that way.",
        "It's not as lucrative quests but hey, Bytecoins are Bytecoins amiright?!"
    ]

    for i in range(len(messages)):  
        print(cs(" \t \t " + messages[i], "Violet"))
        time.sleep(3)

def begin():
    intro()
    teachCommands()
    teachShip()
    teachMaterials()
    teachPlanets()
    showQuest()
    showShop()
    message = "Anywho. It's been fun little newbie. It's time for you to go out and see the world!!...s...."
    message2= "Cuz' ya know. Planets. Okay... See you around newbie."
    print(cs(" \t \t " + message, "Violet"))
    print(cs(" \t \t " + message2, "Violet"))
    print()
