class Car:
    def __init__(self, fuel, engine):
        self.fuel = fuel
        self.engine = engine
    
    def refuel(self):
        print("주유 중 입니다")

    def __str__(self):
        return '나는 자동차입니다. '

class Tesla(Car):
    def __init__(self, fuel, engine):
        self.fuel = fuel
        self.engine = engine
    
    def refuel(self):
        print('충전 중 입니다.')
    
    def __str__(self):
        return super(Tesla, self).__str__() + '바로, 최고의 전기차죠!'

b = Tesla('electric', 'motor')
b.refuel()
b.__str__()
