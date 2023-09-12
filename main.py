

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

# alarm = datetime.time(6,0,0) 
# today= datetime.datetime.now()
# delta= datetime.timedelta(days=1)
# tomorow = today + delta 

# print(datetime.datetime.combine(tomorow,alarm))

today= datetime.datetime.now()
delta= datetime.datetime(year=18,month=1,day=1)
past=today-delta
year = past.days // 365
month = year // 12
days = month % 31
print(past.days % 365)
x = datetime.datetime(year, month, days )
print(x)

print(past)
print(year)
print(month)
print(days)








































