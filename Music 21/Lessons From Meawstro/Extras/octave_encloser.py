coll = []
for i in range(100):
    if i == 0:
        root = i
    else:
        root = root +5
        if root > 11:
            root = root-12
    coll.append(root)

print(coll)
