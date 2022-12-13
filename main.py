#mammal is the base class
class mammal:
      
    def setHair_Color(self, color):
        self.hair_color = color

    def displayOption(self):
        print(f"The hair color is: {self.hair_color}")
      
#dog inherits from mammal
class car(vehicle):

    #set the dog name
    def setName(self, name):
        self.dog_name = name

    #display the dog name
    def displayOption(self):
        print(f"The dog name is: {self.dog_name}")
        print(f"The color to the mammal is: {self.hair_color}")      

input_dog = input("Please enter your dog name:")
input_hair = input("Please enter the hair color:")
new_dog = dog()
new_dog.setName(input_dog)
new_dog.setHair_Color(input_hair)
new_dog.displayOption()
