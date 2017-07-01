#CREATE THE PERSON CLASS
class Person:
	def __init__(self, age, weight, height, activity_level, goal, **kwargs):
      self.age = 0
      self.weight = 0
      self.height = 0
      self.activity_level = 0
      self.goal = ""

      for key, value in kwargs.items():
         setattr(self, key, value)

   def total_daily_expend(self):
      #INSERT FORMULA FOR TDEE HERE

#CREATE THE FUNCTIONS
def gain():

def maintain():

def lose():