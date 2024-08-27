class School:
  def __init__(self,name,level,numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def __repr__(self):
    repr = "A {} school named {} with {} students. ".format(self.level,self.name,self.numberOfStudents)
    return repr

  def getName(self):
    return self.name
  def getLevel(self):
    return self.level
  def getStudents(self):
    return self.numberOfStudents

  def setStudents(self, rando):
    self.numberOfStudents = rando

class PrimarySchool(School):
  def __init__(self,name,numberOfStudents,pickupPolicy):
    super().__init__(name,"primary",numberOfStudents)
    self.pickupPolicy = pickupPolicy
  
  def __repr__(self):
    repr = super().__repr__() + "The pickup policy is: {}.".format(self.pickupPolicy)
    return repr

  def getPickupPolicy(self):
    return self.pickupPolicy


#tester = PrimarySchool("OLPHS",500,"Pickup Allowed")
#print(tester.getPickupPolicy())

class HighSchool(School):
  def __init__(self,name,numberOfStudents,sportsTeams):
    super().__init__(name,"HighSchool",250)
    self.sportsTeams = sportsTeams
  
  def __repr__(self):
    repr = super().__repr__() + "The sports teams are: {}.".format(self.sportsTeams)
    return repr

  def getSportsTeams(self):
    return self.sportsTeams
  
  def setSportsTeams(self,sport):
    self.sportsTeams.append(sport)

tester = HighSchool("PCSHS",300,['Basketball','Volleyball'])
tester.setSportsTeams("Soccer")
print(tester.getSportsTeams())
