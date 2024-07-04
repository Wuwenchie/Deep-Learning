#找出水仙花數
#(Narcissistic number, 它是一個3位數，該數字每個位上數字的立方之和正好等於它本身)
"""
print('following is three digits Narcissistic number : ')
for num in  range(100, 1000):
    hun = num // 100
    ten = num % 10 // 10
    one = num % 10
    if num == one ** 3 + ten ** 3 + hun ** 3:
        print(num)
#正整數反轉 12345 54321 1234...5
num = int(input('please enter the integer : '))
reverse_num = 0
while num > 0:
    reverse_num =  reverse_num*10 + num%10
    num //= 10
print('the reverse number is : %d' % reverse_num)           
#百雞百錢問題
#(公雞5元一隻，母雞3元一隻，小雞1元三隻，用100塊錢買一百隻雞，問公雞、母雞、小雞各有多少隻？)
#100 = 5*x + 3*y + z/3
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y     #隻
        if 5*x + 3*y + z/3 == 100:  #錢
            print('公雞%d隻, 母雞%d隻, 小雞%d隻' % (x, y, z))
"""

#CRAPS賭博遊戲
"""
該遊戲使用兩粒骰子，玩家透過搖兩粒骰子獲得點數進行遊戲。

簡單的規則是:玩家第一次搖骰子如果搖出了7點或11點, 玩家勝;
            玩家第一次如果搖出2點、3點或12點, 莊家勝; 其他點數玩家繼續搖骰子, 如果玩家搖出了7點, 莊家勝;
            如果玩家搖出了第一次搖的點數，玩家勝；其他點數，玩家繼續要骰子，直到分出勝負。

我們設定玩家開始遊戲時有1000元的賭注
遊戲結束的條件是玩家輸光所有的賭注            

from random import randint
money = 1000
while money > 0:
    print('你的總資產為 : %d' % money)
    need_go_on = False
    while True:
        bet = int(input('請輸入下注金額 : '))
        if 0 < bet <= money:
            break
    first = randint(1,6) + randint(1,6)
    print('你骰出了%d點' % first)
    if first == 7 or first == 11:
        print('玩家勝!')
        money += bet
    elif first == 2 or first == 3 or first == 12:
        print('莊家勝!')
        money -= bet
    else:
        need_go_on = True
        
    while need_go_on:
        need_go_on = False    
        second = randint(1, 6) + randint(1, 6)
        print('你骰出了%d點' % second)
        if second == 7:
            print('莊家勝!')
            money -= bet
        elif second == first:
            print('玩家勝!')
            money += bet
        else:
            need_go_on = True     

#生成斐波那契數列的前20個數
num_1 = 1
num_2 = 1
for i in range(1, 20):
    next_num = num_1 + num_2
    num_1 = num_2
    num_2 = next_num
    print(next_num,' ', end = '')
"""

#輸出100以內所有的質數
for num in range(2, 101):
    prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            prime = False
            break
    if prime:        
        print(num, ' ', end = '')     
    