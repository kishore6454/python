''' create a class /name placements which has a func info which displace we have "673 still counting" create another class department with function display
    which will display thr name sof departments present in your college. create a class pragati with a func welcome which display func welcome to pragati engineering
    college this pragati class  should aslo display the details about department and placements '''
class placements:
    def info(self):
        print("displays we have 673 selected and still counting**")
class dept:
    def display(self):
        print('cse')
        print('it')
        print('ece')
        print('mech')
        print('civil')
        print('ai')
        print('eee')
class pragati(placements,dept):
        def welcome(self):
            print('welcome to pragati engineering college')
obj=pragati()
obj.info()
obj.welcome()
obj.display()

