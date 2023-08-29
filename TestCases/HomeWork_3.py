#Task 3

print("В какую систему перевести градусы?\nКельвины(К) либо Фаренгейты(F)")
a = input()
print("Введите число для конвертации")
b = int(input())

def converter():
    if a == "K" or a == "k":
        с = b - 273.15
        print(str(с)+"K")
    elif a == "F" or a == "f":
        с = b * 1.8 + 32
        print(str(с)+"F")
    else:
        print("Данные не корректны")

converter()


