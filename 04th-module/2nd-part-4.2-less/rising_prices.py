prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_percent = int(input("Повышение на первый год: "))
second_percent = int(input("Повышение на второй год: "))


def get_price_with_a_margin(price, percent):
	return round(price * (1 + percent / 100), 2)


prices_after_first_year = [get_price_with_a_margin(i_price, first_percent) for i_price in prices_now]
prices_after_second_year = [get_price_with_a_margin(i_price, second_percent) for i_price in prices_after_first_year]
print(f"Сумма цен за каждый год {sum(prices_now)}, {sum(prices_after_first_year)}, {sum(prices_after_second_year)}")
