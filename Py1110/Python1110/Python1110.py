#1.


# x=[1,2,3,4,5,6,7,8,9,-1]
# jishu=oushu=0
# for i in x:
#     if i%2==0:
#         oushu+=i
#     else:
#         jishu+=i
# print(x,jishu,oushu)
# print("奇数和为",jishu,"偶数和为",oushu)



# dic={'张三':45,'李四':78,'徐来':40,'沙思思':96,'如一':65}
# renshu=len(dic)
# sum=0
# for i in dic:
#          sum+=dic[i]
# print(dic)
# print("总人数为:",len(dic),"平均分为:",sum/len(dic))





list1=[30,20,10,40,50]
vv=list(enumerate(list1))
sum=0
print(vv)
for i in list1:
    sum+=i
pinjun=sum/len(list1)
print("另列表二为大于列表一的平均值")
list2=list(enumerate([i for i in list1 if i>pinjun]))
print(list2)
