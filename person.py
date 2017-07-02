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