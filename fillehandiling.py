#filehandling

import csv
f=open('file.csv',"a",newline="")
a=csv.writer(f)
a.writerow(["studentid","rollno","name"])
studentid=int(input("enter student id:"))
rollno=int(input("enter rollno:"))
name=input("enter name:")
a.writerow([studentid,rollno,name])
print=('student record has save')
