pack = []
decode = []
bad_packs_num = 0

packs_amnt = int(input("Количество пакетов: "))

for i_pack_num in range(packs_amnt):
	print("\nПакет No", i_pack_num + 1)
	for i_bit in range(4):
		print("Биты пакета No", i_bit + 1, ": ", end=" ")
		num = int(input())
		pack.append(num)
	if pack.count(-1) <= 1:
		decode.extend(pack)
	else:
		bad_packs_num += 1
		print("Много ошибок в пакете!")
	pack = []


print("\nПолученное сообщение: ", decode)
print("Количество ошибок в сообщении: ", decode.count(-1))
print("Количество потерянных пакетов: ", bad_packs_num)
