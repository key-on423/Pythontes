﻿
#1. 字符串反转，户输入一句英文,将其中的单词以反序输出。例如:hello c sharp --- sharp c hello。
# x=input("请输入一个字符串：")
# y=x[::-1]
# print("反向输入为:")
# print(y)

#2. 判断一个字符串是否是回文，即正读和反读都一样的字符串。比如‘12321’
# x=input("请输入一个字符串：")
# y=x.replace(" ","")
# print(y)
# z=y[::-1]
# if(z==x):
#     print("该字符串是回文")
# else:
#     print("该字符串不是回文")

#3. 编写一个程序，找出字符串中重复的字符，保存在列表。
# import string
# list1=[]
# x=input("请输入一个字符串：")
# for i in x:
#     if(x.count(i)>1):
#         if(i not in list1):
#          list1.append(i)
# print("重复字符为:",list1)


#4.有个字符串数组my_str，存储了10个书名，书名有长有短，现在将他们统一处理，若长度大于10，
#则截取长度为8的子串,将统一处理后的结果输出。

my_str={"平凡的世界","穆斯林的葬礼","挪威的森林","关于最完美政治制度及乌托邦新岛既有益又有趣的金书",
        "关于一名叫做鲁宾逊·克鲁索诞生于约克镇并且因为船难而独活在一个美洲海岸边接近奥里诺科河河口的小岛长达二十八年的水手的离奇又惊人的冒险故事",
        "曹禺剧本选","生命从明天开始","呼啸山庄","许三观卖血记","拿破仑全传"}
print(my_str)
print("修改后为:")
y=0
for i in my_str:
        print()
        y=0
        for z in i:
         if(y<8):
            print(z,end='')
            y+=1
print("\n结束")
            