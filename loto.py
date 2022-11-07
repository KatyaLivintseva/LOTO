import random
prosloe = set()
while True:
    print('Введите номер бочонка')
    try:
        bochonok = int(input())
        generated_range = [*range(1, bochonok+1)] #цифры от 1 до введенного номера
        loto = list(set(generated_range) - prosloe)
        loto.sort(key=lambda _: random.random()) #рандомный порядок
        prosloe.add(bochonok)
        for c in loto:
            print(c)
            input("Нажмите enter")
    except ValueError:
        print("Нужно ввести целое положительное число")

        
        
