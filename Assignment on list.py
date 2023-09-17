my_list = [1, 0, 2, 1, 0, 3, 2, 3, 4, 5, 4, 5, 0, 1, 3, 2, 4, 3]
count_dict = {}
for num in my_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
for num, count in count_dict.items():
    print(f"{num}: {count}")
