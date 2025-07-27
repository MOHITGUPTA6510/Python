class car:
    def __init__(self,brand,model,rate):
        self.brand = brand
        self.model = model
        self.rate = rate

    def display_(self):
        print("Brand:",self.brand)
        print("model:",self.model)
        print("rate:",self.rate)

car1=car("toyota","fortuner","100000")
car2=car("BMW","M5","40000")
car3=car("lembo","aventedor","400000000")

car1.display_()
car2.display_()
car3.display_()
