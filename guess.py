import random
x = input('請輸入隨機數字初始值: ')
y = input('請輸入隨機數字結束值: ')
x = int(x)
y = int(y)
number = random.randint(x,y)
guess_time = 0
while True:
    guess = int(input('請輸入猜的數字: '))
    if guess == number:
        print('猜對了喔')
        guess_time = guess_time + 1
        print('你共猜了' ,guess_time ,'次')
        break
    elif guess < number:
        print('在大一點!')
        guess_time = guess_time + 1
        print('你共猜了' ,guess_time ,'次')
    elif guess > number:
        print('在小一點!')
        guess_time = guess_time + 1
        print('你共猜了' ,guess_time ,'次')
