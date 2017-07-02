def basal_metabolic_rate(self):
   #INSERT FORMULA FOR BMR HERE -- OUTPUT BASED ON MALE OR FEMALE
   #FEMALE
   if sex == 'f'
      return 655 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age)
   #MALE
   if sex == 'm'
      return 66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age)

def total_daily_expend(self):
   #INSERT FORMULA FOR TDEE
   return basal_metabolic_rate() * activity_level

#CONVERT INPUT POUNDS TO KILOGRAMS FOR EQUATION
def pounds_to_kilograms(self):
   return pounds * 0.45359227

#CONVERT INPUT FEET TO INCHES FOR EQUATION
def feet_to_inches(self):
   return feet / 12

