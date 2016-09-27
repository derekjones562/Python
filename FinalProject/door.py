#!/user/bin/python
from room import Room

class Door:
    def __init__(self, enterRoom, exitRoom, opened=False):
        self.entering = enterRoom
        self.leaving = exitRoom
        self.opened =opened
    def __str__(self):
        return "e: "+str(self.entering)+"\nl: "+str(self.leaving)
    def __repr__(self):
        return str(self)

class KeyPadDoor(Door):
    def __init__(self, enterRoom, exitRoom,opened=False, isLocked=False, setCode="6342"):
        Door.__init__(self, enterRoom, exitRoom, opened)
        self.__locked =isLocked
        self.__unlockCode =setCode
    def getLocked(self):
        return self.__locked
    def __lock(self):
        self.__locked=True
    def __unLock(self):
        self.__locked=False
    def enterCode(self, code):
        #print code
        #print self.__unlockCode
        if(code==self.__unlockCode):
            if(self.__locked==True):
                self.__locked=False
                print"The keypad beeps then flashes: UNLOCKED"
            else:
                self.__locked=True
                self.opened=False
                print"The door closes infront of you and the keypad beeps"
        else:
            print "The KeyPad flahes: WRONG CODE"


#tmp = keyPadDoor(Room("re"),Room("ter"))
#print tmp.locked
