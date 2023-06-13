# 1 Car  nomli class yarating   uning make ,model,color ,year ,price ,km ,id  atrabutlari
# 2 km va id lariga inkapsulatsiya qo’llanilsin.
# 3  get_km() ,get_id() ,get_info()  va add_km() metodlarni yozing.
class Car:
    def __init__(self,make,model,color,year,price,id, km = 0) -> None:
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price =price
        self.__km = km
        self.__id = id
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id

    def add_km(self,km):
        self.get_km + km
    
    def get_info(self):

        return f""" Firmasi: {self.make}
Modeli: {self.model}
Rangi: {self.color}
Yili:  {self.year}
Narxi: {self.price}
Km:    {self.get_km()}
Id:    {self.get_id()}\n"""


def search_id(id,lis):
    for i in range(len(lis)):
        if  id == lis[i].get_id():
            print(lis[i].get_info())


def sort_id(lis):
    sorted_list = sorted(lis, key=lambda x: x.get_id())
    return sorted_list


c1 = Car('fronsiya','mers','qora',2001,15000,123,1000)
c2 = Car('malazia','jip','oq',2061,12000,1234,19000)
c3 = Car('ukraina','porsh','qizl',2010,13000,12345,55000)
# print(c1.get_info())


lis = [c1,c2,c3]

liss = (sort_id(lis))
for i in liss:
    print(i.get_info())
