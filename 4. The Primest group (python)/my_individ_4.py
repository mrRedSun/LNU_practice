from random import randrange

def input_group(n, m):
	groups = []

	for x in range(m):
		groups.append([])

	for group in groups:
		for x in range(n):
			group.append(randrange(100, 1000))

	return groups

def output(groups_func):
	counter = 1
	for group in groups_func:
		print("Group {} contains:".format(counter))
		counter += 1
		for x in group:
			print(x, end = " ")
		else:
			print()


def primarity_test(number):
	for x in range(2, number):
		if number % x == 0:
			return False
	else:
		return True

n = int(input("n = "))
m = int(input("m = "))

my_groups = input_group(n, m)
output(my_groups)

biggest_group_counter = 0

for group in my_groups:
	counter = 0
	for number in group:
		if primarity_test(number):
			counter += 1
	else:
		if biggest_group_counter < counter:
			biggest_group = group
			biggest_group_counter = counter


print("""There are the most primal numbers in this group:{}
There are {} primal numbers in it""".format(biggest_group, biggest_group_counter))