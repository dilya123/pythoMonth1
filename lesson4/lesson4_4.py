names = ["Maruf", "Temirlan", "Seyto"]
print(names)
names.append("Sultan")
print(names)
names.remove("Sultan")
print(names)

for i in range(5):
    name = input()
    names.append(name)


for i in names:
    print(i)
