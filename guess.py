import random
start = input('輸入起始值: ')
end = input('輸入結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
n = 0
while True:
	n = n+1
	num = input('請輸入數字: ')
	num = int(num)
	if num > r:
		print('比數字大')
	elif num < r:
		print('比數字小')
	elif num == r:
		print('你猜對了!')
		print('你共猜了', n, '次')
		break
	print('你共猜了', n, '次')
