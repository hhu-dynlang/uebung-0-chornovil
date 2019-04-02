def flatten(l):
    new_list = list()
    b = False
    for item in l:
        if isinstance(item, list):
            for atoms in item:
                new_list.append(atoms)
            b = True
        else:
            new_list.append(item)
    if b:
        new_list = flatten(new_list)
    return new_list

print(flatten([1,2,[2]]))
print(flatten([1, [2, 4], [6, [42]]]))
