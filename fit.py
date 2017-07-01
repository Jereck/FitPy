#CREATE THE PERSON CLASS
class Person:
   def __init__(self, name, age, sex, weight, height, activity_level, goal, **kwargs):
      self.name = ""
      self.age = 0
      self.sex = ""
      self.weight = 0
      self.height = 0
      self.activity_level = 0
      self.goal = ""

      for key, value in kwargs.items():
         setattr(self, key, value)

   def basal_metabolic_rate(self):
      #INSERT FORMULA FOR BMR HERE
      #OUTPUT BASED ON MALE OR FEMALE
      #WOMAN
      return 655 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age)
      #MALE
      return 66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age)

   def total_daily_expend(self):
      #INSERT FORMULA FOR TDEE
      return basal_metabolic_rate() * activity_level

#CREATE THE FUNCTIONS FOR GAIN, MAINTAIN, LOSE
def gain():
   return gain_tdee
def maintain():
   return maintain_tdee
def lose():
   return lose_tdee