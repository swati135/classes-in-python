class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.model = model
        self.speed_limit= speed_limit
        
    def start(self):
        print("started")
        
    def stop(self):
        print("Stopped")
        

myCar = Car('q7','black','audi',120)
print(myCar.company)
myCar.start()

