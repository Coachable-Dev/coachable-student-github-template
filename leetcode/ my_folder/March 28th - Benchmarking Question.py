class Counter:
  def __init__(self,num):
    self.count=num
  def get_count(self):
    return self.count
  def increment(self):
    self.count+=1
  def reset(self):
    self.count=0

class LimitCounter(Counter):
  def __init__(self,num,max_limit=100):
    if num>max_limit:
      raise ValueError(f" should be under {max_limit}")
    super().__init__(num)
    self.max_limit=max_limit
  def increment(self):
    if self.count+1>self.max_limit:
       raise ValueError(f" should be under {max_limit}")
    self.count+=1

class Thermostat:
  def __init__(self,temperature=72.0):
    self.temperature=temperature
  def get_temperature(self):
    return self.temperature
  def set_temperature(self,new_temp):
    if new_temp < 50 or new_temp > 90:  
            raise ValueError("should be around between 50°F and 90°F！")
        self.temperature = new_temp  
    def __str__(self):
      return f"Thermostat set to {self.temperature}°F"
      
  class smartThermostat(Thermostat):
    def __init__(self, temperature=72.0，eco_mode=False):
      super().__init__(temperature)  
      self.eco_mode = eco_mode
      
    def set_temperature(self, new_temp):
      if self.eco_mode: 
            if new_temp < 60 or new_temp > 78:  
                raise ValueError("should between 60°F and 78°F！")
        else: 
            if new_temp < 50 or new_temp > 90:
                raise ValueError("should be around between 50°F and 90°F!)
        self.temperature = new_temp  

    def toggle_eco_mode(self):  
        self.eco_mode = not self.eco_mode 

    def __str__(self):
      eco="on" if self.eco_mode else "off"
      retrun f"SmartThermostat set to {self.temperature} f,eco mode {eco} "
      
      
      
      
    
    
