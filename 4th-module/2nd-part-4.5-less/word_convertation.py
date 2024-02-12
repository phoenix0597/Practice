word = "Привет"
part_1 = word[0:len(word) // 2]
part_2 = word[len(word) // 2:]

print(part_1[::-1] + part_2[::-1])