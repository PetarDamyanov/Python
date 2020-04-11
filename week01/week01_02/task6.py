def birthday_ranges(birthdays, ranges):
	list_people_bd=[]
	for rng in ranges:
		count_rng=0
		for bd in birthdays:
			if (bd>=rng[0] and bd<=rng[1]):
				count_rng+=1
		list_people_bd.append(count_rng)
	print(list_people_bd)

birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])
# [2, 3, 4, 5, 2]
birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)])
# [5, 2, 0, 1]
