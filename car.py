class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.model=model
        self.color=color
        self.company=company
        self.speedLimit=speedLimit
    
    def start(self):
        print("car is started")
        
    def accelarate(self):
        print("The car is accelarating")

    def stop(self):
        print("The car stopped")

bmw=Car("A1","red","BMW","85")
print(bmw.model)
bmw.start()