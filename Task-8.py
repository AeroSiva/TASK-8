#Q Using the python object oriented Programming scheme (OOPS) kindly complete the following tasks 
    #which is given as below:-
    # Q1. Create a Pythhon class called Circle with constructor which will take a list as an argument for the task.
    # The list is [10,501,22,37,100,999,87,351]
    # Q2. Create proper member variable inside the task if required and use them when necessary. 
    # For example for this task create a class private variable named pi = 3.141
    # Q3. From the given List create two class Mwthods Area and Perimeter 
    # which will be going to calculate the area and Radius.


class Circle:
    def __init__(self,lst) :
        self.lst = lst
        self.pi = 3.141
    def area (self) :
        area_lst = []
        a = 0
        for radius in self.lst :
            a = (self.pi)*(radius**2)
            area_lst.append(a)
        return area_lst
    def perimeter (self) :
        perimeter_lst = []
        p = 0
        for radius in self.lst :
            p = 2*(self.pi)*radius
            perimeter_lst.append(p)
        return perimeter_lst

c = Circle([10,501,22,37,100,999,87,351])
print (c.area())
print (c.perimeter())






#Q4 kindly visit the belowURL and convert the UML diagram into Python Class and its methods.
# https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md


'''TV class
TVClass - Base class
LedTV class
PlasmaTV class


Part - A

Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume.
 Specify brand in a constructor parameter. Channel should be 1 by default. Volume should be 50 by default.
Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
Add a method to set the channel. Let's say the TV has only 50 channels 
so if you try to set channel 60 the TV will stay at the current channel.
Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor).
It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75".


Part - B : LED , Plasma

Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh rate , 
functionalities like viewingAngle , Backlight, DisplayDetails , which displays the detailed features of the TV'''


class Tv:
    def __init__(self, brand,inches,price):
        self.brand = brand
        self.channel = 1
        self.price = price
        self.inches = inches
        self.volume = 50
    
 
    def increase_volume(self):
        if 0<= self.volume <100:
            self.volume += 1

    def decrease_volume(self):
        if 0 < self.volume <= 100:
            self.volume -= 1

    def set_channel(self, chnl):
        if 1 <= chnl <= 50:
            self.channel = chnl

    def reset(self):
        self.channel= 1
        self.volume = 50
    
    def status(self):
        return f"It is {self.brand} brand TV {self.inches} inches TV of price {self.price} is at channel {self.channel} and volume {self.volume}"

Bass_class = Tv(brand = "Panasonic",inches = 32,price = 35000)
result = Bass_class.status()
print('initial status: ',result)
Bass_class.increase_volume()
result = Bass_class.status()
print('Volume increased by one: ',result)
Bass_class.decrease_volume()
result = Bass_class.status()
print('Volume decreased by one: ',result)
Bass_class.set_channel(16)
result = Bass_class.status()
print('Chanel set at 16: ',result)
Bass_class.set_channel(56)
result = Bass_class.status()
print('Chanel set at 56: ',result)
Bass_class.reset() 
result = Bass_class.status()
print('Reset status',result)

class Led(Tv):
    def __init__(self,brand,inches,price,screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand,inches,price)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
    
    def viewing_angle(self):
        return "Best at 30 to 40 degrees."

    def backlight(self):
       return "Yes"

    def display_details(self):
        return f"""It is {self.brand} brand LED TV and {self.inches} inches TV of price {self.price} is at channel {self.channel} and volume {self.volume} and is of having following specifications:
        Screen Thickness: {self.screen_thickness},
        Energy Usage: {self.energy_usage},
        Lifespan: {self.lifespan},
        Refresh Rate: {self.refresh_rate},
        View angle: {self.viewing_angle()},
        Backlight: {self.backlight()}"""
LED = Led(brand = "Panasonic",inches = 42, price =35000,screen_thickness = "1.2 inches", energy_usage = "64 watts on average", lifespan = "1 lakh hour", refresh_rate = "120 Hz")
print(LED.display_details())
print('LED Tv status: ',LED.status())


class Plasma(Tv):
    def __init__(self,brand,inches,price,screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand,inches,price)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
    
    def viewing_angle(self):
        return "Best at 0 to 170 degrees."

    def backlight(self):
       return "No"

    def display_details(self):
        return f"""It is {self.brand} brand Plasma - TV and {self.inches} inches TV of price {self.price} is at channel {self.channel} and volume {self.volume} and is of having following specifications:
        Screen Thickness: {self.screen_thickness},
        Energy Usage: {self.energy_usage},
        Lifespan: {self.lifespan},
        Refresh Rate: {self.refresh_rate},
        View angle: {self.viewing_angle()},
        Backlight: {self.backlight()}"""
plasma_tv = Plasma(brand = "Panasonic",inches = 42, price = 55000,screen_thickness = "1 inches", energy_usage = "195 watts on average", lifespan = "20,000 to 60,000 hours", refresh_rate = "upto 600 Hz")
print(plasma_tv.display_details())
print('Plasma TV status: ',plasma_tv.status()) 