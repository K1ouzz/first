

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






class MyIterator:
    def __init__(self,max_value):
        self.max_value = max_value
        self.current = 0

    def __str__(self):
        return "My name Iterator"

    def __iter__(self):
        print('iterator\n')
        return self

    def __next__(self):
        print('next\n')
        if self.current < self.max_value:
            self.current += 1
            return self.current
        else:
            raise StopIteration 

my_iter = MyIterator(5)
for num in my_iter:
    print(num)

    





















