numbers = []# Boş bir liste

count = int(input("How many numbers will you enter? "))

for x in range(count):#kullanıcıdan sayı al for döngüsü ile ekle
    num = int(input("Enter a number: "))
    numbers.append(num)

zork = 0# Çift sayılar için toplam
print('Before', zork)

for thing in numbers:
    if thing % 2 == 0:
        zork = zork + thing
    print(zork, thing)

print('After', zork)