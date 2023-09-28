

# list=["apple","banna","orange","grape","pineaplle"]
# list[3]="dgrgdgrgddddddddddd"
# print(list)



# a=int(input())
# if a<15:
#     print("rgldkrg")
# else:
#     print("sefkse")





# for i in range(1,10+1):
#     for j in range(1,10+1):
#         print(i*j, end="\t")
#     print()






# num = lambda x :x+15
# print(num(10))



# import functools


# list=[]
# sum = functools.reduce(lambda x,y:x+y,list)
# print(sum)




# y = (lambda x : x-3)(5)
# print(y)






# class MyIterator:
#     def __init__(self,max_value):
#         self.max_value = max_value
#         self.current = 0

#     def __str__(self):
#         return "My name Iterator"

#     def __iter__(self):
#         print('iterator\n')
#         return self

#     def __next__(self):
#         print('next\n')
#         if self.current < self.max_value:
#             self.current += 1
#             return self.current
#         else:
#             raise StopIteration 

# my_iter = MyIterator(5)
# for num in my_iter:
#     print(num)

    



# list = [10,20,30,40,50]
# list.append(60)
# list.remove(20)
# print(list)

# second_list = ("sef","fsef","efse")
# print(second_list[2])



# third_list = [1,2,3,4,5]
# dict={}
# for i in third_list:
#     dict[i]=i
# print(dict)



# second_dict = {"name":"Daniyar","age":18,"tel":"54654"}
# for i in second_dict:
#     print(i)
# print(second_dict["name"])
# print(second_dict.keys())
# print(second_dict.values())
# second_dict["xxx"]=1
# print(second_dict)







# alarm = datetime.time(6,0,0) 
# today= datetime.datetime.now()
# delta= datetime.timedelta(days=1)
# tomorow = today + delta 

# print(datetime.datetime.combine(tomorow,alarm))

# today= datetime.datetime.now()
# delta= datetime.datetime(year=18,month=1,day=1)
# past=today-delta
# year = past.days // 365
# month = ((past.days % 365) // 12) + 1
# days = month % 31
# print(past.days % 365)
# x = datetime.datetime(year, month, days )
# print(x)

# print(year)
# print(year)
# print(month)
# print(days)


# import openpyxl
# from openpyxl import Workbook
# import requests
# import json
# from docx import Document


# wb = Workbook()
# sheet = wb.active
# for i in range(1,11):
#     sheet.cell(row=i,column=1,value=i)

# letters = "ABCDEFGHIJ"
# for i , letter in enumerate(letters, 1):
#     sheet.cell(row=i,column=2,value=letter)

# wb.save('excel_file.xlsx')


# wb = openpyxl.load_workbook('excel_file.xlsx')
# sheet = wb.active

# first_column = [sheet.cell(row=1, column=i).value for i in range(1,11)]

# f_column = []
# for i in range(1,11):
#     f_column.append(sheet.cell(row=i, column=1).value)


# second_column = [sheet.cell(row=2, column=i).value for i in range(1,11)]

# s_column = []
# for i in range(1,11):
#     s_column.append(sheet.cell(row=i, column=2).value)


# print("Первая строка:", f_column)
# print("Вторая строка:", s_column)




# import openpyxl
# from openpyxl import Workbook
from operator import index
from re import X
from tkinter import Y
from turtle import circle
import requests
import json
# from docx import Document


# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# data=response.json()

# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file)

# with open('data.json', 'r') as json_file:
#     data_dict = json.load(json_file)

# for i in data_dict:
#     if i['id'] % 2 ==0:
#         print(i)





# import random
# list=[]
# for i in range(3):
#     list.append(random.randint(1,10))

# result = ", ".join(map(str, list))


# print(f"Hello  {result} these tabels are free")

# choice=int(input("выберите стол "))

# menu= {"суп":2000,"мясо":5000,"салат":1000,"мороженное":500,"чай":100}

# for i in menu:
#     print(f"{i}: {str(menu[i]).replace('[', '').replace(']', '')}")

# order=input("Что будете ? ")

# sym = []
# if order == "суп":
#     sum.append(2000)
# elif order =="мясо":
#     print("Итог 5000")
# elif order =="салат":
#     print("Итог 1000")
# elif order =="мороженное":
#     print("Итог 500")
# elif order =="чай":
#     print("Итог 100")
# else:
#     print("ERROR")

# print(sym)

# elsr=input("Что еще ?")
# if elsr == "нет":
#     print("Хорошо")
# elif elsr =="мясо":
#     print("Итог 5000")
# elif elsr =="салат":
#     print("Итог 1000")
# elif elsr =="мороженное":
#     print("Итог 500")
# elif elsr =="чай":
#     print("Итог 100")
# else:
#     print("ERROR")
    
# sym = ()
# if order == "суп":
#     sum += 2000
# elif order =="мясо":
#     print("Итог 5000")
# elif order =="салат":
#     print("Итог 1000")
# elif order =="мороженное":
#     print("Итог 500")
# elif order =="чай":
#     print("Итог 100")
# else:
#     print("ERROR")





# try:
#     number= int(input("Intput number: "))
#     print("Input number: ", number)
# except:
#     print("Error")
# print("It is all")


# try:
#     n = input('intput number: ')
#     n = int(n)
    # m = input('Intput second number: ')
    # m = int(m)
#     result = n / m
#     print("Ок. вы вели число", n,"и", m)
#     print("Результат их деления ", result)
# except ValueError:
#     print("Wrong")
# except ZeroDivisionError:
#     print("Деление на ноль")
# finally:
#     print("Конец")


# a,b = int(input()), int(input())
# try:
#     if b == 0:
#         raise ZeroDivisionError
# except:
#     print("Деление на 0")
# print("Будет ли это напечатано?")


# try:
#     n = input('intput number: ')
#     m = input('Intput second number: ')
#     n = int(n)
#     m = int(m)
#     result = n + m
#     print("Ок. вы вели число", n,"и", m)
#     print("Результат их суммирование ", result)
# except ValueError:
#     print(str(n)+str(m))
    


# try:
#     n = input('intput number: ')
#     n = int(n)
#     sum = 0
#     mult = 1
#     print("Ок. вы вели число", n)
#     while n > 0:
#         w = n % 10
#         sum = sum + w
#         mult = mult * w
#         try:
#             if w == 0:
#                 raise ZeroDivisionError
#         except:
#             print("Деление на 0")
#         n=n//10
#     print("Результат их суммирование ",sum )
#     print("Результат их произведение ",mult )
# except ValueError:
#     print("Деление на 0")


# '''
# чет,нечет = белый
# нечет,чет=белый

# нечет,нечет=черный
# чет,чет = черный

# '''


# try:
#     delenie_x = int(input('intput number: '))
#     y1 = int(input('Intput second number: '))

#     print("Ок. вы вели число", delenie_x, "и",y1)
#     x1 = 0
#     x2 = 0
#     delenie_y = 0
#     while delenie_x > 0:
#         w = delenie_x % 10
#         x1 = w
#         x2 = 
#         delenie_x=delenie_x//10
#     print(x1)


#     while y1 > 0:
#         w = y1 % 10
#         delenie_y = (delenie_y, w)
#         y1=y1//10


#     # if x


#         # try:
#         #     if w == 0:
#         #         raise ZeroDivisionError
#         # except:
#         #     print("Деление на 0")
#         # n=n//10
# #     print("Результат их суммирование ", )
# #     print("Результат их произведение ", )
# except ValueError:
#     print("Деление на 0")




# class Prorammer():
#     def __init__(self,salary,resposibilities):
#         self.salary = salary
#         self.resposibilities = resposibilities

#     def write_code():
#         print("Code")

# ivan = Prorammer(450000,"web developer")

# ivan.write_code()
         



# class Person():
#     def __init__(self,name,day,city,country):
#         self.name = name
#         self.day = day
#         self.__phone = ''
#         self.city = city
#         self.country = country
#         self.__address = ''

   
#     def get_phone(self):
#         return self.__phone

#     def set_phone(self, phone):
#         self.__phone = phone

#     def set_address(self,address):
#         self.__address = address

#     def get_address(self):
#         return self.__address



# first = Person("Daniyar","22.11.2004","Astana","KZ")

# first.set_phone(454512)
# first.set_address("Kenesary")
# print(first.get_phone())
# print(first.get_address())





# class City():
#     def __init__(self,population,zona):
#         # self.name = name
#         # self.region = region
#         # self.__phone = ''
#         self.population = population
#         # self.country = country
#         # self.__index = ''
#         self.zona = zona

   
    # def get_phone(self):
    #     return self.__phone

    # def set_phone(self, phone):
    #     self.__phone = phone

    # def set_index(self,index):
    #     self.__index = index

    # def get_index(self):
    #     return self.__index

    # def __add__(self,population):
    #     return self.zona + population.zona


# first= City(5,5)
# second = City(6,8)
# print(first+second)








class Games():
    def __init__(self,name,year):
        self.year = year
        self.name = name
 
    def get_Name(self):
        return self.name


class PCGames(Games):
    def __init__(self,kind,name,year):
        super().__init__(name,year)
        self.kind = kind

    def get_Name(self):
        return f'PC Games {self.name}'
    

class PS4Games(Games):
    def __init__(self,price,name,year):
        super().__init__(name,year)
        self.price = price

    def get_Name(self):
        return f'PS4 Games {self.name}'

class XboxGames(Games):
    def __init__(self,gg,name,year):
        super().__init__(name,year)
        self.gg = gg

    def get_Name(self):
        return f'Xbox Games {self.name}'


class MobileGames(Games):
    def __init__(self,comfort,name,year):
        super().__init__(name,year)
        self.comfort = comfort

    def get_Name(self):
        return f'Mobile Games {self.name}'


cock = MobileGames('Nope', 'Clash of Clans', 2013) 
cor = MobileGames('Nope', 'Clash Royale', 2019) 



print(cock.get_Name())
print(cor.get_Name())

