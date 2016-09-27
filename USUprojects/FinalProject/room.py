#!user/bin/python

#each room has 6 possible doors; north,  east, south, west, up, down
class Room:
    def __init__(self,roomName, roomString, pressure, ndoor = None ,sdoor=None,edoor=None,wdoor=None,udoor=None,ddoor=None ):
        self.name = roomName
        self.enterString = roomString
        self.pressurized = pressure
        self.north=ndoor
        self.south=sdoor
        self.east=edoor
        self.west=wdoor
        self.up=udoor
        self.down=ddoor
        self.itemList =[]
        self.inRoom=[]#things that are in the room but cant be picked up
        self.commandList=["use waterbottle on battery","look at back of picture",r'look at',r'use',r'wear', r'take\s',"take","use keypad","quit","help","inventory","look","health","go north", "go south", "go east", "go west", "go up", "go down","open door","enter code", "drop", "take"]
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)
    def addItem(self, item):
        self.itemList.append(item)
    def addObject(self, obj):
        self.inRoom.append(obj)
    def addCommand(self, command):
        for c in command:
            commandList.append(c)
    def lookAroundRoom(self):
        print self.enterString
        if not self.itemList and not self.inRoom:
            print"You don't see much else"
        else:
            strItems=""
            for i in self.itemList:
                if(i != self.itemList[0]):
                    strItems=strItems+", "
                strItems=strItems+str(i)
            strItems=strItems+"\nOther objects include "
            for i in self.inRoom:
                if(i != self.inRoom[0]):
                    strItems=strItems+", "
                strItems=strItems+str(i)
            
            print "You also see a " + strItems
    def adjRoomDepressure():
        pass
#myRoom=Room("Default")
    
