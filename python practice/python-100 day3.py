#使用者身份認證
"""
username = input('please enter username : ')
password = input('plaese enter password : ')

if username == 'mia' and password == '123456':
    print('verification successful!')
else:
    print('verification failed!')    
"""

#分段函式求值
"""
     = 3x - 5(x>1)   
f(x) = x + 2 (-1<=x<=1)
     = 5x + 3 (x<-1)
"""
"""
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))     

#英制單位英吋與公制單位釐米轉換
value = float(input('please enter the length : '))
unit = input('please enter the length unit (inch or cm) : ')
if unit == 'inch':
    print('%f inch = %f cm' % (value, value*2.54))
elif unit == 'cm':
    print('%f cm = %f inch' % (value, value/2.54))    

#百分制轉換為等級製成績
score = float(input('please enter the score : '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('the grade is : ', grade)                   
"""
#輸入三個邊長，如果能夠成三角形就計算周長和面積
a = float(input('the first side length : '))
b = float(input('the second side length : '))
c = float(input('the third side length : '))
if a+b>c and a+c>b and b+c>a:
    print('perimeter = %.1f' % (a+b+c))
    s = (a + b + c) / 2
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5  #海龍公式
    print('area = %.1f' % area)
else:
    print('It cannot be a triangle')    