import random

min = input('請輸入最小值: ')
max = input('請輸入最大值: ')
min = int(min)
max = int(max)

num = random.randint(min, max)

count = 0
while True:
	count += 1 #count = count + 1
	guess = input('請猜數字: ')
	guess = int(guess)
	if guess == num:
		print('恭喜你猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif guess > num and guess <= max:
		print('猜錯囉!再猜小一點')
	elif guess < num and guess >= min:
		print('猜錯囉!再猜大一點')
	else:
		print('只能猜', min, '~', max)
	print('這是你猜的第', count, '次')