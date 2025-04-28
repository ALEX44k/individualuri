text = input("შეიყვანე წინადადება: ")
vowels = "აეიოუ"
v = 0
c = 0
for letter in text:
    if letter in vowels:
        v = v + 1
    if letter not in vowels and letter != " ":
        c = c + 1
print("ხმოვნები =", v)
print("თანხმოვნები =", c)