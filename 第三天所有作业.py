#实现输入10个数字，并打印10个数的求和结果
'''
num = [10,1,2,3,4,5,6,7,8,9]

i = 0
k = 0
while i <10:
    k = k + num[i]
    i = i+1

print(k)
'''
#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数

'''
num = ["0"]
i = 0
while i < 10:
    print("输入次数为",i+1,"次")
    sum = int(input("输入数字为："))
    if i == 0:
        num[0] = sum
    else:
        num.append(sum)
    i = i + 1
i=0
k=0
while i< 10:
    k = k+ num[i]
    i = i +1

p = len(num)
print("总和为：",k)
print("平均值为",k/p)
print("最大值是：",max(num))
'''
#使用random模块，如何产生 50~150之间的数

'''
import random
num = random.randint(50,100)
print(num)
'''
#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
# （结果判断：等腰，等边，直角，普通，不能形成三角形。）

'''
第一类型
a=int(input("输入第一条边："))
b=int(input("输入第二条边："))
c=int(input("输入第三条边："))

if (a+b<c) or (a+c<b) or (b+c<a):
    print("不能组成三角形")
elif a==b==c and a==b==c:
    print("这是等腰")
elif a==b==c :
    print("是等边三角形")
elif a==b or b==c or a==c:
    print("是等腰三角形")
elif (a*a+b*b==c*c) or (a*a+b*b==c*c) or (a*a+b*b==c*c):
    print("是直角三角形")
else:
    print("是普通三角形")
    
第二类型
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("等边三角形！")
    elif (a==b or b == c or a == c):
        print("等腰三角型！")
    elif (a * a +  b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print("直角三角形！")
    else:
        print("普通三角形！")
else:
    print("不能形成三角形！")
'''
#a=56,b=78调换为a=78,b=56

A=56
B=78
A = A + B    #A=134
B = A - B    # B = 56
A = A - B    # A = 78
print(A,B)

#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''
name = "root"
password = "admin"

i = 0
while i<3:
    n = input("请输入用户名：")
    p = input("请输入密码：")
    if n == name and p == password:
        print("恭喜您登陆成功")
        break
    else:
        print("密码输入失败，请重新输入，")
        print("您还有",2-i,"次机会")
        if i == 2:
            print("三次机会输入错误！系统已经锁定")
            break
    i = i+1
'''
#使用while编程实现求1~100以内的数的和
'''
a = 0
b = 1
while b <= 100:
    a = a + b
    b = b + 1
print("1~100的和为：",a)
'''
#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出
'''
bai = 3
hei = 2
gao =20
sky = 0
forg = 0
while True:
    sky = sky + 1
    forg = forg + bai
    if forg >= gao:
        break
    forg = forg - hei
print("第",sky,"天能爬出来！")
'''
#有一个列表，[“北京”,”上海”,”广东”]
#将中国所有省会城市添加到上述列表中
'''
sity = ["北京", "上海", "广东"]
while True:
    atc = input("请输入你要增加的城市：")
    if atc == "q" or atc == "Q":
        print("结束添加城市！")
        break
    sity.append(atc)
    print("已经添加的城市有：",sity)
'''
#广东成为第二大发达城市，将广东排在上海前面
'''
sity = ["北京", "上海", "广东"]
sity.remove("广东")  #移除
sity.insert(1,"广东")#插入
print(sity)
'''
#请统计前8城市的GDP总和，平均GDP
'''
gdp = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
i = 0
gt = 0
num = len(gdp)
while i < num:
    gt = gt + gdp[i]
    gt = int(gt)
    i = i + 1
pj = gt/num
print("总和gdp为：",gt,"平均gdp为：",pj)
'''
#以下一个列表，求其中是5的倍数的和
'''
a = [1,5,21,30,15,9,30,24]
num = []
l = len(a)
i = 0
k = 0
while i < l:
    k = 5 * a[i]
    num.insert(i,k)
    i = i + 1

i = 0
k = 0
while i <l:
    k = k + num[i]
    i = i +1
print("列表5倍，分别显示为：",num)
print("5倍之和显示为：",k)
'''