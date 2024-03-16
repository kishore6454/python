#multilevel interitance

class placements:
    def info(self):
        print("displays we have 673 selected and still counting**")
class dept(placements):
    def display(self):
        print('cse')
        print('it')
        print('ece')
        print('mech')
        print('civil')
        print('ai')
        print('eee')
class pragati(dept):
        def welcome(self):
            print('welcome to pragati engineering college')
obj=pragati()
obj.info()
obj.welcome()
obj.display()


 ''' obj2=dept()
     obj2,info() '''
