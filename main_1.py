# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = 'Marcus'
# character_list = [letter for letter in name]
# print(character_list)

# list = []
# for i in range(1, 5):
#   list.append(i)
#   new_range = [n + 1 for n in list]
# print(new_range)

# new_list = [num * 2 for num in range(1, 5)]
# print(new_list)


# digits= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# new_digits = [nums for nums in digits if nums % 2 == 0]
# print(new_digits)

names = ['Marcus', 'Franck', 'Alex', 'Junior', 'Arnauld', 'Donald']
new_names = [name.upper() for name in names]
print(new_names)