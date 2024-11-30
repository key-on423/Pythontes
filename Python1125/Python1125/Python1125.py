

#print("hah","big",sep='?',end="jieshu")

#print(12/4-2+5*8/4%5/2)

#isalnum()判断所有字符都是数字或字母
#isalpha()判断所有字符都是字母
#isdigit()判断所有字符都是数字 islower() isupper()判断带小写
#isspace()判断空白字符

# a='1'
# if a.isdigit():
#            print(a,"是数字")
import string
x=(input("请输入一个正整数:"))
y=int(x)
z=1
while y/10>=1:
    z+=1
    y=y/10
print(x,"是",z,"位数")
print(x[::-1])
