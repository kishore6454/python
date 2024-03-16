#four pillars of oops

# 1->inheritance   parent-->class

class faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def print_info(self):
        print('faculty information=',self.f_name,self.department,self.f_id)
obj=faculty("kishore","it",1234)
obj.print_info()

class cse(faculty):
    pass
obj =cse("sai","it",1235)
obj.print_info()
