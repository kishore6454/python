#polymorphism run time

class father:
    def bike(self):
        print('ktm')

    def laptop(self):
        print('laptop with low features')
class kishore(father):
    def laptop(self):
        print('as high features s/w')
        print('i7,1tb')
obj=kishore()
obj.bike()
obj.laptop()
    
