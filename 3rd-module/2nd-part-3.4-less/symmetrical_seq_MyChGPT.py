def is_symmetric(sequence):
    return sequence == sequence[::-1]

def min_additions_to_make_symmetric(sequence):
    additions = []
    for i in range(len(sequence)):
        if is_symmetric(sequence + additions):
            return len(additions), additions
        else:
            additions.append(sequence[-(i+1)])
    return len(additions), additions

N = int(input("Введите длину последовательности: "))
sequence = []
for i in range(N):
    num = int(input(f"Введите {i + 1}-е число: "))
    sequence.append(num)

count, additions = min_additions_to_make_symmetric(sequence)
print(f"Минимальное количество добавлений: {count}")
print(f"Добавить числа: {additions}")