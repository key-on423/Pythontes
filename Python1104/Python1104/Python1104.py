# 输入20个学生的成绩，请对其进行统计优（100～90）、良（89～80）、中（79～60）、差（59～0）四个等级的人数，输出由等级和人数构成的字典。

# list1=[68,77,60,57,36,88,69,99,88,81,82,83,85,89,56,55,48,75,80,91]
# list2=[]
# list3=[]
# list4=[]
# list5=[]
# for i in list1:
#     if i<60:
#         list2.append(i)
#     elif i<80:
#         list3.append(i)
#     elif i<90:
#         list4.append(i)
#     else:
#         list5.append(i)
# print("等级优人数:",len(list5),list5,"\n等级良的人数:",len(list4),list4,"\n等级中的人数",len(list3),list3,"\n等级差的人数:",len(list2),list2)


#编写程序，随机生成50个介于[1, 20]之间的整数，请写出集合推导式

# import random

# list1=[]
# for _ in range(50):
#            list1.append(random.randint(1,20))
# print(list1)


#编写程序，请用列表推导式表示：100以内既被3整除又被7整除的数。
# list1=[]
# for i in range(1,100):
#     if(i%3==0 and i%7==0):
#         list1.append(i)
# print("100以内既被3整除又被7整除的数:",list1)



#编写程序，生成一个15个不重复的大小写字母组成的列表。
import random
import string
s=string.ascii_letters#所有大小写字母 ascii_lowercase + ascii_uppercase
r=random.sample(s,15)
print(r)