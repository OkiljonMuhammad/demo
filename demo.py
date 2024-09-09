"""“raqamlar” nomli tekst fayl ichiga 1 dan 10 gacha 
sonlarni kiritib, ularning yig'indisini ekranga 
chiqaruvchi dastur yarating."""

with open("raqamlar.txt", "w") as f:
    f.write("1 2 3 4 5 6 7 8 9 10")

with open("raqamlar.txt", "r") as f:
    numbers = f.read()
    mylist = numbers.split()
    mylist = list(map(lambda x: int(x), mylist))
    result = sum(mylist)
print(result)