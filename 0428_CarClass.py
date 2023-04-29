class Car:
    PRIVATE_MAX_SPEED = 100
    PRIVATE_ACCELERATE = 10
    PRIVATE_BREAK = 10
    PRIVATE_SPEED = 0

    def __init__(self,model,color):
        self.model = model
        self.color = color

    def accelerate(self):
        self.PRIVATE_SPEED += self.PRIVATE_ACCELERATE
        self.PRIVATE_SPEED = min(self.PRIVATE_SPEED,self.PRIVATE_MAX_SPEED)

    def break_(self):
        self.PRIVATE_SPEED -= self.PRIVATE_BREAK
        self.PRIVATE_SPEED = max(self.PRIVATE_SPEED,0)

    def get_speed(self):
        return self.PRIVATE_SPEED


son_car = Car("son","red")
print(son_car.get_speed(),son_car.model,son_car.color)
son_car.accelerate()
print(son_car.get_speed())

for i in range(10):
    son_car.accelerate()
print(son_car.get_speed())

son_car.break_()
print(son_car.get_speed())

for i in range(10):
    son_car.break_()
print(son_car.get_speed())