class Person:
   'Represents the person/user using this API'

   def __init__(self, name, age, sex, weight, height, activity_level, goal, **kwargs):
      '''Initialize the stats of the new person. Each attribute can be specified
      and the ***kwargs argument is just a place holder for new arguments that
      might beed to come up later as the program expands'''

      self.name = name
      self.age = age
      self.sex = sex
      self.weight = weight
      self.height = height
      self.activity_level = activity_level
      self.goal = goal

      for key, value in kwargs.items():
         setattr(self, key, value)

'Initializes an example program to make sure this works'
person1 = Person("Jake", 28, 'm', 180, 74, 2, 'gain')
print (person1)