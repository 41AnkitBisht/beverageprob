import random
hashmap = { 'beer1' : [3,7], 'beer2' : [4,8], 'beer3' : [4,9]}

class Beverage:
    def __init__(self, name, low, high):
        self.name =  name
        self.low = low
        self.high = high
        hashmap.update({self.name : [self.low, self.high]})
    #prompt for high and low
    @classmethod
    def take_input(cls,beverage):
        return cls(beverage,int(input("enter low temp:")),int(input("enter high temp:")) )

class randomtemp:
    def __init__(self):
        self.randomval = random.randrange(1,10)

class Node:
    def __init__(self, lowtemp, hightemp, boxname):
        self.lowtemp = lowtemp
        self.hightemp = hightemp
        self.boxname = boxname
        self.nextval = None

class Container:
    def __init__(self):
        self.headval = None

    def insertcontainer(self, lowtemp,hightemp, box_name):
        NewBox = Node( lowtemp,hightemp, box_name)
        if self.headval is None:
            self.headval = NewBox
            return
        BoxLoc = self.headval
        while BoxLoc.nextval:

            BoxLoc = BoxLoc.nextval
        BoxLoc.nextval = NewBox

    def addcontainer(self):
        showmenu = Container()
        showmenu.showmenu()

    def checkbox(self):
        checkval = self.headval
        newrandomval = randomtemp()

        while checkval:
            print("Current temp:" ,newrandomval.randomval,  "Temperature Range:"  ,checkval.lowtemp,  "-"  ,checkval.hightemp)
            if newrandomval.randomval < checkval.lowtemp:
                print("Message alert:", checkval.boxname,"Low Temperature")
            elif newrandomval.randomval > checkval.hightemp:
                print("Message alert :", checkval.boxname, "High Temperature ")
            else:
                print("All ok")
            newrandomval = randomtemp()
            checkval = checkval.nextval

    def showmenu(self):
        #traverse hashmap
        containername = input("enter container name:")
        available = hashmap.keys()
        print("Choose from avaiable beverages or enter new one:", available)
        beverage = input("Name of beverage:")
        if beverage in hashmap:
            recorded_low = hashmap[beverage][0]
            recorded_high = hashmap[beverage][1]
            box.insertcontainer(recorded_low, recorded_high, containername)
        else:
            Beverage.take_input(beverage)
            recorded_low = hashmap[beverage][0]
            recorded_high = hashmap[beverage][1]
            box.insertcontainer(recorded_low, recorded_high, containername)

box = Container()
box.insertcontainer(3,7,"contianer1")
box.insertcontainer(4,8,"container2")
box.insertcontainer(4,9,"container3")
box.addcontainer()
print(hashmap)
box.checkbox()
