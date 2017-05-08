
string = input().split()


longest = string[0]
shortest = string[0]

for word in string:

	if len(word) > len(longest):
		longest = word

	if len(word) < len(shortest):
		shortest = word

shortest_list = []
longest_list = []

for word in string:
	if len(word) == len(shortest):
		shortest_list.append(word)

	if len(word) == len(longest):
		longest_list.append(word)

print("The longest words are: ", longest_list)
print("The shortest words are: ", shortest_list)
