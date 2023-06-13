class Person:
    def __init__(self,first_name,last_name,birthdate) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def get_info(self):
        return f""" ismi: {self.first_name}
familiya:  {self.last_name}
tuglga kun:  {self.birthdate} \n"""
    
class Student(Person):
    def __init__(self, first_name, last_name, birthdate,faculty,leval) -> None:
        super().__init__(first_name, last_name, birthdate)
        self.faculyt = faculty
        self.level = leval
        self.subjecs = []

    def get_info(self):
        return super().get_info() + f""" fakulteti: {self.faculyt}\nkursi:  {self.level}"""
    
    
    def add_subject(self,fan):
        self.subjecs.append(fan)
    
    def remove_subject(self,ochr):
        if ochr in self.subjecs:
            self.subjecs.remove(ochr)
        
        else:
            print ('invalide Subject')

    def get_full_info(self):
        for sub in self.subjecs:
            print(sub.get_info())

class Subject:
    def __init__(self,name) -> None:
        self.name = name
    
    def get_info(self):
        return f"{self.name}"
    


student1=Student("John","Smith",2002,"programming",3)
fan1=Subject("Algorithms")
fan2=Subject("Algorithms2")
fan3=Subject("Algorithms3")
fan4=Subject("Algorithms4")
fan5=Subject("Algorithms5")

student1.add_subject(fan1)
student1.add_subject(fan2)
student1.add_subject(fan3)
student1.add_subject(fan4)
student1.add_subject(fan5)
student1.get_full_info()
student1.remove_subject(fan3)
student1.get_full_info()
