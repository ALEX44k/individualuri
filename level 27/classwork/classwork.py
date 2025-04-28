qula = int(input("შეიყვანე ქულა"))
if 90 <= qula <= 100:
    print("შესანიშნავი")
elif 75 <= qula <= 89:
    print("კარგი")
elif 50 <= qula <= 74:
    print("დამაკმაყოფილებელი")
elif 0 <= qula <= 49:
    print("დაუგმაყოფილებელი")
else:
    print("არასწორი მონაცემი")

