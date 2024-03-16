import csv
class landr:
    def userlogin(kishore,u,p):
        with open("userinfo.csv","r",newline="")as file:
            read=csv.DictReader(file)
            for row in read:
                if row['username']==u and row['password']==p:
                    return True
            return False
    def registration(kishore,username,password,email):
        kishore.uname=username
        kishore.pwd=password
        kishore.em=email
        with open('userinfo.csv','a',newline="") as file:
            a=csv.writer(file)
            a.writerow([kishore.uname,kishore.pwd,kishore.em])
        
                     