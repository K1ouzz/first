

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







import datetime
import imp
from unittest import result
import webbrowser

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





import random
list=[]
for i in range(3):
    list.append(random.randint(1,10))

result = ", ".join(map(str, list))


print(f"Hello  {result} these tabels are free")

choice=int(input("выберите стол "))

menu= {"суп":2000,"мясо":5000,"салат":1000,"мороженное":500,"чай":100}

for i in menu:
    print(f"{i}: {str(menu[i]).replace('[', '').replace(']', '')}")

order=input("Что будете ? ")

sym = []
if order == "суп":
    sum.append(2000)
elif order =="мясо":
    print("Итог 5000")
elif order =="салат":
    print("Итог 1000")
elif order =="мороженное":
    print("Итог 500")
elif order =="чай":
    print("Итог 100")
else:
    print("ERROR")

print(sym)

elsr=input("Что еще ?")
if elsr == "нет":
    print("Хорошо")
elif elsr =="мясо":
    print("Итог 5000")
elif elsr =="салат":
    print("Итог 1000")
elif elsr =="мороженное":
    print("Итог 500")
elif elsr =="чай":
    print("Итог 100")
else:
    print("ERROR")
    
sym = ()
if order == "суп":
    sum += 2000
elif order =="мясо":
    print("Итог 5000")
elif order =="салат":
    print("Итог 1000")
elif order =="мороженное":
    print("Итог 500")
elif order =="чай":
    print("Итог 100")
else:
    print("ERROR")

