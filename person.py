class Person:
   def __init__(self, name, age, weight, height_feet, height_inches, goal):
      self.name = name
      self.age = age
      self.weight = weight
      self.height_feet = height_feet
      self.height_inches = height_inches
      self.goal = goal

   def reset(self):
      self.name = ""
      self.age = 0
      self.weight = 0
      self.goal = ""

jake = Person("Jake", 28, 180, 6, 2, "gain")

print(jake.name)
print(jake.age)
print(jake.weight)
print((jake.height_feet * 12) + jake.height_inches)
print(jake.goal)