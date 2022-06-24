number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 1
for i in number_list:
    list_i = [multiple*i for multiple in number_list]
    if i < 10:
        print(*list_i)
        i += 1
    else:
        break