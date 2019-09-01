import random

r = random.randint(1, 100)

while True:
	num = input('請輸入數字: ')
	num = int(num)
	if num > r:
		print('比數字大')
	elif num < r:
		print('比數字小')
	elif num == r:
		print('你猜對了!')
		break
