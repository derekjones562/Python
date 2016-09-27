#!/user/bin/python
from item import Compass

class Character:
    def __init__(self, heatOn=True):
        self.isAlive=True
        self.oxygenLvl=30
        self.health = 10
        self.heat = heatOn
        self.inventory =[]

    def getOxygenLvl(self):
        if (self.oxygenLvl < 5):
            print "Oxygen is getting low. Turns left: "+self.oxygenLvl
        return self.oxygenLvl
    def addOxygen(self, amount):
        self.oxygenLvl=self.oxygenLvl+amount
    def getIsAlive(self):
        return self.isAlive
    def oneMove(self, heatOn):
        self.oxygenLvl= self.oxygenLvl-1
        self.heat=heatOn
        self.oneStepCloserToDeath()
    def oneStepCloserToDeath(self):
        if(not self.heat):
            self.health=self.health-1
        if(self.oxygenLvl<=0):
            self.health=self.health-1
        if(self.health==0):
            self.isAlive =False
    def showStats(self):
        print"Health: " +str(self.health)+"\nOxygen Level: "+str(self.oxygenLvl)
        if(not self.heat):
            print "You are cold and losing health"
    def addItem(self, item):
        self.inventory.append(item)

#me=Character()
#me.oneMove(False)
#print me.getOxygenLvl()
