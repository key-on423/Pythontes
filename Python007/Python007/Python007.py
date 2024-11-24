
# 编写函数，给定任意字符串，计算每个字符出现的次数。调用该函数，输出结果。

# import string
# re={}#采用字典,字典的key不重复，只打印一次相同符号
# x=input("请输入一个字符串:")
# for i in x:
#     re[i]=x.count(i)
#     #print(i,"出现了",x.count(i),"次")
# for key in re:
#     print(key,"出现了",re[key],"次")


#编写函数，判断字符串是否为纯数字。

# def panbie(s):
#     x=0
#     for i in s:
#         if(s.isdigit()==0):
#             x=1
           
#     if(x==0):
#         print(s,"是纯数字")
#     else:
#         print(s,"不是纯数字")
# y=input("请输入一个纯数字字符串:")
# panbie(y)



#编写函数，判断一个数是否为素数。调用该函数，判断从键盘输入的数是否为素数
# import math
# x=int(input("请输入一个数:"))
# panbie=1
# for i in range(1,x):
#          if(x%i==0 and i!=1):
#             panbie=0
# if (panbie==1):
#     print(x,"是素数")
# else:
#     print(x,"不是素数")
  

#编写函数，利用可变参数计算一组数的最大值

def maxx(x):
    Maxx=x[0]
    for i in range (len(x)):
        if(Maxx<x[i]):
            Maxx=x[i]
    print(x,"中最大值为:",Maxx)

x=[1,2,3,4,5,6,7,8,9,10,999]
maxx(x)