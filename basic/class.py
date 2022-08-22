class student:
    Name= "mayur"
    Email= "m@gmail.com"
    clg= ""

    def __init__(self, collageName):
        self.clg = collageName

    def rollno(self):
        print("23", self.Name)



mayur = student("VNSGU")
print(mayur)
mayur.rollno()


