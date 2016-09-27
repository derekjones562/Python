#!/usr/bin/python
import random
from room import Room

class Item:
    def __init__(self, name="item", look="its an item"):
        self.name = name
        self.look = look
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)
class Compass(Item):
    def __init__(self):
        Item.__init__(self,"compass","Strange...it the arrow always points towards the windows on the flightDeck.")
class Picture(Item):
    def __init__(self):
        Item.__init__(self, "picture", "Its a picture of the copilots family")
        self.lookatback = "LEET"
class WaterBottle(Item):
    def __init__(self):
        Item.__init__(self, "waterbottle", )
        self.full=True
class SpaceSuit(Item):
    def __init__(self):
        Item.__init__(self, "spacesuit", "Seems air tight")
        self.isBeingWorn = False
class Tools(Item):
    def __init__(self):
        Item.__init__(self, "tools", "An assortment of tools")
class OxygenTank(Item):
    def __init__(self):
        Item.__init__(self, "oxygen tank", "its a tank with what appears to be unlimited oxygen")
        self.valveOpen=False
    def openValve(self):
        self.valveOpen=True
    def closeValve(Self):
        self.valveOpen=False

class RadioAtenna:
    def __init__(self):
        self.deployed=False
        self.name="radioatenna"
        self.look ="Its a huge attena. doubt i can pick it up"
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)
class AirLockPad:
    def __init__(self, room):
        self.room =room
        self.name ="airlockpad"
        self.look = "you can use this to change the pressure in this room"
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)
    def depressurizeRoom(self):
        self.room.pressurized = False
    def pressurizeRoom(self):
        self.room.pressurized = True
class Battery:       
    def __init__(self):
        self.charged=False
        self.name = "battery"
        self.look = "has a positive and negative. be careful to not electicute yourself"
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)
    def charge(water):
        if water.full:
            self.charged=True
            
class Switch:
    def __init__(self, on):
        self.on=on
        self.name="switch"
        self.look = "you can use this"
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)
    def flipSwitch(self):
        self.on= (not self.on)
class MasterSwitch(Switch):
    def __init__(self):
        Switch.__init__(self, False)
        self.name="masterswitch"
    def flipSwitch(self, battery):
        if battery.charged:
            self.on=(not self.on)
        return self.on
class DeployRadioSwitch(Switch):
    def __init__(self, radio):
        Switch.__init__(self, False)
        self.radio = radio
        self.name="deployradioswitch"
    def flipSwitch(self, battery):
        if(battery.charged):
            self.on=(not self.on)
            self.radio.deployed=True
        return self.on
class RadioMasterSwitch(Switch):
    def __init__(self):
        Switch.__init__(self, False)
        self.name="radiomasterswitch"
    def flipSwitch(self, radioAntenna):
        if(radioAntenna.deployed):
            self.on=(not self.on)
        return self.on
class PayloadDoorsSwitch(Switch):
    def __init__(self, doorN, doorS):
        Switch.__init__(self, False)
        self.doorN = doorN
        self.doorS = doorS
        self.name ="payloaddoorswitch"
    def flipSwitch(self):
        self.on=(not self.on)
        self.doorN.opened= not self.doorN.opened
        self.doorS.opened= not self.doorS.opened
        self.doorN.entering.pressurized= not self.doorN.entering.pressurized
        self.doorS.entering.pressurized= not self.doorS.entering.pressurized
        if(not self.doorN.entering.pressurized):
            print str(self.doorN.entering)+" and "+ str(self.doorS.entering)+ " are now depressurized"
        else:
            print str(self.doorN.entering)+" and "+ str(self.doorS.entering)+ " are now pressurized"
        
        
