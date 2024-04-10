# Задача 3. IP-адрес
# IP-адрес компьютера состоит из 4 чисел, разделённых точкой.
# Каждое число находится в диапазоне от 0 до 255 (включительно).
#
# Пример правильного адреса: 192.168.1.0
#
# Пример неправильного адреса: 192.168.300.0
#
# Напишите программу, которая получает на вход 4 числа и выводит на экран IP-адрес.
# Используйте переменную ip_address в качестве шаблона. Обеспечьте контроль ввода.
def get_ip():
	i_mask = 1
	ip_addr_list = []
	while i_mask < 5:
		ip_addr_byte = int(input("Введите {i_num} байт IP-адреса: ".format(i_num=i_mask)))
		if ip_addr_byte not in range(0, 256):
			print("Каждый из байтов IP-адреса должен быть в диапазоне от 0 до 255!")
			continue
		ip_addr_list.append(ip_addr_byte)
		i_mask += 1
	ip_addr = ".".join(str(i_byte) for i_byte in ip_addr_list)
	return ip_addr


print(get_ip())