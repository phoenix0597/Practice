N = int(input("Кол-во участников: "))
K = int(input("Кол-во человек в команде: "))
members = []
num = 1  # count of people
if N % K == 0:  # if count of people can be divided by count of people in team
	for _ in range(N // K):
		members.append(list(range(num, num + K)))
		num += K
	print("Общий список команд:", members)
else:
	print(f"{N} участников невозможно поделить на команды по {K} человек!")
