#CREATE THE PERSON CLASS
class Person:
   def __init__(self, name, age, sex, weight, height, activity_level, goal, **kwargs):
      self.name = name
      self.age = age
      self.sex = sex
      self.weight = weight
      self.height = height
      self.activity_level = activity_level
      self.goal = goal

      for key, value in kwargs.items():
         setattr(self, key, value)

   def basal_metabolic_rate(self):
      #INSERT FORMULA FOR BMR HERE
      #OUTPUT BASED ON MALE OR FEMALE
      #WOMAN
      if sex == 'f'
         return 655 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age)
      #MALE
      if sex == 'm'
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