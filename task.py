import random as rnd


class Squad:
    _countOfDeathsSol=0
    _countOfDeathsDrones=0
    _countOfDeathsVeh=0
    def __init__(self,name):
        self._name=name
        self._units=[]
        k=rnd.randint(0,7)
        for i in range(8):
            a=Solider()
            self._units.append(a)
        self._units[k]=Solider(IsCommander=True)
        for i in range(4):
            a=Drone()
            self._units.append(a)
        for i in range(2):
            a=Vehicle()
            self._units.append(a)
    def ReportHealth(self):
        SolHealth = [i for i in self._units if type(i) is Solider]
        DroneHealth = [i for i in self._units if type(i) is Drone]
        VehicleHealth = [i for i in self._units if type(i) is Vehicle]
        SolHealth=[i for i in SolHealth if i.Report()[0]>0]
        DroneHealth=[i for i in DroneHealth if i.Report()[0]>0]
        VehicleHealth=[i for i in VehicleHealth if i.Report()[0]>0]
        return [len(SolHealth),len(DroneHealth),len(VehicleHealth)]

        
    
    def ReportPosition(self):
        #This function returns how much of units are in the area of enemy
        SolPos = [i for i in self._units if type(i) is Solider]
        DronePos = [i for i in self._units if type(i) is Drone]
        VehPos = [i for i in self._units if type(i) is Vehicle]
        SolPos=[i for i in SolPos if i.Report()[1]>=200]
        DronePos=[i for i in DronePos if i.Report()[1]>=200]
        VehPos=[i for i in VehPos if i.Report()[1]>=200]
        return [len(SolPos),len(DronePos),len(VehPos)]

    def NumOfFinalPositions(self):
        #This function returns the all count units, that's are in the area of enemy
        return len(self.ReportPosition())
    
    def NumOfDeaths(self):
        #This function returns number of deaths for each unit
        return [self._countOfDeathsSol,self._countOfDeathsDrones,self._countOfDeathsVeh]

    def PrintReport(self):
        print(f"On squad {self._name} leave {self.ReportHealth()[0]} soliders, {self.ReportHealth()[1]} drones, {self.ReportHealth()[2]} vehicles")
        print(f"On squad {self._name} {self.ReportPosition()[0]} soliders on the enemies area, {self.ReportPosition()[1]} drones on the enemies area,{self.ReportPosition()[2]} vehicles on the enemy area")
        print(f"Is death on squad {self._name}: The soliders {self.NumOfDeaths()[0]}, the drones {self.NumOfDeaths()[1]}, vehicles {self.NumOfDeaths()[2]}")
        self.AboutPosition()
    def Bomb(self):  
        for i in self._units:
            if i.Touch():
                if type(i) is Solider:
                    self._countOfDeathsSol+=1
                    if i.IsCommander() and self._countOfDeathsSol<7:
                        k=rnd.randint(0,7-self._countOfDeathsSol)
                        self._units[k].SetCommander()
                if type(i) is Drone:
                    self._countOfDeathsDrones+=1
                if type(i) is Vehicle:
                    self._countOfDeathsVeh+=1
                self._units.remove(i)
    def Move(self):
        for units in self._units:
            units.Move() 
    def PrintUnitsCount(self):
        print(len(self._units))

    def AboutPosition(self):
        SolPos = [i for i in self._units if type(i) is Solider]
        DronePos = [i for i in self._units if type(i) is Drone]
        VehPos = [i for i in self._units if type(i) is Vehicle]
        AheadSol = [i for i in SolPos if i.Report()[1]>100]
        AheadDrone = [i for i in DronePos if i.Report()[1]>100]
        AheadVeh = [i for i in VehPos if i.Report()[1]>100]
        print(f"{len(AheadSol)} soliders ahead of 100m, {len(AheadDrone)} drones ahead of 100m, {len(AheadVeh)} vehicles ahead of 100m")
        print(f"{len(SolPos)-len(AheadSol)} soliders near of 100m, {len(DronePos)-len(AheadDrone)} drones near of 100m, {len(VehPos)-len(AheadVeh)} vehicles near of 100m")


class Unit:
    def __init__(self):
        self._Health=100
        self._IsDead=False
    def IsDead(self):
        return self._Health==0
    def Report(self):
        return [self._Health,self._position]
    def Move(self):
        self._position+=self._v
    
    
class Solider(Unit):
    _v=1
    def __init__(self,IsCommander=False):
        super().__init__()
        self._position=rnd.randint(0,50)
        self._IsCommander = IsCommander
    def SetCommander(self):
        self._IsCommander=True
    def IsCommander(self):
        return self._IsCommander
    #using the probability death of solider probOfDeath=1/8
    def Touch(self):
        n = rnd.randint(0,7)
        return n==0

class Drone(Unit):
    _v=12
    def __init__(self):
        super().__init__()
        self._position=rnd.randint(0,15)
    _probDeath = 1/7
    #using the probability death of drone probOfDeath=1/7
    def Touch(self):
        n = rnd.randint(0,6)
        return n==0

class Vehicle(Unit):
    _v=10
    def __init__(self):
        super().__init__()
        self._position=rnd.randint(0,15)
    _probDeath = 1/6
    #using the probability death of vehicle probOfDeath=1/6
    def Touch(self):
        n = rnd.randint(0,5)
        return n==0
 

def Play():
    Unit1 = Squad("Arm")
    Unit2 = Squad("Isr")
    Unit3=Squad("Rus")
    i=1
    while True:
        if sum(Unit1.NumOfDeaths())+sum(Unit2.NumOfDeaths())+sum(Unit3.NumOfDeaths())==42:
            print("Lost")
            break
        elif sum([Unit1.NumOfFinalPositions(),Unit2.NumOfFinalPositions(),Unit3.NumOfFinalPositions()])>=42*70/100:
            print("Win")
            break
        else:                
            if i%5==0:
                Unit1.Bomb()
                Unit2.Bomb()
                Unit3.Bomb()
            if i%10==0:
             print("The game is continued\n")
             Unit1.PrintReport()
             input()
             Unit2.PrintReport()
             input()
             Unit3.PrintReport()
             continue
        Unit1.Move()
        Unit2.Move()
        Unit3.Move()
        i+=1
        
def main():
    Play()
if __name__=="__main__":
    main()
    
    

