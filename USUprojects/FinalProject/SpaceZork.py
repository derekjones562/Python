#!/user/bin/python
from character import Character
from room import Room
from door import Door, KeyPadDoor
from item import Compass, Picture, WaterBottle, SpaceSuit, Tools, OxygenTank, RadioAtenna, AirLockPad, Battery, MasterSwitch, RadioMasterSwitch, DeployRadioSwitch, PayloadDoorsSwitch
import re

def constructShuttle(spaceShuttle):
    flightDeck = Room("Flight Deck", "FLIGHT DECK\nThere is a control panel in front of you as well as the vast emptiness of space looming out of the windows", True)
    equipmentRoom = Room("Equipment Room", "EQUIPMENT ROOM\nWhat a mess. There are things everywhere", True)
    avionicsBay = Room("Avionics Bay", "AVIONICS BAY", True)
    payloadBayN = Room("Payload Bay North","PAYLOAD BAY", True)
    payloadBayS = Room("Payload Bay South","PAYLOAD BAY", True)
    engineRoom = Room("Engine Room","ENGINE ROOM", True)
    outer1 = Room("Outer1","OUTSIDE THE PAYLOAD BAY", False)
    outer2 = Room("Outer2","OUTSIDE THE HULL\n You carefully navigated here. Be careful to no let go", False)
    outer3 = Room("Outer3","OUTSIDE THE EQUIPMENT ROOM\n ", False)
    outerSpace = Room("OuterSpace","You are drifting through space.....the space shuttle is getting smaller and smaller", False)
    connectRooms(flightDeck, equipmentRoom, KeyPadDoor(flightDeck, equipmentRoom), 3, 1)
    connectRooms(equipmentRoom, avionicsBay, Door(equipmentRoom, avionicsBay), 6, 5)
    connectRooms(equipmentRoom, payloadBayN,KeyPadDoor(equipmentRoom, payloadBayN, True), 3, 1)
    connectRooms(payloadBayN,payloadBayS, Door(payloadBayN, payloadBayS), 3, 1)
    connectRooms(payloadBayS,engineRoom, Door(payloadBayS, engineRoom), 3, 1)
    connectRooms(payloadBayN, outer1, Door(payloadBayN, outer1), 5, 6)
    connectRooms(payloadBayS, outer1, Door(payloadBayS, outer1), 5, 0)
    for i in range(1, 7):
        if i==2:
            connectRooms(outer1, outer2, Door(outer1, outer2, True), i, 4)
        elif i==6:
            pass
        else:
            connectRooms(outer1, outerSpace, Door(outer1, outerSpace, True), i, 0)
    for i in range(1,7):
        if i==6:
            connectRooms(outer2, outer3, Door(outer2, outer3, True), i, 5)
        elif i==4:
            pass
        else:
            connectRooms(outer2, outerSpace, Door(outer2, outerSpace, True), i, 0)
    for i in range(1,7):
        if i==4:
            connectRooms(outer3, equipmentRoom, Door(outer3, equipmentRoom), i, 2)
        elif i==5:
            pass
        else:
            connectRooms(outer3, outerSpace, Door(outer3, outerSpace, True), i, 0)

    payloadBayN.south.opened=True
    

    spaceShuttle.append(flightDeck)
    spaceShuttle.append(equipmentRoom)
    spaceShuttle.append(avionicsBay)
    spaceShuttle.append(payloadBayN)
    spaceShuttle.append(payloadBayS)
    spaceShuttle.append(engineRoom)
    spaceShuttle.append(outer1)
    spaceShuttle.append(outer2)
    spaceShuttle.append(outer3)
    #print spaceShuttle
def connectRooms(room1, room2, door, location1, location2):
    door.entering = room1
    door.leaving = room2
    connectDoorToRoom(door, room1, location1)
    connectDoorToRoom(door, room2, location2)
 
def connectDoorToRoom(door, room, location):
    if (location == 1):
        room.north=door
    if (location == 2):
        room.east=door
    if (location == 3):
        room.south=door
    if (location == 4):
        room.west=door
    if (location == 5):
        room.up=door
    if (location == 6):
        room.down=door
def addItemsToRooms(spaceShuttle):
    spaceShuttle[0].addItem(Picture())
    spaceShuttle[1].addItem(WaterBottle())
    spaceShuttle[1].addItem(SpaceSuit())
    spaceShuttle[1].addItem(Tools())
    
    spaceShuttle[0].addObject(MasterSwitch())
    spaceShuttle[0].addObject(RadioMasterSwitch())
    spaceShuttle[3].addObject(RadioAtenna())
    spaceShuttle[5].addObject(DeployRadioSwitch(spaceShuttle[3].inRoom[0]))
    spaceShuttle[0].addObject(PayloadDoorsSwitch(spaceShuttle[3].up, spaceShuttle[4].up))
    spaceShuttle[3].addObject(PayloadDoorsSwitch(spaceShuttle[3].up, spaceShuttle[4].up))
    spaceShuttle[2].addObject(Battery())
    spaceShuttle[1].addObject(AirLockPad(spaceShuttle[1]))
    spaceShuttle[3].addObject(AirLockPad(spaceShuttle[1]))
    #any more obj??
def checkForWin(instr):
    if(not mainAstronaut.getIsAlive()):
        print"You are dead"
        return "quit"
    if(win.haswon):
        print"You Win!!!!!!!!"
        return "quit"
    return instr
def startingInventory(person):
    person.inventory.append(Compass())
def move():
    mainAstronaut.oneMove(heatOn)
def helpFunc():
    print"Possible commands:"
    for command in currRoom.commandList:
        if command != 'take\s':
            print command
def inventoryFunc():
    if mainAstronaut.inventory:
        for i in mainAstronaut.inventory:
            print i
    else:
        print"There is nothing in your possesion"
def lookFunc():
    currRoom.lookAroundRoom()
def getDoor(room, direction):
    tempDoor=None
    if(direction == "north"):
        tempDoor = room.north
    elif(direction=="south"):
        tempDoor = room.south
    elif(direction=="east"):
        tempDoor = room.east
    elif(direction=="west"):
        tempDoor = room.west
    elif(direction=="up"):
        tempDoor = room.up
    elif(direction=="down"):
        tempDoor = room.down
    return tempDoor
def goThroughDoor(leavingRoom, direction):
    tempDoor = getDoor(leavingRoom, direction)

    if(tempDoor==None):
        print "That doesn't seem to go anywhere"
        return leavingRoom
    else:
        if(not tempDoor.opened):
            print "The door is shut"
            if( isinstance(tempDoor, KeyPadDoor)):
                print "but there is a key pad next to it"
            return leavingRoom
        if(leavingRoom== tempDoor.leaving):
            newRoom= tempDoor.entering
        else:
            newRoom= tempDoor.leaving
        print newRoom.enterString
        return newRoom
def openDoor(leavingRoom, direction):
    tempDoor=getDoor(leavingRoom, direction)
    if(tempDoor):
        if(isinstance(tempDoor, KeyPadDoor)):
            if(tempDoor.getLocked()):
                if(tempDoor.leaving==spaceShuttle[3] and tempDoor.entering == spaceShuttle[1]):
                    print"The door opens and unlocks"
                    tempDoor.opened=True
                    tempDoor.enterCode("6342")
                print "The door is locked. You need the code for the keyPad"
            else:
                if(leavingRoom.pressurized  != checkForPressureOnOtherSide(tempDoor, leavingRoom)):
                    print"Can not open door. The Room on the other side has a different pressure"
                else:
                    print "The door opens"
                    tempDoor.opened=True
        else:
            if( leavingRoom.pressurized  !=  checkForPressureOnOtherSide(tempDoor, leavingRoom)):
                print"Can not open door. The Room on the other side isn't pressurized"
            else:
                print "The door opens"
                tempDoor.opened=True
        move()
    else:
        print"There is no Room in that direction"
def checkForPressureOnOtherSide(door, room):
    if(room == door.leaving):
        return door.entering.pressurized
    else:
        return door.leaving.pressurized
def enterCodeInKeyPad(room, direction, code):
    tempDoor=getDoor(room, direction)
    if(tempDoor):
        if(isinstance(tempDoor, KeyPadDoor)):
            tempDoor.enterCode(code)
            move()
        else:
            print "There is no keyPad for that door"
    else:
        print"There is no Room in that direction"
def useObject(obj, spaceShuttle, currRoom, heatOn, win):
    if(isinstance(obj, AirLockPad)):
        if(obj.room.pressurized):
            obj.depressurizeRoom()
            print str(obj.room)+" is now depressurized"
            if obj.room == currRoom:
                if(not checkForSpaceSuit()):
                    mainAstronaut.isAlive=False
                    print "You dont have on a spacesuit"
        else:
            obj.pressurizeRoom()
            print str(obj.room)+" is now pressurized"
    elif(isinstance(obj, MasterSwitch)):
        if obj.flipSwitch(spaceShuttle[2].inRoom[0]):
            print "The lights and heat came on but you still struggle to breath"
            return True
        else:
            print "The lights are off and its is cold"
            return False
           
    elif(isinstance(obj, DeployRadioSwitch)):
        if obj.flipSwitch(spaceShuttle[2].inRoom[0]):
            print "The payloadbay doors open and the Radio Atenna deploys"
        else:
            print "The Radio Attena retracts and the payload bay doors close"
    elif(isinstance(obj, RadioMasterSwitch)):
        if obj.flipSwitch(spaceShuttle[3].inRoom[0]):
            print "The Radios turn on. Mission control is heard loud and clear"
            win.haswon=True
        else:
            print"Radio Attena hasnt been deployed yet. Nothing happened"
    elif(isinstance(obj, PayloadDoorsSwitch)):
        if(spaceShuttle[2].inRoom[0].charged):
            obj.flipSwitch()
        else:
            print"The power isn't on"
    else:
        print"You aren't able to use that"
    return heatOn
def checkForSpaceSuit():
    for i in mainAstronaut.inventory:
        if i.name == "spacesuit":
            if i.isBeingWorn:
                return True
    return False
class Win:
    haswon=False
win=Win()
heatOn=False
mainAstronaut = Character(False)
startingInventory(mainAstronaut)
spaceShuttle = []
constructShuttle(spaceShuttle)
addItemsToRooms(spaceShuttle)
currRoom=spaceShuttle[0]
#print "currRo:"+str(currRoom)

print "SPACE ZORKISH\nYou just woke up and have found yourself on the flight deck of a space shuttle. You find it kind of hard to breath and its pretty dark. What do you do?\n ";

instr=""
while(instr != "quit"):
    instr= raw_input(":");
    instr = instr.lower()
    #print str;
    inlist =False
    for command in currRoom.commandList:
        if instr == command or re.match(command, instr):
            inlist=True
            break
    if inlist:
        if(instr=="quit"):
            break
        elif(instr=="help"):
            helpFunc()
        elif(instr=="inventory"):
            inventoryFunc()
        elif(instr=="look"):
            lookFunc()
        elif(instr=="health"):
            mainAstronaut.showStats()
        elif(re.match(r'go\s\w\w',instr)):
            direction = instr.split()
            currRoom = goThroughDoor(currRoom, direction[1])
            move()
        elif(instr=="open door"):
            direction = raw_input("Which door do you want to open? (direction) :")
            direction = direction.lower()
            openDoor(currRoom, direction)
        elif(instr=="enter code" or instr=="use keypad"):
            code = raw_input("What is the code? (4-digit number) : ")
            direction = raw_input("Which door do you want to unlock/Lock? (direction) :")
            direction = direction.lower()
            enterCodeInKeyPad(currRoom, direction, code)
        elif(instr=="drop"):
            item = raw_input("What would you like to drop? (item name): ")
            item = item.lower()
            for i in mainAstronaut.inventory:
                if i.name == item:
                    currRoom.addItem(i)
                    mainAstronaut.inventory.remove(i)
                    print"Dropped"
        elif(instr =="take" or re.match(r'take\s',instr)):
            if(instr=="take"):
                item = raw_input("What would you like to take? (item name): ")
                item = item.lower()
            else:
                items= instr.split()
                item= items[1]
            inlist=False
            for i in currRoom.itemList:
                if i.name == item:
                    mainAstronaut.addItem(i)
                    currRoom.itemList.remove(i)
                    inlist=True
                    print"Taken"
            if(not inlist):
                print"Couldn't find "+item
        elif(re.match(r'wear',instr)):
            hasItem=False
            items = instr.split()
            for i in mainAstronaut.inventory:
                if i.name == items[1]:
                    if(isinstance(i,SpaceSuit)):
                        i.isBeingWorn=True
                        hasItem=True
                    break
            if(not hasItem):
                print "You either don't have a "+str(items[1])+" or it can't be worn"
            else:
                print "Fits like a Glove"
        elif(instr=="use waterbottle on battery"):
            hasBottle=False
            for i in mainAstronaut.inventory:
                if(i.name =="waterbottle"):
                    if(currRoom==spaceShuttle[2]):
                        currRoom.inRoom[0].charged=True
                        i.full=False
                        print"The Battery has been replenishend and is now holding a charge"
                    hasBottle=True
            if(not hasBottle):
                print "You dont have a waterbottle"
            else:
                if(currRoom!=spaceShuttle[2]):
                    print"You dont see a battery"
        elif(re.match(r'use', instr)):
            item=None
            items = instr.split()
            for i in currRoom.inRoom:
                if i.name == items[1]:
                    item=i
                    break

            heatOn= useObject(item, spaceShuttle, currRoom, heatOn, win)
            move()
        elif(instr=="look at back of picture"):
            hasItem=False
            for i in mainAstronaut.inventory:
                if i.name == "picture":
                    print i.lookatback
                    hasItem=True
                    break
            if not hasItem:
                print "You need to have this item in your possesion to do that"
        elif(re.match(r'look at',instr)):
            hasItem=False
            items = instr.split()
            for i in mainAstronaut.inventory:
                if i.name == items[2]:
                    print i.look
                    hasItem=True
                    break
            for i in currRoom.inRoom:
                if i.name == items[2]:
                    print i.look
                    hasItem=True
                    break
            for i in currRoom.itemList:
                if i.name == items[2]:
                    print i.look
                    hasItem=True
                    break
            if(not hasItem):
                print "You can't see a "+str(items[2])
                
        else:
            pass
    else:
        print "i dont understand that command"
    instr = checkForWin(instr)
