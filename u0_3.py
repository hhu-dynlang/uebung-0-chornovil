def pascal(n):
    pascal_list = list()
    if n == 0:
        return pascal_list
    pascal_list.append([1])
    #print(empty_pascal)
    for i in range(n-1):
        print(i)
        size = len(pascal_list[i])-1
        new_list = list()
        new_list.append(1)
        for p in range(size):
            new_list.append(pascal_list[i][p]+pascal_list[i][p+1])
        new_list.append(1)
        pascal_list.append(new_list)
    return pascal_list

print(pascal(4))
