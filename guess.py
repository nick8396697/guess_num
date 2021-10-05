import random

min = input('請輸入最小值: ')
max = input('請輸入最大值: ')
min = int(min)
max = int(max)

num = random.randint(min, max)

times = 0
while True:
	times = times + 1
	guess = input('請猜數字: ')
	guess = int(guess)
	if guess == num:
		print('恭喜你猜對了!')
		print('你總共猜了', times, '次')
		break
	elif guess > num and guess <= max:
		print('猜錯囉!再猜小一點')
		print('你已經猜了', times, '次')
	elif guess < num and guess >= min:
		print('猜錯囉!再猜大一點')
		print('你已經猜了', times, '次')
	else:
		print('只能猜', min, '~', max)