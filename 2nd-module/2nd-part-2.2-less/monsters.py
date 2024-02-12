monsters_count = int(input("How many monsters are there? "))
mage_index = int(input("The Mage's index in the list? "))
# check if the Mage's index is valid
while (mage_index < 1) or (mage_index > monsters_count):
	print("Invalid index. Please try again. ", end = "")
	mage_index = int(input("The Mage's index in the list? "))

monsters_damage = []


# fill in the monsters_damage list
for monster in range(monsters_count):
	monsters_damage.append(int(input("What is the damage of monster #" + str(monster + 1) + "? ")))


for i_monster in range(monsters_count):
	if (monsters_damage[i_monster] < 100) and (i_monster != mage_index - 1):
		monsters_damage[i_monster] += monsters_damage[mage_index - 1]

print("The damage of each monster is:", monsters_damage)
