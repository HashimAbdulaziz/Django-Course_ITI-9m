class Car:
   
   def __init__(self, name, fuelRate=100, velocity=0):
      self.name = name
      self.fuelRate = max(0, min(fuelRate, 100))
      self.velocity = max(0, min(velocity, 100))


   def run(self, velocity, distance):
      self.velocity = max(0, min(velocity, 200))

      fuel_needed = (distance//10)*10 

      if fuel_needed > self.fuelRate:
         possible_distance = (self.fuelRate//10)*10
         self.fuelRate = 0
         self.stop(distance - possible_distance)
      else:
         self.fuelRate -= fuel_needed
         self.stop(0)
   

   def stop(self, remaining_distance):
      self.velocity = 0
      
      if remaining_distance > 0:
         print(f"Stopped, Remainging distance is {remaining_distance} km")
      else:
         print("Arrived at destination")