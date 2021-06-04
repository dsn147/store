'''
产生一个0~500的一个随机数，给5000金币  --
输入的数字大于随机数输出大了-500  --
输入的数字小于随机数输出小了-500  --
输入的数字正确输出“恭喜您猜对了”+3000金币

系统在输入15锁定。系统没有金币系统锁定

'''
#产生一个随机数
import random
num = random.randint(0,500)
kj = 5000  #开始金币
#
i = 0
print(num)
while i < 15:  #判断次数
    number = input("请输入一个数字")  #键盘输入
    number = int(number) #将字符创改为整数

    if number > num:   #判断
        kj= (kj - 400)
        print("大了，您还有金币为：",kj)
    elif number < num:
        kj= (kj - 300)
        print("小了，您还有金币为：",kj)
    else:
        kj= (kj + 3000)
        print("恭喜您猜对了，随机数字是：",num,"您当前金币为：",kj)
        print(kj)
        break


    if kj <= 0:
       print("您没有金币了")
       break  #跳出循环

    i= i + 1
  #  print("您已经输入了15次请重新开始",i)

