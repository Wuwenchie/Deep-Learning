a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))

#華氏轉攝氏 先-32 再乘以5/9
f = float(input('請輸入華氏溫度: '))
c = (f - 32) / 1.8
print('攝氏溫度為 %.1f' % c)
print(f'{f:.1f}華氏度 = {c:.1f}攝氏度')

#計算圓周常與園半徑
radius = float(input('請輸入園半徑 : '))
perimeter = 2 * 3.14159 * radius
area = 3.14159 * radius * radius
print('圓周長 = %.2f    園面積 = %.2f' % (perimeter, area))

#判斷閏年
year = int(input('請輸入年份 : '))

is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)